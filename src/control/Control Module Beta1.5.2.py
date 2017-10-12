print "*************************"        #####################################
print "*Module version Beta 1.5*"        ###     #####    ##    #####       ##
print "*Standby for imports....*"        ##  ########   #    #   ####  ###  ##
print "*************************"        ##  ########  ###  ###  ####  #### ##
print "                         "        ##  ########  ###  ###  ####  ###  ##
import pygame                            ###     ####  ###  ###  ####       ##
import socket                            #####################################
import sys                               #Revision number: 1                 #
import os                                #####################################
from time import gmtime, strftime, sleep

##################
#Asset Detection!#
##################

if os.path.exists("C:\Users\Tom"):
    commander_name = "Ingram"
elif os.path.exists("C:\Users\Cian"):
    commander_name = "Byrne"
else:
    commander_name = ""


time = strftime("%H:%M:%S")
os_type = os.name
if os_type == "nt":
    os_type = "Windows"
    if os.path.exists("C:\Windows\DesktopTileResources"):
        os_name = "8"
        kernel_version = str("6.2")
    else:
        os_name = "7"
        kernel_version = str("6.1")

else:
    os_type = "OSX"
    os_name = "10.8"
    kernel_version = str("XNU") #Will make searchable if command post switches so Linux/OSX


print ("Welcome back Commander " + commander_name)
print ("You are running on " + os_type + " " + os_name + " with kernel version " + kernel_version)
print " "
print ("The current time is " + time)
print " "


##########################################
# Manual functionality specification     #
# Ingram & Byrne's idea                  #
##########################################

question_one = raw_input("Would you like to start both the TCP client and Joystick? (y/n): ")


if question_one == "y":
    question_two = "y"
    question_three = "y"
if question_one != "y":
    if question_one != "n":
        while question_one != "y" or question_one != "n":
            print "Please enter a valid value"
            question_one = raw_input("Would you like to start both the TCP client and Joystick? (y/n): ")
            if question_one == "y":
                question_two = "y"
                question_three = "y"
            elif question_one == "n":
                break
    question_two = raw_input("Would you like to enable TCP client for this sesson? (y/n): ")
    while question_two != "y" or question_two != "n":
        if question_two == "y" or "n":
            break
        print "Please enter a valid value"
        question_two = raw_input("Would you like to enable TCP client for this sesson? (y/n): ")
        if question_two == "y" or "n":
            break
    question_three = raw_input("Would you like to enable the Joystick Controller? (y/n): ")
    while question_three != "y" or question_three != "n":
        if question_three == "y" or "n":
            break
        print "Please enter a valid value"
        question_three = raw_input("Would you like to enable the Joystick Controller? (y/n): ")


############################
#Joystick Detection Script!#
############################

if question_three == "y":
    pygame.init()
    joycount = pygame.joystick.get_count()

    if joycount == 0:
        print "                                                                      "
        print "**********************************************************************"
        print "* [ WARNING ]           No joystick detected!            [ WARNING ] *"
        print "*                                                                    *"
        print "*                   Restart module with joystick!                    *"
        print "*                                                                    *"
        print "* [ WARNING ]           Module halt in TIME-5            [ WARNING ] *"
        print "**********************************************************************"
        sleep(5)
        sys.exit("No joystick found!")
    else:
        print "[ SUCCESS ] Joystick Detected! [ SUCCESS ] "    
        print " "
    j = pygame.joystick.Joystick(0)
    j.init()
     
    print 'Initialized Joystick : %s' % j.get_name()

else:
    print "Manual input method will now be activated!"
    manual_input = 1

##########################
# TCP clients are below. #
##########################

if question_two == "y":
##    HOST = raw_input("Enter IP address of the Server: ")
##    PORT = raw_input("Enter Port number of Server: ")
#print "Enter host and port separated by a comma #Future host and port assignment

    HOST, PORT = "10.0.0.1", 9999
    print "                                                                  "
    print "******************************************************************"
    print "*[ALERT]Stand by for TCP connection on " + str(HOST) + ":" + str(PORT)+" [ALERT]*"
    print "******************************************************************"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT)) #'''Added in a try command for unsucessful TCP connection'''
    except:
        print "Unable to connect to " + HOST +", please check your connection!"

    print "Connected to ", HOST, PORT

    def sendcommand(motor_a,motor_b,dir_y):
        byte1 = chr(int(motor_a))
        byte2 = chr(int(motor_b))
        byte3 = chr(int(dir_y))
        sock.send(byte1+byte2+byte3)

    motor_a_prev = 0
    motor_b_prev = 0
    dir_y_prev = 0

else:
    print "No TCP Client this sesson!"

#########################################
# The mode that you want to enter which #
#  can be one of the following:         #
#########################################
debug_value = 0
if str(question_two) == "y":
    i = raw_input("What do you want to detect? (button/pos/all)") ####@@@@####
elif str(question_two) == "n":
    debug_value = raw_input("Do you want to enter debug mode? (y/n): ")
else:
    print "Enter a correct value next time!"
    sys.exit("Value Error!")

