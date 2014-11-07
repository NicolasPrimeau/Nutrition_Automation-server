#interface to mongoDB

from pymongo import MongoClient
import datetime
import sys

FOOD = "food"
ALERT = "alert"
CONTACT = "contact"

__DATABASE = "Nutrition_Automation"

collections = {}
collections[FOOD] = "food_data"
collections[ALERT] = "alerts"
collections[CONTACT] = "contacts" 

def __setup():
  # Actually, we don't need any setup up
  # In the case that the database and collections don't exists, 
  # any function accessing the database would create them implicitly 
  return


#Data is a dictionary, type is a string or integer
def store_data( type, data):
  if isinstance(data,dict) and (type == FOOD or type == ALERT or type == CONTACT):
    client = MongoClient()
    db = client[__DATABASE]
    collection = db[collections[type]]
    collection.insert(data);
    client.close()
  else:
    raise LookupError("No Such Collection")
  
def get_data(type,query = {},single = False):
  if type == FOOD or type == ALERT or type == CONTACT:
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

def _cleanup():
  day = datetime.datetime.now() - datetime.timedelta(days = 30)
  query = {}
  query['date'] = {'$lte':day}
  
  __remove(FOOD, query)

#query is a dictionary with the elements to choose from

def __remove(type,query):
  if type == FOOD or tpye == ALERT or type == CONTACT:
    client = MongoClient()
    db = client[__DATABASE]
    collection = db[collections[type]]
    collection.remove(query)
    client.close()
  else:
    raise LookupError("No Such Collection")  




