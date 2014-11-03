#!/usr/bin/env python
#A sort of API to the core modules of the software. Additional modules should only use the following functions or else
#there will be unexpected behaviour

import database_interface
import data_input
from threading import Thread

def main():
  thread = Thread(target = server_thread)
  thread.start()
  print "main is done started"
  thread.join()

def server_thread():
  print "Server started"
  data_input.__main()

if __name__ == "__main__":
  main()


