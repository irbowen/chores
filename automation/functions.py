#!/usr/bin/python3

import json
import constants as c
roomies = c.roomies

def print_allowable_chores():
  ''' Print the allowable chores for each person
  using json.dumps() '''
  print(json.dumps(roomies, sort_keys=True, indent=2))
