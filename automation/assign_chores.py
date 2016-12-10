#!/usr/bin/python3

import datetime
import json
import os
import random
import readline
import shlex
import subprocess
import time

from functions import *
from constants import *

def zero_debts(roomies):
  for roomie in roomies:
      roomie['rent_balance'] = 0
      roomie['util_balance'] = 0

def interactively_update_payments(roomies):
  pass

def interactively_update_charges(roomies):
  charge_rent = input('Charge rent?(yes/no)')
  if charge_rent == 'yes':
    for person in roomies:
      person['rent_balance'] += person['base_rent']
      print(person['rent_balance'])
  comcast = input('How much was comcast? ') or 0
  dte = input('How much was dte - electricity and gas? ') or 0
  aa_water = input('How much was ann arbor water? ') or 0
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

def build_venmo_links(roomies):
  links = []
  friendly_note = 'dec_utils'
  for person in roomies:
    person['total_charge'] = person['rent_balance'] + person['util_balance']
    if person['charge_on_venmo']:
      base_str = 'https://venmo.com/?txn=charge&amount=%s&note=%s&recipients=%s' % (
              str(round(person['total_charge'], 2)), friendly_note, person['venmo_name'])
      person['venmo_url'] = base_str
      links.append({'name': person['name'], 'venmo_link' : person['venmo_url']})

  print(json.dumps(links, sort_keys=True, indent=2))


def main():
  print("Welcome to the 427 Hamplace chore management script\n")

  options = [
      {'command' : 'list', 'desc' : 'Show all the roomates, and what chores they can do'},
      {'command' : 'calc', 'desc' : 'Calculate the bill'},
      {'command' : 'pay', 'desc' : 'Get payments from roommates'},
      {'command' : 'venmo', 'desc' : 'Charge them on venmo'},
      {'command' : 'exit', 'desc' : 'Exit the program'},
      {'command' : 'help', 'desc' : 'Print this menu'}
  ]

  if os.path.isfile('data.json'):
    print('Using custom roomies data, stored in file...')
    with open('data.json') as data_file:
      roomies = json.load(data_file)
  else:
    roomies = static_roomies
    print('Using default roomies data...')

  print_help(options)

  while True:
    cmd, *args = shlex.split(input('> '))
    if cmd == 'exit':
      break
    if cmd == 'help':
      print_help(options)
    if cmd == 'list':
      print_roomies(roomies)
    if cmd == 'venmo':
      build_venmo_links(roomies)
    if cmd == 'calc':
      interactively_update_charges(roomies)
    if cmd == 'pay':
      interactively_update_payments(roomies)
    if cmd == 'clear':
      subprocess.call('clear', shell=True)
    if cmd == 'zero':
      zero_debts(roomies)

if __name__ == '__main__':
  main()

