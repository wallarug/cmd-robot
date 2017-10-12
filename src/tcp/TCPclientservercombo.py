import socket
import sys
import os
username = os.name
if username == "nt":
    username = "Windows"
print "Welcome commander, you are using " + username
s = socket.socket()         # Create a socket object
host = '10.88.112.173' # Get local machine name
port = 9980
print 'Server started!'
print 'Waiting for clients...'
HOST, PORT = "10.88.112.174", 9996
#HOST, PORT = "10.88.114.173", 9997
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
# Create a socket (SOCK_STREAM means a TCP socket)
while 1:
    x = 0
    data = raw_input("Enter your message to send to " + HOST + ":  ")
    # Connect to server and send data
    sock.sendall(data + "\n")
    print "Sent:     {}".format(data)
    while x < 1:
        msg = c.recv(1024)
        print msg
        x = x + 1
