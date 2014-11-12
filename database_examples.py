#!/usr/bin/env python

import database_interface


contact = {}
contact['name'] = "Nicolas Primeau"
contact['phone'] = "613-915-7187"
contact['email'] = "nicolas.primeau@gmail.com"

#store data
#database_interface.store_data(database_interface.CONTACT,contact)

alarm = {}
alarm['description'] = "General catch all alarm for testing"
alarm['type'] = "quantity"
alarm['flag'] = {}
alarm['flag']['max'] = 100
alarm['flag']['min'] = 20
alarm['target_bins'] = []
alarm['target_bins'] = -1
alarm['contact'] = []
c = {}
c['name'] = "Nicolas Primeau"
c['email'] = True
c['phone'] = False

alarm['contact'].append(c)

#database_interface.store_data(database_interface.ALERT, alarm)

import datetime

food = {}
food['bin'] = 1
food['quantity'] = 0
food['date'] = datetime.datetime.now()

database_interface.store_data(database_interface.FOOD, food)

config = {}
config['bin'] = 1
config['name'] = 'Apple'
config['type'] = 'Fruit'
config['perishable'] = True

database_interface.store_data(database_interface.CONFIG, config)






