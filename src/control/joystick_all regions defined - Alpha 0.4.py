import pygame
import socket
import math
#import sys
#import os
##import serial
##
##DEVICE = 'COM10'
##BAUD = 9600
##ser = serial.Serial(DEVICE, BAUD)


pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
 
print 'Initialized Joystick : %s' % j.get_name()

########################
# TCP client is below. #
########################

##HOST, PORT = "192.168.12.12", 9999
##sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##sock.connect((HOST, PORT))
##print "Connected to ", HOST, PORT
##
##
##
##def sendcommand(motor_a,motor_b,dir_y):
##    byte1 = chr(int(motor_a))
##    byte2 = chr(int(motor_b))
##    byte3 = chr(int(dir_y))
##    sock.send(byte1+byte2+byte3)
##
##motor_a_prev = 0
##motor_b_prev = 0
##dir_y_prev = 0

###########################################################


i = raw_input("What do you want to detect?")
while i == "button":
    pygame.event.pump()
    if j.get_button(1):
        print "Left"
    if j.get_button(0):
        print "Kill"
    if j.get_button(2):
        print "Right"
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
## Whenever the ROBOT is moving and the     #
##  Co-ordinates are not (0,0)              #
#############################################

##    if y == -x or y == x:               ############################################################
##        a = 0                           # When it cross the line |x| or -|x|.  Solution to problem.#
##        b = 0                           ############################################################  
        
    if x != 0 and y != 0:       
        sy = abs(sy)                    #######
        if y > abs(x):        # Top!#
                                        ############
            if -1 < x < 0:              # Top Left!#
                                        #############################
                c = abs(x)              # Convert to positive value!#
                a = (sy) - (c)          #############################
                b = (sy)
                                        #############
            elif 0 < x < 1:             # Top Right!#
                                        #############################
                d = abs(x)              # Convert to positive value!#
                b = (sy) - (d)          #############################
                a = (sy)
                                        ##########
        elif y < -abs(x):     # Bottom!#
                                        ###############
            if -1 < x < 0:              # Bottom Left!#
                                        #############################
                c = abs(x)              # Convert to positive value!#
                a = (sy) - (c)          #############################
                b = (sy)
                                        ################
            elif 0 < x < 1:             # Bottom Right!#
                                        #############################
                d = abs(x)              # Convert to positive value!#
                b = (sy) - (d)          #############################
                a = (sy)
##            else:                       ############################################
##                a = abs(sy)             # So that values "a" and "b" are regonised #
##                b = abs(sy)             #  by python reader (I had problems)!      #
                                        ############################################



#################################
# Special formula for when you  #
#   leave the "allowed" area    #
#################################

    elif y <= abs(x) and y >= -abs(x):  
        if x < 0:
            b = abs(x)
            a = 0
        elif x > 0:
            a = abs(x)
            b = 0
        


##################################
# Special Formula for all values #
#  on the x-axis for immediate   #
#    turning.                    #
##################################

    elif y == 0:
        if x < 0:
            a = 0
            b = abs(sx)
        elif x > 0:
            a = abs(sx)
            b = 0


#######################################
#  Anything else that is not defined  #
#   (Only when x and y = 0)           #
#######################################

    elif x == 0:
        a = abs(sy)
        b = abs(sy)

##    else:
##        a = 0
##        b = 0
        
               

######################################
## PWM convertion for AnalogueWrite()#
######################################

##    if 0 > str(a) >= 1 or 0 > str(b) >= 1:
##        a = 0
##        b = 0
##    else:
    PWM = 255
    a = PWM*a
    a = round(a, 1)
    b = PWM*b
    b = round(b, 1)

###################################
# Arduino Varibles Decleared Here!#
###################################

##    motor_a = a
##    motor_b = b
##
##    if y < 0:           ##############################
##        y = 2           # Direction Determinded Here!#
##    else:               ##############################
##        y = 1
##    dir_y = y


##########################################
# Sends data ONLY when data is different!#
##########################################

##    if motor_a != motor_a_prev:
##        sendcommand(motor_a,motor_b,dir_y)
##    elif motor_b != motor_b_prev:
##        sendcommand(motor_a,motor_b,dir_y)
##    elif dir_y != dir_y_prev:
##        sendcommand(motor_a,motor_b,dir_y)
##
##    motor_a_prev = motor_a
##    motor_b_prev = motor_b
##    dir_y_prev = dir_y


####################################
# Printing Output - Only used in   #
# development of Joystick Control. #
####################################

    print (a, b)
    #print (int(motor_a),int(motor_b))


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
########
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