######################################
#                                    #
#       D E B U G   M O D E          #
#                                    #
#      Advanced out of ALPHA         #
######################################
while debug_value == "n":
    print "Script conclusion, module exitting in TIME-5"
    sleep(5)
    sys.exit("End of Script")
    
while debug_value == "y":
    motor_a = input("LEFT MOTOR: Enter value between 0 and 255: ")
    motor_b = input("RIGHT MOTOR: Enter value between 0 and 255: ")
    if motor_a < 0 and motor_a > -256 or motor_b < 0 and motor_b > -256:
        dir_y = 2
        #print "Going Backwards!"
        if question_two == "y":
            sendcommand(motor_a,motor_b,dir_y)
    elif motor_a >= 0 and motor_a < 256 or motor_b >= 0 and motor_b < 256:               
        dir_y = 1
        #print "Going Forwards!"
##    if str(question_two) == "y":   ##Add question 2 check to top of loop/control structure
        if question_two == "y":
            sendcommand(motor_a,motor_b,dir_y)

    else:
        print "Number not in range, value not sent to server"
        print "Not sent to TCP Server!"
    print (motor_a, motor_b)

##################
#CUSTOM FUNCTIONS#  Currently unstable, to make usable in next update
##################

###########################################################

while i == "button":
    pygame.event.pump()
    if j.get_button(1):
        print "Left"
    if j.get_button(0):
        print "Kill"
    if j.get_button(2):
        print "Right"

###########################################################


while i == "pos":
    pygame.event.pump()
    y = j.get_axis(1)
    x = j.get_axis(0)   
    z = j.get_axis(2)   
    z = round(z,1)
    #print(x,y,z)
   
    if y < 0:          ############################
        y = abs(y)     #New Y-axes inversion code!#
    elif y > 0:        ############################
        y = y*-1

#############################################
# Formulas for working out the speed of the #
# motor in certain areas of the Joystick!   #
#############################################

    f = 1
    sy = f*(y)
    sx = f*(x)
    a = 0
    b = 0
    

#############################################
## Joystick Control Registry and Conversion!#
#############################################


    if x == 0:
        a = abs(sy)
        b = abs(sy)
    elif y > 0:
        if x > 0 and y <= x:
            a = abs(x)
            b = 0
        elif x > 0 and y > x:
            a = abs(sy)
            b = abs(sy) - abs(x)
        elif x < 0 and y <= -x:
            b = abs(x)
            a = 0
        elif x < 0 and y > -x:
            b = abs(sy)
            a = abs(sy) - abs(x)
    
    elif y == 0 and x != 0:
        if x < 0:
            a = 0
            b = abs(sx)
        elif x > 0:
            a = abs(sx)
            b = 0
    elif y < 0:
        if x > 0 and y >= -x:
            a = abs(x)
            b = 0
        elif x > 0 and y < -x:
            a = abs(sy)
            b = abs(sy) - abs(x)
        elif x < 0 and y >= x:
            a = 0
            b = abs(x)
        elif x < 0 and y < x:
            a = abs(sy) - abs(x)
            b = abs(sy)
               
               

######################################
## PWM convertion for AnalogueWrite()#
######################################

    PWM = 255
    a = PWM*a
    a = round(a, 1)
    b = PWM*b
    b = round(b, 1)

###################################
# Arduino Varibles Decleared Here!#
###################################

    motor_a = a
    motor_b = b

    if y < 0:           ##############################
        y = 2           # Direction Determinded Here!#
    else:               ##############################
        y = 1
    dir_y = y


##########################################
# Sends data ONLY when data is different!#
##########################################
    try:
        if motor_a != motor_a_prev:
            sendcommand(motor_a,motor_b,dir_y)
        elif motor_b != motor_b_prev:
            sendcommand(motor_a,motor_b,dir_y)
        elif dir_y != dir_y_prev:
            sendcommand(motor_a,motor_b,dir_y)


        motor_a_prev = motor_a
        motor_b_prev = motor_b
        dir_y_prev = dir_y
    

####################################
# Printing Output - Only used in   #
# development of Joystick Control. #
####################################

    #print (a, b)
        print (int(motor_a),int(motor_b))
    except KeyboardInterrupt:
            sock.close()
            sys.exit("Closing Application...")

#####################################################
##@@@@@@@@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@ ##
#####################################################

    

while i == "speed":
    print"currently in progress"
    x = 0.4
    y = 0.5
    f = 100
    sy = f*abs(y)
    print sy


###################################################


while i == "all":
    pygame.event.pump()
    y = j.get_axis(1)
    y = round(y,2)
    x = j.get_axis(0)
    x = round(x,2)
    z = j.get_axis(2)
    z = round(z,1)
    if j.get_button(0):
        b0 = " Kill"
    else:
        b0 = ""
    if j.get_button(1):
        b1 = " Left"
    else:
        b1 = ""
    if j.get_button(2):
        b2 = " Right"
    else:
        b2 = ""
    print(str(x) + "," + str(y) + "," + str(z) + b0 + b1 + b2)

'''CMD Official Comment ART

#####################################
###     #####    ##    #####       ##
##  ########   #    #   ####  ###  ##
##  ########  ###  ###  ####  #### ##
##  ########  ###  ###  ####  ###  ##
###     ####  ###  ###  ####       ##
#####################################
'''
