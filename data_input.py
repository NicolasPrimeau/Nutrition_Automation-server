#Decodes incoming data

def startServer():
  import database_interface
  from socket import * 
  HOST = '' 
  PORT = 50001
  ADDR = (HOST, PORT)
  BUFSIZE = 1024
  serv = socket (AF_INET, SOCK_STREAM)
  serv.bind((ADDR))

  while 1:
    #MODIFY if we are to allow additional data acquistion clients
    serv.listen(1)

    conn, addr = serv.accept()
    print("Accepted connection")
  
    while 1:
      data = conn.recv(BUFSIZE)
      if not data:
        break
      data_router.save_data()

      database.store_data(format(decode_data(data)),database.FOOD)  
    
#Decode from protocol, convert into dictionary
def decode_data(data):
  #!!IMPLEMENT
  #Implement later when proper protocol is established
  return data


#Format dictionary into proper JSON
def format(data):
  #!!IMPLEMENT
  #formatting hapens here
  return data


