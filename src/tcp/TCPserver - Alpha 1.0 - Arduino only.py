import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = '192.168.12.25' # Get local machine name
port = 9999                # Reserve a port for your service.
 
import serial
#serial.Serial.close() 
DEVICE = '/dev/ttyACM0' # the arduino serial interface (use dmesg when connecting)
BAUD = 9600
ser = serial.Serial(DEVICE, BAUD)
 
print 'Server started!'
print 'Waiting for clients...'
 
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
   
while True:
   msg = c.recv(3) # get 3 bytes from the TCP connection
   #print msg
   ser.write(msg)  # write the 3 bytes to the serial interface
