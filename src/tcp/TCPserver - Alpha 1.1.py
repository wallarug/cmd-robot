from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime            
import socket
import sys
import binascii


lcd = Adafruit_CharLCD()
lcd.begin(16,1)
asc = binascii
cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

s = socket.socket()         
host = '192.168.12.37'
port = 8888
a = 0
b = 0
motor_a = 0
motor_b = 0
try: 
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
                data = c.recv(3) # get 3 bytes from the TCP connection
                data2 = c.recv(3)
##                motor_b = byte5
##                motor_a = byte4
##                a = int(a)
##                motor_b = b
##                b = int(b)
                print (data, data2)
##           #print msg
##           lcd.clear()
##           ipaddr = run_cmd(cmd)
##           lcd.message('A = ' +a + ' | B = ' +a + '/n')
##           lcd.message('IP %s' % ( ipaddr ) )   
except KeyboardInterrupt:
   print "Closing shell..."
   s.close()
   sys.exit("Closing Application...")
