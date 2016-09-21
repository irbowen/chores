import json
import random

date = 'Sunday, Sept. 25th'

shared_chores = ['living_room', 'dining_room', 'porches_and_shoe_area']
downstairs_chores = ['downstairs_kitchen_monday', 'downstairs_ktichen_wednesday', 'downstairs_bathroom']
upstairs_chores = ['upstairs_kitchenn', 'upstairs_bathroom', 'hallway_and_stairwell']

default_downstairs = shared_chores + downstairs_chores
default_upstairs = shared_chores + upstairs_chores

roomies = [
    {'name':'Isaac', 
      'charge_on_venmo' : False,
      'allowable_chores': default_downstairs},
    {'name':'Dieter', 
      'charge_on_venmo' : True,
      'venmo_name' : 'klemchowda',
      'allowable_chores': default_downstairs},
    {'name':'Faris', 
      'charge_on_venmo' : True,
      'venmo_name' : 'farisdizdarevic',
      'allowable_chores': default_downstairs},
    {'name':'Justin', 
      'charge_on_venmo' : True,
      'venmo_name' : 'kimsjustin',
      'allowable_chores': default_downstairs},
    {'name':'Amr', 
      'charge_on_venmo' : True,
      'venmo_name' : 'kimsjustin',
      'allowable_chores': shared_chores + ['downstairs_kitchen_monday', 'downstairs_ktichen_wednesday', 'upstairs_bathroom']},
    {'name':'Jake', 
      'charge_on_venmo' : True,
      'venmo_name' : 'Jacob-Oestreich',
      'allowable_chores': default_upstairs},
    {'name':'Matt', 
      'charge_on_venmo' : True,
      'venmo_name' : 'Matt-Dolan-5',
      'base_rent' : 476,
      'allowable_chores': default_upstairs},
    {'name':'Zac', 
      'charge_on_venmo' : False,
      'allowable_chores': default_upstairs},
    {'name':'Marc', 
      'charge_on_venmo' : False,
      'base_rent' : 411,
      'allowable_chores': default_upstairs},
    {'name':'Alex', 
      'charge_on_venmo' : False,
      'base_rent' : 411,
      'allowable_chores': ['trash']}]

def print_venmo_status():
  for person in roomies:
    if person['charge_on_venmo']:
      out_str = person['name'] + ':' + person['venmo_name']
      print(out_str)

def calculate_total_charges():

  total_rent = input('How much was rent? ')
  rent_sum = 0
  count = 0
  for person in roomies:
    if 'base_rent' in person:
      rent_sum += person['base_rent']
      count += 1
  
  print(rent_sum)
  remaining_rent = float(total_rent) - float(rent_sum)
  print(remaining_rent)
  rent_per_person = remaining_rent / (len(roomies) - count)
  print(rent_per_person)

  for person in roomies:
    if 'base_rent' not in person:
      person['base_rent'] = rent_per_person

  comcast = input('How much was comcast? ')
  dte = input('How much was dte - electricity and gas? ')
  aa_water = input('How much was ann arbor water? ')
  utils_per_person = sum([float(comcast), float(dte), float(aa_water)])/len(roomies)
  print('The utils will be %s per person' % (utils_per_person))
  
  for person in roomies:
    p = {}
    p['total_charge'] = person['base_rent'] + utils_per_person
    p['base_rent'] = person['base_rent']
    if not person['charge_on_venmo']:
      print(p)
    if person['charge_on_venmo']:
      base_str = 'https://venmo.com/?txn=charge&amount=' + str(p['total_charge'])
      base_str += '&note=rent&recipients=' + person['venmo_name']
      print(base_str)

def print_allowable_chores():
  ''' Print the allowable chores for each person
  using json.dumps() '''
  print(json.dumps(roomies, sort_keys=True, indent=2))

def make_api_call():
  print("Not done yet")

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
  base_str = '''
    <div class="container">
      <div class="panel panel-default">
        <div class="panel-heading"> Chores must be done by midnight on <b>'''
  base_str += date
  base_str += '''</b> </div>
          <table class="table table-striped">
            <tr>  <td><b>Chore</b></td>                   <td><b>Name</b></td>    <td><b>Done?</b></td></tr>'''

  for chore,name in chore_assignment.items():
    base_str += '<tr> <td>'
    base_str += chore
    base_str += '</td> <td>'
    base_str += name
    base_str += '</td> <td> </td> </tr>'
  
  base_str += r'</table></div></div>'
  print(base_str)

def main():
    print("Welcome to the 427 Hamplace chore management script\n")

    options = [
        {"name": "Show all the roomates, and what chores they can do", "fn": print_allowable_chores},
        {"name": "Create json for chores", "fn": assign_chores},
        {"name": "Create html", "fn": build_html_from_json},
        {"name": "Print venmo status", "fn": print_venmo_status},
        {"name": "Calculate bill for venmo", "fn": calculate_total_charges}
    ]

    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i]["name"])

    option = input("\nSelect an option: ")

    try:
        selected_option = options[int(option) - 1]
    except:
        print("\nERROR: Invalid option. Script done.")
        return

    print("")
    selected_option["fn"]()

if __name__ == '__main__':
  main()

