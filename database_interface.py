#interface to mongoDB

from pymongo import MongoClient
import datetime
import sys

FOOD = "food"
ALERT = "alert"
CONTACT = "contact"
CONFIG = "config"
DETECTED_CONCERNS = "concerns"

__DATABASE = "Nutrition_Automation"

collections = {}
collections[FOOD] = "food_data"
collections[ALERT] = "alerts"
collections[CONTACT] = "contacts" 
collections[CONFIG] = "config"
collections[DETECTED_CONCERNS] = "concerns"

def __setup():
  # Actually, we don't need any setup up
  # In the case that the database and collections don't exists, 
  # any function accessing the database would create them implicitly 
  return


#Data is a dictionary, type is a string or integer
def store_data( type, data):
  if isinstance(data,dict) and type in collections:
    client = MongoClient()
    db = client[__DATABASE]
    collection = db[collections[type]]
    collection.insert(data);
    client.close()
  else:
    raise LookupError("No Such Collection")
  
def get_data(type,query = {},single = False):
  if type in collections:
    client = MongoClient()
    db = client[__DATABASE]
    collection = db[collections[type]]
    if not single:
      if query == {}: 
        iterator = collection.find()
      else:
        iterator = collection.find(query)
      
      results = []
      for ar in iterator:
        results.append(ar)
      
    else:
      results = collection.find_one(query)
    client.close()
    return results
  else:
    raise LookupError("No Such Collection")  

#cleanup removes all Food entries

def update(type,query,update,create=False):
    if type in collections:
      client = MongoClient()
      db = client[__DATABASE]
      collection = db[collections[type]]
      if collection.count() == 0 and create:
        collection.insert(update)
      else:
        collection.update(query,update)
      client.close() 

def _cleanup():
  day = datetime.datetime.now() - datetime.timedelta(days = 30)
  query = {}
  query['date'] = {'$lte':day}
    
  __remove(FOOD, query)


#query is a dictionary with the elements to choose from

def __remove(type,query):
  
  if type in collections:
    client = MongoClient()
    db = client[__DATABASE]
    collection = db[collections[type]]
    collection.remove(query)
    client.close()
  else:
    raise LookupError("No Such Collection")  




