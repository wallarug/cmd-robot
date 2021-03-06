while True:
    import sys
    import socket               # Import socket module
    s = socket.socket()         # Create a socket object
    host = '192.168.12.12'          # Get local machine name
    port = 9999                 # Reserve a port for your service.


##    import serial
##    DEVICE = '/dev/ttyACM0' # the arduino serial interface (use dmesg when connecting)
##    ##DEVICE = 'COM12'
##    BAUD = 9600
##    ser = serial.Serial(DEVICE, BAUD)
    try: 
        print "Server started on", str(host) + ":" + str(port)
        print 'Waiting for clients...'
     
        s.bind((host, port))        # Bind to the port
        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        while True:
            msg = c.recv(3) # get 3 bytes from the TCP connection
##            ser.write(msg)  # write the 3 bytes to the serial interface
            print msg
            if msg == "":
                c.shutdown(socket.SHUT_RDWR)
                c.close()
                print "Lost connection with"+ str(addr) +"! Restarting server..."
                break
    except KeyboardInterrupt:
        print "[ALERT]  Closing shell...  [ALERT]"
        c.shutdown(socket.SHUT_RDWR)
        c.close()
##        ser.close()
        sys.exit("Application forcibly halted!")
