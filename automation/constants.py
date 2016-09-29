
shared_chores = ['living_room', 'dining_room', 'porches_and_shoe_area']
downstairs_chores = ['downstairs_kitchen_sunday', 'downstairs_ktichen_wednesday', 'downstairs_bathroom']
upstairs_chores = ['upstairs_kitchen', 'upstairs_bathroom', 'hallway_and_stairwell']

default_downstairs = shared_chores + downstairs_chores
default_upstairs = shared_chores + upstairs_chores


# All of the starting information for the roomates
roomies = [
    {'name':'Isaac', 
      'charge_on_venmo' : False,
      'allowable_chores': default_downstairs,
      'rent_balance' : 0,
      'util_balance' : 0},
    {'name':'Dieter', 
      'charge_on_venmo' : True,
      'venmo_name' : 'klemchowda',
      'allowable_chores': default_downstairs,
      'rent_balance' : 0,
      'util_balance' : 0},
    {'name':'Faris', 
      'charge_on_venmo' : True,
      'venmo_name' : 'farisdizdarevic',
      'allowable_chores': default_downstairs,
      'rent_balance' : 0,
      'util_balance' : 0},
    {'name':'Justin', 
      'charge_on_venmo' : True,
      'venmo_name' : 'kimsjustin',
      'allowable_chores': default_downstairs,
      'rent_balance' : 0,
      'util_balance' : 0},
    {'name':'Amr', 
      'charge_on_venmo' : True,
      'venmo_name' : 'kimsjustin',
      'allowable_chores': shared_chores + ['downstairs_kitchen_monday', 'downstairs_ktichen_wednesday', 'upstairs_bathroom'],
      'rent_balance' : 0,
      'util_balance' : 0},
    {'name':'Jake', 
      'charge_on_venmo' : True,
      'venmo_name' : 'Jacob-Oestreich',
      'allowable_chores': default_upstairs,
      'rent_balance' : 0,
      'util_balance' : 0},
    {'name':'Matt', 
      'charge_on_venmo' : True,
      'venmo_name' : 'Matt-Dolan-5',
      'base_rent' : 476,
      'allowable_chores': default_upstairs,
      'rent_balance' : 0,
      'util_balance' : 0},
    {'name':'Zac', 
      'charge_on_venmo' : False,
      'allowable_chores': default_upstairs,
      'rent_balance' : 0,
      'util_balance' : 0},
    {'name':'Marc', 
      'charge_on_venmo' : False,
      'base_rent' : 411,
      'allowable_chores': default_upstairs,
      'rent_balance' : 0,
      'util_balance' : 0},
    {'name':'Alex', 
      'charge_on_venmo' : False,
      'base_rent' : 411,
      'allowable_chores': ['trash'],
      'rent_balance' : 0,
      'util_balance' : 0}]


