import socket

########################
# TCP client is below. #
########################
##
##HOST, PORT = "localhost", 9999
##sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##sock.connect((HOST, PORT))
##print "Connected to ", HOST, PORT


h, p = "localhost", 8883
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect((h, p))
print "2nd Client Connect to ", h, p
byte1 = input("Enter 1st value: ")
byte2 = input("Enter 2nd value: ")


def send2screen(motor_a,motor_b):
##    byte4 = str(int(motor_a))
##    byte5 = str(int(motor_b))
    sock2.send(str(byte1)) #First lot of data
    sock2.send(str(byte2)) #Second lot of data

try:
    send2screen(byte1,byte2)
except KeyboardInterrupt:
    sock2.close()
##            sys.exit("Closing Application...")


