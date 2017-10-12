import socket
import sys
import os
username = os.name
if username == "nt":
    username = "Windows"
    print "Welcome commander, you are using " + username
else:
    print "Welcome Linux User!"

HOST, PORT = "192.168.12.37", 9998
data = " ".join(sys.argv[1:])

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
sock.sendto(data + "\n", (HOST, PORT))
received = sock.recv(1024)

print "Sent:     {}".format(data)
print "Received: {}".format(received)
