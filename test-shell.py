#!/usr/bin/env python


import database_interface, info_checking, data_input
from multiprocessing import Process
import os,sys, signal

pids = {}

def main():

    signal.signal(signal.SIGINT, exit_handler)

    while True:
      cmd = raw_input(">")


      if cmd.lower() == "exit":
         break;
  
      if cmd in cmds:
          cmds[cmd]()
      elif cmd in stop_cmds:
          stop_cmds[cmd]  
      else:
          print("Command not supported")

def start_tcp_server():
    print ("Server started")
    if 'server' not in pids:
        pids['server'] = Process(target = data_input.startServer)


def cleanup_db():
    return

def check_data():
    info_checking.check_data()
    return

def stop_tcp_server():
    os.kill(pid['server'], signal.SIGINT)  

def exit_handler(signal, frame):
    print("\nBye\n")
    sys.exit(0)

def help_func():
    print("I'll allow this eventually")


cmds = {}
cmds['start_server'] = start_tcp_server
cmds['cleanup_db'] = cleanup_db
cmds['check_data'] = check_data
cmds['help'] = help_func

stop_cmds = {}
stop_cmds['stop_server'] = stop_tcp_server


if __name__ == "__main__":
  main()








