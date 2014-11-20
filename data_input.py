#The protocol to be used for now to test is the following:
#-Incoming data must be plain text
#-The text will be JSON

from socket import *
import database_interface
import signal
import errno
import sys
import time

def startServer():

  HOST = '' 
  PORT = 50001
  ADDR = (HOST, PORT)
  BUFSIZE = 1024
  serv = socket (AF_INET, SOCK_STREAM)
  serv.bind((ADDR))

  def itrp_handler(signum,frame):
    sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
    sys.stdout.write("Terminating server process...")
    serv.close()
    sys.stdout.write("Terminated!\n")
    sys.exit()

 
  signal.signal(signal.SIGINT, itrp_handler)
  signal.signal(signal.SIGTERM, itrp_handler)
  signal.signal(signal.SIGQUIT, itrp_handler)

  while 1:
    #MODIFY if we are to allow additional data acquistion clients
    serv.listen(1)

    conn, addr = serv.accept()

    print("Accepted connection")
  
    while 1:
      data = conn.recv(BUFSIZE)
      if not data:
        break
      database_interface.store_data(database_interface.FOOD,decode_data(data))
  
#Decode from protocol, convert into dictionary
def decode_data(data):
  #!!IMPLEMENT
  #Implement properly later when proper protocol is established

  #test implementation
  import json
  import datetime
  info = json.loads(data)
  info['date'] = datetime.datetime.now()

  return info



