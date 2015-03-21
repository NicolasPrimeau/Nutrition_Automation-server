#!/usr/bin/env python

import database_interface


contact = dict()
contact['name'] = "Nicolas Primeau"
contact['phone'] = "6139157187"
contact['email'] = "nicolas.primeau@gmail.com"

# store data
#database_interface.store_data(database_interface.CONTACT,contact)

alarm = dict()
alarm['description'] = "General catch all alarm for testing"
alarm['type'] = "quantity"
alarm['flag'] = dict()
alarm['flag']['max'] = 100.0
alarm['flag']['min'] = 20.0
alarm['target_bins'] = [1, 2]
alarm['contact'] = list()
c = dict()
c['name'] = "Nicolas Primeau"
c['email'] = True
c['phone'] = True

alarm['contact'].append(c)

#database_interface.store_data(database_interface.ALERT, alarm)

import datetime

food = dict()
food['bin'] = 1
food['quantity'] = 0.0
food['date'] = datetime.datetime.now()

database_interface.store_data(database_interface.FOOD, food)

food = dict()
food['bin'] = 2
food['quantity'] = 0.0
food['date'] = datetime.datetime.now()

database_interface.store_data(database_interface.FOOD, food)

config = dict()
config['bin'] = 1
config['name'] = 'Steak'
config['type'] = 'Meat'

#database_interface.store_data(database_interface.CONFIG.BINS, config)

config = dict()
config['bin'] = 2
config['name'] = "Bacon"
config['type'] = "Meat"

#database_interface.store_data(database_interface.CONFIG.BINS, config)





