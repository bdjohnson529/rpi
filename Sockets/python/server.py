import socket
import sys

s = socket.socket()
ip = sys.argv[1]  #ip of raspberry pi
host = ip
port = 12345
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.send('Hello World!')
  c.close()
