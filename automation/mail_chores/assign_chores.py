#!/usr/bin/python3

import datetime
import json
import os
import random
import readline
import shlex
import subprocess
import time

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
  return chore_assignment

def get_next_sunday():
  d = datetime.date.today()
  while d.weekday() != 6:
    d += datetime.timedelta(1)
  return d.strftime("%B %d %Y")

def get_next_wednesday():
  d = datetime.date.today()
  while d.weekday() != 2:
    d += datetime.timedelta(1)
  return d.strftime("%B %d %Y")

def build_csv_from_json(json, data):
  base_str = ''
  for chore, name in sorted(json.items()):
    person = [i for i in data if i['name'] == name]
    assert len(person) == 1
    umich = person[0]['umich']
    date = get_next_wednesday() if 'wednesday' in chore else get_next_sunday()
    base_str += "%s,%s,%s,%s\n" % (name, umich, chore, date)
  return base_str

def main():

  if os.path.isfile('data.json'):
    with open('data.json') as data_file:
      data = json.load(data_file)
  else:
      sys.exit()

  print(build_csv_from_json(assign_chores(data), data))

if __name__ == '__main__':
  main()

