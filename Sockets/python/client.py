import socket
import sys

s = socket.socket()
ip = sys.argv[1] # ip of raspberry pi
host = ip
port = 12345
s.connect((host, port))
print(s.recv(1024))
s.close()
