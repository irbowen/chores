
import json
import datetime

from constants import *

def print_help(options):
  ''' Prints a help msg...'''
  print("These are your options...\n")
  for option in options:
    print(option['command'], "\t", option['desc'])

def print_allowable_chores():
  ''' Print the allowable chores for each person
  using json.dumps() '''
  print(json.dumps(roomies, sort_keys=True, indent=2))

def print_venmo_status():
  ''' Print out venmo names, if they exist '''
  for person in roomies:
    if person['charge_on_venmo']:
      out_str = person['name'] + ':' + person['venmo_name']
      print(out_str)

def get_next_sunday():
  ''' Looks at todays date, and then loops until the next
  Sunday.  At that point, it builds and returns the string
  for that date '''
  d = datetime.date.today()
  while d.weekday() != 6:
    d += datetime.timedelta(1)
  return d.strftime("%B %d, %Y")


