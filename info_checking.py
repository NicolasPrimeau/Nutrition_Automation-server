#Checks the consistency of database software

import database_interface
import alert

def check_data():
  #get data
  
  message = _alert_check()
  if message:
    alert_module.send_email(message['address'],message['header'],message['content'])

  __check_alert(alert, food_item):
  raise NotImplementedError()  



def _alert_check():
  alerts = database.get_data("if is alert") #fix
  
  for alert in alerts:
    print("alert")
    __check_alert(alert, food_item)


  


