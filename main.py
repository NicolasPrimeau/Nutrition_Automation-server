#!/usr/bin/env python
#A sort of API to the core modules of the software. Additional modules should only use the following functions or else
#there will be unexpected behaviour

#Might be more useful
from multiprocessing import Process,Queue
import sys
import time
import database_interface

def main():

  #setup database/ check for proper setup
  setup_p = Process(target = setup)
  setup_p.start()
  setup_p.join()

  #start info checking,data management
  data_p = Process(target=data_manager)
  data_p.start()
  #start TCP server
  server_p = Process(target=start_server)
  server_p.start()

  #Start GUI

  server_p.join()
  data_p.join()
  
def setup():
  sys.stdout.write("Initializating...")
  database_interface.__setup()

  sys.stdout.write("Complete!\n")

#Data manager
def data_manager():
  import info_checking.py
  while 1:
    #do info check
    sys.stdout.write("Checking data...")
    info_checking.check_data()
    sys.stdout.write("Complete!\n")
    sys.stdout.write("Cleaning database...")
    database_interface.cleanup()
    sys.stdout.write("Complete!\n")
    #sleep
    time.sleep()


def start_server():
  import data_input
  while 1:
    sys.stdout.write("Data input server  --  Started\n")
    try:
      data_input.startServer()
    except Error:
      sys.stderr.write("Warning: Server crashed. Restarting Server\n")

    #We should never reach this point, 
    #the loop is completely for redundancy
    #in case the server crashed for any reason

if __name__ == "__main__":
  main()


