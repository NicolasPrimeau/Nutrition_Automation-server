__author__ = 'Nixon'

import datetime
import database_interface as database


def generate_consumption_report(days, hours=0):
    delay = datetime.datetime.now() - datetime.timedelta(days=days, hours=hours)

    report = list()
    food_data = database.get_data(database.FOOD)
    purged_data = database.get_data(database.PURGED.DATA)
    for bin in database.get_data(database.CONFIG.BINS):
        temp = dict()
        temp['bin'] = bin['bin']
        temp['name'] = bin['name']
        temp['type'] = bin['type']
        temp['date of purged'] = None
        temp['consumption'] = dict()
        if hours >= 1:
            temp['consumption']['hourly'] = _consumption_hourly(bin['bin'], food_data)
        if days >= 1:
            temp['consumption']['daily'] = _consumption_daily(bin['bin'], food_data)
        if days >= 7:
            temp['consumption']['weekly'] = _consumption_weekly(bin['bin'], food_data)
        if days >= 30:
            temp['consumption']['monthly'] = _consumption_monthly(bin['bin'], food_data)
        report.append(temp)

    # add purged bins
    for bin in database.get_data(database.PURGED.BINS):
        if bin['date'] < delay:
            continue
        temp = dict()
        temp['bin'] = bin['bin']
        temp['name'] = bin['name']
        temp['type'] = bin['type']
        temp['date of purged'] = bin['date']
        temp['consumption'] = dict()
        if hours >= 1:
            temp['consumption']['hourly'] = _consumption_hourly(bin['bin_id'], purged_data)
        if days >= 1:
            temp['consumption']['daily'] = _consumption_daily(bin['bin_id'], purged_data)
        if days >= 7:
            temp['consumption']['weekly'] = _consumption_weekly(bin['bin_id'], purged_data)
        if days >= 30:
            temp['consumption']['monthly'] = _consumption_monthly(bin['bin_id'], purged_data)
        report.append(temp)

    return report


def _consumption_hourly(id, location):
    return __consumption(id, location, datetime.timedelta(hours=1))


def _consumption_daily(id, location):
    return __consumption(id, location, datetime.timedelta(days=1))


def _consumption_weekly(id, location):
    return __consumption(id, location, datetime.timedelta(weeks=1))


def _consumption_monthly(id, location):
    return __consumption(id, location, datetime.timedelta(days=30))


def __consumption(query, location, time_delta):
    ret_val = list()
    start = None
    last = dict()
    last['quantity'] = 0
    temp = None
  
    for entry in location:
        if 'bin_id' in entry:
            if entry['bin_id'] != query:
                continue
        elif int(entry['bin']) != int(query):
            continue

        if start is None:
            start = __get_start(entry['date'], time_delta)
            temp = dict()
            temp['start time'] = start
            temp['decrease'] = 0
            temp['increase'] = 0

        if(entry['date'] - start) > time_delta:
            temp['difference'] = temp['increase'] - temp['decrease']
            temp['end time'] = start+time_delta
            ret_val.append(temp)
            start = __get_start(entry['date'], time_delta)
            temp = dict()
            temp['start time'] = start
            temp['decrease'] = 0
            temp['increase'] = 0

        if entry['quantity'] > last['quantity']:
            temp['increase'] += entry['quantity'] - last['quantity']
        elif entry['quantity'] < last['quantity']:
            temp['decrease'] += last['quantity'] - entry['quantity']
        last = entry
    else:
        if temp is not None:
            temp['difference'] = temp['increase'] - temp['decrease']
            temp['end time'] = start+time_delta
            ret_val.append(temp)
            
    return ret_val




def __get_start(start, td):
    if td <= datetime.timedelta(hours=1):
        return datetime.datetime(year=start.year,
                                 month=start.month,
                                 day=start.day,
                                 hour=start.hour)
    elif td <= datetime.timedelta(days=1):
        return datetime.datetime(year=start.year,
                                 month=start.month,
                                 day=start.day,
                                 hour=0)
    elif td <= datetime.timedelta(days=7):
        return datetime.datetime(year=start.year,
                                 month=start.month,
                                 day=(int(start.day/7)*7),
                                 hour=0)
    elif td <= datetime.timedelta(days=30):
        return datetime.datetime(year=start.year,
                                 month=start.month,
                                 day=1,
                                 hour=0)
