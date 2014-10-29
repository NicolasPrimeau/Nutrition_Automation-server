#A sort of API to the core modules of the software. Additional modules should only use the following functions or else
#there will be unexpected behaviour

def main():


def get_data():
  print("Data router: getting data")
  raise NotImplementedError

def check_data():
  print("Data router: checking data")
  raise NotImplementedError

def send_alert():
  print("Data router: sending alert")
  raise NotImplementedError

def save_setting():
  print("Data router: saving setting")
  raise NotImplementedError

def get_setting():
  print("Data router: getting settings")
  raise NotImplementedError

if __name__ == "__main__":
  main()


