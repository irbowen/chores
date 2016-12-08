

shared_chores = ['living_room', 'dining_room', 'porches_and_shoe_area']
downstairs_chores = ['downstairs_kitchen_sunday', 'downstairs_ktichen_wednesday', 'downstairs_bathroom']
upstairs_chores = ['upstairs_kitchen', 'upstairs_bathroom', 'hallway_and_stairwell']

default_downstairs = shared_chores + downstairs_chores
default_upstairs = shared_chores + upstairs_chores

roomies = [
  {
    "allowable_chores":  default_downstairs,
    "name": "Isaac",
    "umich" : "irbowen"
  },
  {
    "allowable_chores":  default_downstairs,
    "name": "Dieter",
    "umich" : "dietdk"
  },
  {
    "allowable_chores":  default_downstairs,
    "umich" : "fdizdar",
    "name": "Faris"
  },
  {
    "allowable_chores":  default_downstairs,
    "name": "Justin",
    "umich" : "jskimmer"
  },
  {
    "allowable_chores":  shared_chores + ['downstairs_kitchen_sunday', 'downstairs_ktichen_wednesday', 'upstairs_bathroom'],
    "name": "Amr",
    "umich" : "aammrrrr"
  },
  {
    "allowable_chores":  default_upstairs,
    "name": "Jake",
    "umich" : "oesjacob"
  },
  {
    "allowable_chores":  default_upstairs,
    "name": "Matt",
    "umich" : "mjdolan"
  },
  {
    "allowable_chores":  default_upstairs,
    "name": "Zac",
    "umich" : "haaszac"
  },
  {
    "allowable_chores":  default_upstairs,
    "name": "Marc",
    "umich" : "marcwm"
  },
  {
    "allowable_chores": [ "trash" ],
    "name": "Alex",
    "umich" : "anicho"
  }
]
