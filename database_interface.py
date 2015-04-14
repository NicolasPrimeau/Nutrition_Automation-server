# interface to mongoDB

from pymongo import MongoClient
import datetime
import guidelines
from enum import Enum


class CONFIG(Enum):
    BINS = "config"


class GUIDELINES(Enum):
    SHELF_TIME = "shelf_time"


class PURGED(Enum):
    BINS = "purged_bins"
    DATA = "purged_data"

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
collections[PURGED.BINS] = "purged_bins"
collections[PURGED.DATA] = "purged_data"

client = None
db = None


def __setup():
    global client
    global db
    # prime database with guideline information
    client = MongoClient()
    db = client[__DATABASE]
    collection = db[collections[GUIDELINES.SHELF_TIME]]

    for struct in guidelines.TIME_LENGTHS:
        collection.remove({'name': struct['name']})
        collection.insert(struct)

    return


# Data is a dictionary, type is a string or integer
def store_data(ty, data):
    if isinstance(data, dict) and ty in collections:
        try:
            collection = db[collections[ty]]
        except TypeError:
            __setup()
            collection = db[collections[ty]]
        collection.insert(data)
    else:
        raise LookupError("No Such Collection")


def get_data(ty, query, single=False, sort=""):
    if ty in collections:
        try:
            collection = db[collections[ty]]
        except TypeError:
            __setup()
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
        else:
            if query == {}:
                iterator = collection.find_one()
            else:
                iterator = collection.find_one(query)
        return iterator
    else:
        raise LookupError("No Such Collection")

    # cleanup removes all Food entries


def update(ty, query, updat, create=False):
    if ty in collections:
        try:
            collection = db[collections[ty]]
        except TypeError:
            __setup()
            collection = db[collections[ty]]
        if collection.count() == 0 and create:
            collection.insert(updat)
        else:
            collection.update(query, updat)


def count(ty):
    if ty in collections:
        try:
            collection = db[collections[ty]]
        except TypeError:
            __setup()
            collection = db[collections[ty]]
        cnt = collection.count()
        return cnt
    else:
        raise LookupError("No Such Collection")


def configure_bin(new_bin):
    old_bin = get_data(CONFIG.BINS, {'bin': new_bin['bin']}, single=True)
    old_bin['date'] = datetime.datetime.now()
    old_bin['bin_id'] = old_bin['_id']
    bin_id = old_bin['_id']
    del old_bin['_id']

    store_data(PURGED.BINS, old_bin)

    update(CONFIG.BINS, {'bin': new_bin['bin']}, {'$set': new_bin})

    for item in get_data(FOOD, {}):
        del item['_id']
        item['bin_id'] = bin_id
        store_data(PURGED.DATA, item)

    __remove(FOOD, {'bin': new_bin['bin']})


def _cleanup():
    day = datetime.datetime.now() - datetime.timedelta(days=30)

    __remove(FOOD, {'date': {'$lte': day}})
    __remove(PURGED.DATA, {'date': {'$lte': day}})
    __remove(PURGED.BINS, {'date': {'$lte': day}})


# query is a dictionary with the elements to choose from

def delete_contact(query):
    __remove(CONTACT, query)


def delete_alert(query):
    __remove(ALERT, query)


def __remove(ty, query):
    if ty in collections:
        try:
            collection = db[collections[ty]]
        except TypeError:
            __setup()
            collection = db[collections[ty]]
        collection.remove(query)
    else:
        raise LookupError("No Such Collection")