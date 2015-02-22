# Checks the consistency of database software

import database_interface
import alert
import datetime
import custom_functions
import guidelines


def check_data():
    #consistency_check()

    alerts = database_interface.get_data(database_interface.ALERT)
    messages = list()

    _check_time_alerts(messages)

    for a in alerts:
        if a['type'] == 'quantity':
            x = _check_quantity_alert(a)
            if len(x) != 0:
                messages.append(x)

    # distille the messages
    # !! Implement later !!
    # For now just send all emails

    if len(messages) != 0:
        database_interface.update(database_interface.DETECTED_CONCERNS, {},
                                  {'info': messages, 'date': datetime.datetime.now()}, create=True)

    # Alert_set is a set of flags raised by one configured alert
    for alert_set in messages:
        # We process every alert in the set seperately
        for a in alert_set:
            #For now !! Remove later
            print("\n\nAddress: " + ", ".join(a['address']))
            print("Subject: " + a['subject'])
            print("Message: " + a['message']['plain'])

            #alert.send_email(a['address'], a['subject'], a['message'])
            #alert.send_text(a['phone_num'], a['message'])


def _check_time_alerts(msgs):

    alerts = dict()

    for bin in database_interface.get_data(database_interface.CONFIG.BINS, {'bin': {'$gt': 0}}):
        guide = database_interface.get_data(database_interface.GUIDELINES.SHELF_TIME, {'name': bin['name'].lower()})
        if len(guide) < 0:
            continue
        i = guide[0]['fridge']['min'].split(",")

        unit = "days"
        i[0] = i[0].split(" ")
        time = i[0][0]
        if len(i[0]) > 1:
            unit = i[0][1]

        if unit == "days":
            time = datetime.datetime.now() - datetime.timedelta(days=int(time))
        if unit == "hours":
            time = datetime.datetime.now() - datetime.timedelta(hours=int(time))
        query = dict()
        query['bin'] = bin['bin']
        query['date'] = {'$gte': time}

        data_since = database_interface.get_data(database_interface.FOOD, query)
        if len(data_since) < 5:
            continue

        query = dict()
        query['target_bins'] = bin['bin']
        query['type'] = 'quantity'

        al = database_interface.get_data(database_interface.ALERT, query)
        if len(al) < 0:
            minimum = 5
        else:
            minimum = al[0]['flag']['min']

        data_since = __sort_by_date(data_since)

        flag = False

        for entry in data_since:
            if entry['quantity'] < minimum:
                flag = True
                break

        if not flag or True:
            msgs.append(__create_time_message())

    return alerts

def __sort_by_date(data_since):
    for index in range(1, len(data_since)):
        currentvalue = data_since[index]
        position = index

        while position > 0 and data_since[position-1]['date'] > currentvalue['date']:
            data_since[position] = data_since[position-1]
            position -= 1

        data_since[position] = currentvalue
    return data_since



def _check_quantity_alert(al):
    time = datetime.datetime.now() - datetime.timedelta(hours=3)

    query = dict()
    if al['target_bins'] != -1:
        query['bin'] = dict()
        query['bin']['$in'] = al['target_bins']
    query['date'] = {'$gte': time}

    data = database_interface.get_data(database_interface.FOOD, query)
    stats_data = dict()

    # gather preliminary information

    for d in data:
        if d['bin'] not in stats_data:
            stats_data[d['bin']] = dict()
            stats_data[d['bin']]['avg'] = 0
            stats_data[d['bin']]['last_reading_date'] = d['date']
            stats_data[d['bin']]['last_reading'] = d['quantity']
            stats_data[d['bin']]['num'] = 0

        stats_data[d['bin']]['avg'] += d['quantity']
        stats_data[d['bin']]['num'] += 1

        if d['date'] > stats_data[d['bin']]['last_reading_date']:
            stats_data[d['bin']]['last_reading'] = d['quantity']
            stats_data[d['bin']]['last_reading_date'] = d['date']

    # Finalize the average computation

    for key in stats_data:
        stats_data[key]['avg'] /= stats_data[key]['num']

    del data
    problems = list()

    for key in stats_data:
        ty = None
        if stats_data[key]['avg'] < al['flag']['min'] and stats_data[key]['last_reading'] < al['flag']['min']:
            ty = "min"
        elif stats_data[key]['avg'] > al['flag']['max'] and stats_data[key]['last_reading'] > al['flag']['max']:
            ty = "max"
        if ty is not None:
            problems.append(__create_quantity_message(
                {"bin": key, "quantity": stats_data[key]['avg'], "date": stats_data[key]['last_reading_date'],
                 "type": ty}, al))

    return problems


def consistency_check():
    time = datetime.datetime.now() - datetime.timedelta(hours=2)

    query = dict()
    query['date'] = {'$gte': time}

    data = database_interface.get_data(database_interface.FOOD, query)

    stats_data = {}

    # setup data, setup avg

    for item in data:

        if item['bin'] not in stats_data:
            stats_data[item['bin']] = {}
            stats_data[item['bin']]['avg'] = 0.0
            stats_data[item['bin']]['cnt'] = 0
            stats_data[item['bin']]['std_dev'] = 0
            stats_data[item['bin']]['concern_cnt'] = 0
        stats_data[item['bin']]['avg'] += item['quantity']
        stats_data[item['bin']]['cnt'] += 1

        # calc average


    for key, stats in stats_data:
        stats_data[key]['avg'] /= stats_data[item['bin']]['cnt']

    # calc raw standard variance, not divided

    for item in data:
        stats_data[item['bin']]['std_dev'] += (item['quantity'] - stats_data[item['bin']]['avg']) ** 2

        # calc std dev

    for key, stats in stats_data:
        stats_data[key]['std_dev'] = (stats_data[key]['std_dev'] / (
        stats_data[key]['cnt'] - stats_data[key]['cnt'] != 1) ) ** (1 / 2)

    # Check the amount of outliers

    for item in data:
        if item['quantity'] > 2 * stats_data[item['bin']]['std_dev']:
            stats_data[item['bin']]['concern_cnt'] += 1

    # print results

    for key, stat in stats_data:
        if stat['concern_cnt'] > 6:
            print("Bin " + str(item['bin']) + " has highly inconsistent data")


def __create_quantity_message(info, ale):
    names = []
    for cont in ale['contact']:
        names.append(cont['name'])
    query = dict()
    query['name'] = {}
    query['name']['$in'] = names

    contacts = database_interface.get_data(database_interface.CONTACT, query)

    msg = dict()
    msg['address'] = []
    msg['phone_num'] = []
    for cont in contacts:
        msg['address'].append(cont['email'])
        msg['phone_num'].append(cont['phone'])

    msg['subject'] = "Low Stock - Bin " + str(info['bin']);

    msg['message'] = {}

    msg['message']['plain'] = info['date'].strftime("%Y-%m-%d") + "\n"
    msg['message']['html'] = "<p>" + msg['message']['plain'] + "</p><br>"

    msg['message']['plain'] = "Stock in Bin " + str(info['bin']) + " is "
    msg['message']['html'] = "<p>" + "Stock in Bin " + str(info['bin']) + " is "

    if info['type'] == "min":
        msg['message']['plain'] += "below configured minimum threshold. Stock must be replenished soon.\n"
        msg['message']['html'] += "below configured minimum threshold. Stock must be replenished soon.</p><br>"
    else:
        msg['message']['plain'] += "above configured maximum threshold.\n"
        msg['message']['html'] += "above configured maximum threshold.</p>"

    return msg


def __create_time_message(info, alert):
    raise NotImplementedError

