#!/usr/bin/env python
#A sort of API to the core modules of the software. Additional modules should only use the following functions or else
#there will be unexpected behaviour

#Might be more useful
from multiprocessing import Process,Queue
import sys
import time
import database_interface
import info_checking
import signal
import data_input
import errno 

def main():

  processes = []

  #setup database/ check for proper setup
  setup_p = Process(target = setup)
  setup_p.start()
  setup_p.join()

  del setup_p

  #Start Info checking
  #!! Not Implemented !!
  processes.append(Process(target=check_info))

  #start Database Management
  # !! Not Implemented !!
  processes.append(Process(target = database_management))

  #start TCP server
  processes.append(Process(target=start_server))

  #Start GUI
  # !! Not implemented !!
  #processes.append(Process(target=start_gui))

  for p in processes:
    p.start()

  for p in processes:
    p.join()

  sys.stderr.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
  sys.stderr.write("Error - Nutrition System terimnated\n")
  
def setup():
  sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
  sys.stdout.write("Initializating...")
  database_interface.__setup()

  sys.stdout.write("Complete!\n")

#Info Checking
def check_info():
  signal.signal(signal.SIGINT,check_info_exit_handler)
  signal.signal(signal.SIGTERM, check_info_exit_handler)
  signal.signal(signal.SIGQUIT, check_info_exit_handler)

  while 1:
    #do info check
    sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
    sys.stdout.write("Checking data...\n")
    info_checking.check_data()
    sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
    sys.stdout.write("Checking data... Complete!\n")
    #sleep
    time.sleep(7200)

def check_info_exit_handler(signum,frame):
  sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
  sys.stdout.write("Terminating info checking process...")
  sys.stdout.write("Terminated!\n")
  sys.exit()

#Database handler
def database_management():
  signal.signal(signal.SIGINT, database_management_exit_handler)
  signal.signal(signal.SIGTERM, database_management_exit_handler)
  signal.signal(signal.SIGQUIT, database_management_exit_handler)

  while 1:
    #cleanup database
    sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
    sys.stdout.write("Cleaning up database...\n")
    database_interface._cleanup()
    sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
    sys.stdout.write("Cleaning up database... Complete!\n")
    time.sleep(24*60*60)    

def database_management_exit_handler(signum, frame):
  sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
  sys.stdout.write("Terminating database management process...")
  sys.stdout.write("Terminated!\n")
  sys.exit()

#TCP Server handler
def start_server():
  while 1:
    sys.stdout.write(time.strftime("%d-%m-%Y - %H:%M") + "  ")
    sys.stdout.write("Data input server... Started\n")
    
    data_input.startServer()

    #We should never reach this point, 
    #the loop is completely for redundancy
    #in case the server crashed for any reason

if __name__ == "__main__":
  main()


