import json
import random

def assign_chores(roomies):
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
        return assign_chores(roomies)
    # Assign the chore
    chore_assignment[chore] = name
  # Print the final result!
  print(json.dumps(chore_assignment, sort_keys=True, indent=2))


shared_chores = ['living_room', 'dining_room', 'porches_and_shoe_area']
downstairs_chores = ['downstairs_kitchen_monday', 'downstairs_ktichen_wednesday', 'downstairs_bathroom']
upstairs_chores = ['upstairs_kitchenn', 'upstairs_bathroom', 'hallway_and_stairwell']

default_downstairs = shared_chores + downstairs_chores
default_upstairs = shared_chores + upstairs_chores

roomies = [
    {'name':'Isaac', 
      'allowable_chores': default_downstairs},
    {'name':'Dieter', 
      'allowable_chores': default_downstairs},
    {'name':'Faris', 
      'allowable_chores': default_downstairs},
    {'name':'Justin', 
      'allowable_chores': default_downstairs},
    {'name':'Amr', 
      'allowable_chores': shared_chores + ['downstairs_kitchen_monday', 'downstairs_ktichen_wednesday', 'upstairs_bathroom']},
    {'name':'Zac', 
      'allowable_chores': default_upstairs},
    {'name':'Jake', 
      'allowable_chores': default_upstairs},
    {'name':'Marc', 
      'allowable_chores': default_upstairs},
    {'name':'Matt', 
      'allowable_chores': default_upstairs},
    {'name':'Alex', 
      'allowable_chores': ['trash']}]

print(json.dumps(roomies, sort_keys=True, indent=2))
assign_chores(roomies)

