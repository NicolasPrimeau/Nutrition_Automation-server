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
            report[bin['bin']]['consumption']['weekly'] = _consumption_monthly(bin['bin'], database.FOOD)

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
            report[bin['bin']]['consumption']['weekly'] = _consumption_monthly(bin['bin'], database.FOOD)

    return report


def _consumption_hourly(id, location):

    total_decrease = 0

    for entry in database.get_data(location, {'bin': id}):
        pass

    return total_decrease


def _consumption_daily(id, location):

    total_decrease = 0

    for entry in database.get_data(location, {'bin': id}):
        pass

    return total_decrease


def _consumption_weekly(id, location):

    total_decrease = 0

    for entry in database.get_data(location, {'bin': id}):
        pass

    return total_decrease


def _consumption_monthly(id, location):
    total_decrease = 0

    for entry in database.get_data(location, {'bin': id}):
        pass

    return total_decrease
