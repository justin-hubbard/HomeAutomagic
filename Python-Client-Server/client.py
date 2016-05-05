#client

import socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))


# default port for socket
port = 12345

# Connection to the server
s.connect(('127.0.0.1', port))

# receive data from the server
print (s.recv(1024).decode())

s.close()
