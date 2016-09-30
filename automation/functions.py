
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

def build_html_from_json(json):
  base_str = '<div class="container"><div class="panel panel-default"><div class="panel-heading"> Chores must be done by midnight on <b>' + get_next_sunday() + '</b></div><table class="table table-striped"><tr><td><b>Chore</b></td><td><b>Name</b></td><td><b>Done?</b></td></tr>'
  for chore,name in sorted(json.items()):
    base_str += '<tr> <td>' + chore + '</td> <td>' + name + '</td> <td> </td> </tr>'
  base_str += '</table></div></div>'
  return base_str

def get_next_sunday():
  ''' Looks at todays date, and then loops until the next
  Sunday.  At that point, it builds and returns the string
  for that date '''
  d = datetime.date.today()
  while d.weekday() != 6:
    d += datetime.timedelta(1)
  return d.strftime("%B %d, %Y")


