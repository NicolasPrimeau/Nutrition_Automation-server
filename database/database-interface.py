#Interface to mongoDB

import pymongo

def main():
  store_data()
  get_data()
  _cleanup()

def store_data():
  print("Storing data")
  raise NotImplementedError

def get_data():
  print("Getting data")
  raise NotImplementedError

def _cleanup():
  print("Cleaning up")
  raise NotImplementedError

def __timer():
  print("Database timer")
  raise NotImplementedError

if __name__ == "__main__":
  main()





