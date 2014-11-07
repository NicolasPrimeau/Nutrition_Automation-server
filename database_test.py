#!/usr/bin/env python

import database_interface

test_data = {}
test_data['name'] = "helloworld"
test_data['value'] = 12345

t2 = {}
t2['name'] = "banana"
t2['value'] = 565656

#store data
database_interface.store_data(database_interface.FOOD,test_data)
database_interface.store_data(database_interface.FOOD,t2)

#get data
items = database_interface.get_data(database_interface.FOOD)

for item in items:
  print item['name']
  print item['value']


#remove
for item in items:
  database_interface.__remove(database_interface.FOOD, item)
  
