import socket
import sys
#import os

##username = os.name
##if username == "nt":
##    username = "Windows"
##print "Welcome commander, you are using " + username
#.join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
while 1:
    #HOST, PORT = "10.88.112.174", 9999
    #HOST, PORT = "10.88.114.130", 9997
    HOST, PORT = "10.88.112.173", 9982
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    data = raw_input("Enter your message to send to " + HOST + ":  ")
    # Connect to server and send data
    sock.sendall(data + "\n")
    # Receive data from the server and shut down
    # received = sock.recv(1024)
    print "Sent:     {}".format(data)



















##################@@@@@@@@@@@@@@@@@@ OLD CLIENT @@@@@@@@@@@@@@@@@@@@@###############

####import socket
####import sys
####import os
####
######username = os.name
######if username == "nt":
######    username = "Windows"
######print "Welcome commander, you are using " + username
#####.join(sys.argv[1:])
####
##### Create a socket (SOCK_STREAM means a TCP socket)
####while 1:
####    #HOST, PORT = "10.88.112.174", 9999
####    #HOST, PORT = "10.88.114.130", 9997
####    HOST, PORT = "192.168.12.32", 9999
####    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
####    sock.connect((HOST, PORT))
####    data = raw_input("Enter your message to send to " + HOST + ":  ")
####    # Connect to server and send data
####    sock.sendall(data + "\n")
####    # Receive data from the server and shut down
####    #received = sock.recv(1024)
####    print "Sent:     {}".format(data)
#####    print "Received: {}".format#(received)
####    HOST2, PORT2 = "10.88.112.174", 9999
####    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
####    sock.connect((HOST2, PORT2))
####    # Connect to server and send data
####    sock.sendall(data + "\n")
####    # Receive data from the server and shut down
####    #received = sock.recv(1024)
####    print "Sent:     {}".format(data)






