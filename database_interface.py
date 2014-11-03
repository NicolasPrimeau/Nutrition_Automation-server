#interface to mongoDB

from pymongo import MongoClient

FOOD = "food"
ALERT = "alert"
CONTACT = "contact"

__DATABASE = "Nutrition_Automation"

collections = {}
collections[FOOD] = "food_data"
collections[ALERT] = "alerts"
collections[CONTACT] = "contacts" 


#Data is a dictionary, type is a string or integer
def store_data( type, data):
  if isinstance(data,dict) and (type == FOOD or type == ALERT or type == CONTACT):
    client = MongoClient()
    db = client[__DATABASE]
    collection = db[collections[type]]
    collection.insert(data);
    client.close()
  else:
    raise LookupError("No such database type")
  
def get_data(type,query = "",single = False):
  if type == FOOD or type == ALERT or type == CONTACT:
    client = MongoClient()
    db = client[__DATABASE]
    collection = db[collections[type]]
    if not single:
      if query == "": 
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
    raise LookupError("No such database type")  

def cleanup():
  print("Cleaning up")
  raise NotImplementedError

def _setup():
  

  print("Setting up database")
  raise NotImplementedError






