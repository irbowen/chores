#!/usr/bin/python3

import json
import random
import time
import readline
import shlex

import functions as f
import constants as c

roomies = c.roomies

date = 'Sunday, Sept. 25th'

def print_venmo_status():
  for person in roomies:
    if person['charge_on_venmo']:
      out_str = person['name'] + ':' + person['venmo_name']
      print(out_str)

def interactively_update_charges(previous_charges):
  total_rent = input('How much was rent? ')
  rent_sum = 0
  count = 0
  for person in roomies:
    if 'base_rent' in person:
      rent_sum += person['base_rent']
      count += 1
  
  remaining_rent = float(total_rent) - float(rent_sum)
  rent_per_person = remaining_rent / (len(roomies) - count)
  rent_str = 'Rent per person is ' + str(rent_per_person)
  print(rent_str)

  for person in roomies:
    if 'base_rent' not in person:
      person['base_rent'] = rent_per_person

  comcast = input('How much was comcast? ')
  dte = input('How much was dte - electricity and gas? ')
  aa_water = input('How much was ann arbor water? ')
  utils_per_person = sum([float(comcast), float(dte), float(aa_water)])/len(roomies)
  print('The utils will be %s per person' % (utils_per_person))

def build_venmo_links():
  for person in roomies:
    person['total_charge'] = person['base_rent'] + utils_per_person
    if person['charge_on_venmo']:
      base_str = 'https://venmo.com/?txn=charge&amount=' + str(person['total_charge'])
      base_str += '&note=rent&recipients=' + person['venmo_name']
      person['venmo_url'] = base_str
 
      driver = webdriver.Chrome()
      driver.get(base_str);
      time.sleep(5) # Let the user actually see something!
      search_box = driver.find_element_by_name('q')
      search_box.send_keys('ChromeDriver')
      search_box.submit()
      time.sleep(5) # Let the user actually see something!
      driver.quit()
  print(json.dumps(roomies, sort_keys=True, indent=2))

def calculate_total_charges():
  print('First, we load the current state of the debt from our state file')

  with open('data.json') as data_file:
    data = json.load(data_file)
    interactively_update_charges(data)
    dump_to_file()
    build_venmo_links()

def assign_chores():
  # Keep track of how many times we have failed to assign chores
  # given the current configuration
  fail_count = 0
  
  # The current chore assignment
  chore_assignment = {}

  # We look at each person, and try to build a chore schedule
  for person in roomies:
    # Get their name and a chore they can do
    name = person['name']
    chore = random.choice(person['allowable_chores'])
    # Check to make sure no one else is already doing this chore
    while (chore in chore_assignment):
      fail_count += 1
      chore = random.choice(person['allowable_chores'])
      # If we have failed more than 1000 times, give up and call the function again
      if (fail_count > 1000):
        return assign_chores()
    # Assign the chore
    chore_assignment[chore] = name
  # Print the final result!
  print(json.dumps(chore_assignment, sort_keys=True, indent=2))
  return chore_assignment

def build_html_from_json():
  chore_assignment = assign_chores()
  base_str = '<div class="container"><div class="panel panel-default"><div class="panel-heading"> Chores must be done by midnight on <b>'
  base_str += date
  base_str += '</b></div><table class="table table-striped"><tr><td><b>Chore</b></td><td><b>Name</b></td><td><b>Done?</b></td></tr>'

  for chore,name in sorted(chore_assignment.items()):
    base_str += '<tr> <td>'
    base_str += chore
    base_str += '</td> <td>'
    base_str += name
    base_str += '</td> <td> </td> </tr>'

  base_str += r'</table></div></div>'
  print(base_str)


def print_help(options):
  print("These are your options...\n")
  for option in options:
    print(option['command'], "\t", option['desc'])


def main():
    print("Welcome to the 427 Hamplace chore management script\n")

    options = [
        {'command' : 'list', 'desc' : 'Show all the roomates, and what chores they can do'},
        {'command' : 'json', 'desc' : ''},
        {'command' : 'html', 'desc' : ''},
        {'command' : 'venmo', 'desc' : ''},
        {'command' : 'calc', 'desc' : 'Calculate the bill'},
        {'command' : 'exit', 'desc' : 'Exit the program'},
        {'command' : 'help', 'desc' : 'Print this menu'}
    ]

    while True:
      cmd, *args = shlex.split(input('> '))
      if cmd == 'exit':
        break
      if cmd == 'help':
        print_help(options)

if __name__ == '__main__':
  main()

