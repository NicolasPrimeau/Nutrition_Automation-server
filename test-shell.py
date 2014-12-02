#!/usr/bin/env python


import database_interface
import info_checking
import signal
from multiprocessing import Process
import data_input
import os 

pids = {}

def main():

  while True:
    cmd = raw_input(">")


    if cmd.lower() == "exit":
     break;
  
    if cmd in cmds:
      cmds[cmd]()
    elif cmd in stop_cmds:
      stop_cmds[cmd]  


def start_tcp_server():
  print ("Server started")
  if 'server' not in pids:
    pids['server'] = Process(target = data_input.startServer)


def cleanup_db():
  return

def check_data():
  return

def stop_tcp_server():
  os.kill(pid['server'], signal.SIGINT)  






cmds = {}
cmds['start_server'] = start_tcp_server
cmds['cleanup_db'] = cleanup_db
cmds['check_data'] = check_data

stop_cmds = {}
stop_cmds['stop_server'] = stop_tcp_server


if __name__ == "__main__":
  main()








