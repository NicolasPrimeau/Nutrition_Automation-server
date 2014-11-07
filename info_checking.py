#Checks the consistency of database software

import database_interface
import alert
import datetime

def check_data():

  #process time alerts
  alerts = database_interface.get_data(database_interface.ALERT)
  messages = []
  for alert in alerts:
    if alert['type'] == 'time':
      messages.append(_check_time_alert(alert))
    elif alert['type'] == 'quantity':
      messages.append(_check_quantity_alert(alert))
  
  #distille the messages

  ## !! Implement later !!
  # For now just send all emails
   
  for msg in messages:
    alert.send_email(msg['address'],msg['subject'],msg['address'])


  
def _check_time_alert(alert):
  # !! Remove Later !!
  raise NotImplementedError
  # !!              !!

  query = {}
  query['number'] = {}
  query['number']['$in'] = alert['target_bins']
    

  #if month difference is bigger than what is specified in the alert
  if "month" in alert['flag']:
    pass  


  #if day difference is bigger than what is specified in the alert
  if "day" in alert['flag']:
    pass


  #if hour difference is bigger than what is specified in the alert 
  if "hour" in alert['flag']:
    pass


  database_interface.get_data(query)

def _check_quantity_alert(alert):
  # !! remove later !!
  raise NotImplementedError
  # !!              !!


  time = datetime.datetime.now() - datetime.timedelta(hours=2)
  
  query = {}
  query['number'] = {}
  query['number']['$in'] = alert['target_bins']
  query['date'] = {'$gte':time}
  
  data = database_interface.get_data(database_interface.FOOD,query)
  stats_data = {}

  #gather preliminary information

  for d in data:
    if d['number'] not in stats_data:
      stats_data[d['number']] = {}
      stats_data[d['number']]['avg'] = 0
      stats_data[d['number']]['last_reading_data'] = d['date']
      stats_data[d['number']]['last_reading'] = d['quantity']
      stats_data[d['number']]['num'] = 0

    stats_data[d['number']]['avg'] += d['quantity']
    stats_data[d['number']]['num'] += 1
 
    if d['date'] > stats_data[d['number']]['last_reading_date']:
      stats_data[d['number']]['last_reading'] = d['quantity']
      stats_data[d['number']]['last_reading_data'] = d['date']

  # Finalize the average computation

  for key,stat in stats_data:
    stats_data[key]['avg'] /= stats_data[key]['num']

  del data
  problems = []

  for key,d in stats_data:
    if stats_data[key]['avg'] < alert['flag']['quantity'] and stats[key]['last_reading'] < alert['flag']['quantity']:
      problems.append(__create_quantity_message({"bin" : key, "quantity" : stats_data[key]['avg'], "date" : stats_data[key]['last_reading_date']}, alert))

  return problems


def consistency_check():
  raise NotImplementedError

def __create_quantity_message(info,alert):
  raise NotImplementedError


def __create_time_message(info,alert):
  raise NotImplementedError

