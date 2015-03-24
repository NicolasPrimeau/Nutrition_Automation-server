# interface to mongoDB

from pymongo import MongoClient
import datetime
import guidelines
from enum import Enum


class CONFIG(Enum):
    BINS = "config"


class GUIDELINES(Enum):
    SHELF_TIME = "shelf_time"


FOOD = "food"
ALERT = "alert"
CONTACT = "contact"
DETECTED_CONCERNS = "concerns"
CLIENTS = "clients"
PLAIN_TEXT_MESSAGES = 'plain_concerns'


__DATABASE = "Nutrition_Automation"
# if needed eventually
__USER = "Nutrition_Automation"
__PASSWORD = "Nutrition_Automation_Password"

collections = dict()
collections[FOOD] = "food_data"
collections[ALERT] = "alerts"
collections[CONTACT] = "contacts"
collections[CONFIG.BINS] = "bins"
collections[DETECTED_CONCERNS] = "concerns"
collections[GUIDELINES.SHELF_TIME] = "shelftime"
collections[CLIENTS] = "clients"
collections[PLAIN_TEXT_MESSAGES] = "plain_concerns"


def __setup():
    # prime database with guideline information
    client = MongoClient()
    db = client[__DATABASE]
    collection = db[collections[GUIDELINES.SHELF_TIME]]

    for struct in guidelines.TIME_LENGTHS:
        collection.remove({'name': struct['name']})
        collection.insert(struct)

    client.close()
    return


# Data is a dictionary, type is a string or integer
def store_data(ty, data):
    if isinstance(data, dict) and ty in collections:
        client = MongoClient()
        db = client[__DATABASE]
        collection = db[collections[ty]]
        collection.insert(data)
        client.close()
    else:
        raise LookupError("No Such Collection")


def get_data(ty, query=dict(), single=False,sort=""):
    if ty in collections:
        client = MongoClient()
        db = client[__DATABASE]
        collection = db[collections[ty]]
        if not single:
            if query == {} and not sort == "":
                iterator = collection.find()
            elif query == {} and sort != "":
                iterator = collection.find().sort(sort, 1)
            elif sort != "":
                iterator = collection.find(query).sort(sort, 1)
            else:
                iterator = collection.find(query)

            results = list()
            for ar in iterator:
                results.append(ar)

        else:
            results = collection.find_one(query)
        client.close()
        return results
    else:
        raise LookupError("No Such Collection")

    # cleanup removes all Food entries


def update(ty, query, updat, create=False):
    if ty in collections:
        client = MongoClient()
        db = client[__DATABASE]
        collection = db[collections[ty]]
        if collection.count() == 0 and create:
            collection.insert(updat)
        else:
            collection.update(query, updat)
        client.close()


def count(ty, query=dict()):
    if ty in collections:
        client = MongoClient()
        db = client[__DATABASE]
        collection = db[collections[ty]]
        cnt = collection.count(query)
        client.close()
        return cnt
    else:
        raise LookupError("No Such Collection")


def configure_bin(new_bin):
    update(CONFIG.BINS, {'bin': new_bin['bin']}, new_bin)
    __remove(FOOD, {'bin': new_bin['bin']})


def _cleanup():
    day = datetime.datetime.now() - datetime.timedelta(days=30)
    query = dict()
    query['date'] = {'$lte': day}

    __remove(FOOD, query)


# query is a dictionary with the elements to choose from

def delete_contact(query):
    __remove(CONTACT, query)

def __remove(ty, query):
    if ty in collections:
        client = MongoClient()
        db = client[__DATABASE]
        collection = db[collections[ty]]
        collection.remove(query)
        client.close()
    else:
        raise LookupError("No Such Collection")




