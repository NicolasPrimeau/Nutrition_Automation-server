__author__ = 'Nixon'

import datetime
import database_interface as database


def generate_consumption_report(days, hours=0):
    delay = datetime.datetime.now() - datetime.timedelta(days=days, hours=hours)

    report = dict()
    for bin in database.get_data(database.CONFIG.BINS):
        report[bin['bin']] = dict()
        report[bin['bin']]['name'] = bin['name']
        report[bin['bin']]['type'] = bin['type']
        report[bin['bin']]['date of purged'] = None
        report[bin['bin']]['consumption'] = dict()
        if hours >= 1:
            report[bin['bin']]['consumption']['hourly'] = _consumption_hourly(bin['bin'], database.FOOD)
        if days >= 1:
            report[bin['bin']]['consumption']['daily'] = _consumption_daily(bin['bin'], database.FOOD)
        if days >= 7:
            report[bin['bin']]['consumption']['weekly'] = _consumption_weekly(bin['bin'], database.FOOD)
        if days >= 30:
            report[bin['bin']]['consumption']['monthly'] = _consumption_monthly(bin['bin'], database.FOOD)

    # add purged bins
    for bin in database.get_data(database.PURGED.BINS, {'date': {'date': {'$lte': delay}}}):
        report[bin['bin']] = dict()
        report[bin['bin']]['name'] = bin['name']
        report[bin['bin']]['type'] = bin['type']
        report[bin['bin']]['date of purged'] = bin['date']
        report[bin['bin']]['consumption'] = dict()
        if hours >= 1:
            report[bin['bin']]['consumption']['hourly'] = _consumption_hourly(bin['bin'], database.FOOD)
        if days >= 1:
            report[bin['bin']]['consumption']['daily'] = _consumption_daily(bin['bin'], database.FOOD)
        if days >= 7:
            report[bin['bin']]['consumption']['weekly'] = _consumption_weekly(bin['bin'], database.FOOD)
        if days >= 30:
            report[bin['bin']]['consumption']['monthly'] = _consumption_monthly(bin['bin'], database.FOOD)

    return report


def _consumption_hourly(id, location):
    return __consumption(id, location, datetime.timedelta(hours=1))


def _consumption_daily(id, location):
    return __consumption(id, location, datetime.timedelta(days=1))


def _consumption_weekly(id, location):
    return __consumption(id, location, datetime.timedelta(weeks=1))


def _consumption_monthly(id, location):
    return __consumption(id, location, datetime.timedelta(days=30))


def __consumption(id, location, time_delta):
    ret_val = list()
    start = None
    last = dict()
    last['quantity'] = 0
    temp = None

    for entry in database.get_data(location, {'bin': id}):

        if start is None:
            start = entry['date']

        if(entry['date'] - start) > time_delta or start == entry['date']:
            if start != entry['date']:
                ret_val.append(temp)
            temp = dict()
            temp['start time'] = start
            temp['end time'] = entry['date']
            start = entry['date']
            temp['decrease'] = 0
            temp['increase'] = 0
        if entry['quantity'] > last['quantity']:
            temp['increase'] += entry['quantity'] - last['quantity']
        elif entry['quantity'] < last['quantity']:
            temp['decrease'] += last['quantity'] - entry['quantity']
        last = entry
    else:
        if temp is not None:
            temp['end time'] = last['date']
            ret_val.append(temp)
            
    return ret_val




