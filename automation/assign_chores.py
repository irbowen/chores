#!/usr/bin/python3

import datetime
import json
import os
import random
import subprocess
import readline
import shlex
import time

from functions import *
from constants import *

def interactively_update_charges():
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

  update = input('Would you like to update the data.json file?(yes/no)')
  if update == 'yes':
    for roomie in roomies:
      roomie['util_balance'] += utils_per_person
    print('Cool, let\'s do it')
    with open('data.json', 'w') as outfile:
          json.dump(roomies, outfile, sort_keys=True, indent=2)
  else:
    print('Okay, but it doesn\'t make much sense to run this script then...')

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
  return chore_assignment


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

    if os.path.isfile('data.json'):
      print('Using custom roomies data, stored in file...')
      with open('data.json') as data_file:
        data = json.load(data_file)
    else:
      data = None
      print('Using default roomies data...')
    if data is None:
      print('data is none')
    else:
      roomies = data
    print_help(options)

    while True:
      cmd, *args = shlex.split(input('> '))
      if cmd == 'exit':
        break
      if cmd == 'help':
        print_help(options)
      if cmd == 'list':
        print_allowable_chores()
      if cmd == 'json':
        print(json.dumps(assign_chores(), sort_keys=True, indent=2))
      if cmd == 'html':
        print(build_html_from_json(assign_chores()))
      if cmd == 'calc':
        interactively_update_charges()
      if cmd == 'clear':
        subprocess.call('clear', shell=True)
if __name__ == '__main__':
  main()

