from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime
import socket               

lcd = Adafruit_CharLCD()
lcd.begin(16,1)

s = socket.socket()         
host = '192.168.12.25'
port = 9999
 
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


def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output




while True:
   msg = c.recv(3) # get 3 bytes from the TCP connection
   #print msg
   ser.write(msg)  # write the 3 bytes to the serial interface
   lcd.clear()
   ipaddr = run_cmd(cmd)
   lcd.message('A = ' +int(motor_a) ' | B = ' +int(motor_b) '/n')
   lcd.message('IP %s' % ( ipaddr ) )
   
