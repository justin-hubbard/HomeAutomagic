import socket

s = socket.socket()
print("Sock success")

port = 12345

s.bind(('', port))
print ("socket bound to %s" % (port))

s.listen(5)
print ("socket is listening")

while True:
    c, addr = s.accept()
    print ('got connection from', addr)

    c.send('Thank you for connecting'.encode())
    c.close()
