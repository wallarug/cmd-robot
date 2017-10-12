print "*************************"        ###########################################
print "*Module version Beta 1.6*"        #     #####     ##    ##      #####       #
print "*Standby for imports....*"        #   ####      #    ##    #     ####  ###  #
print "*************************"        #   ##       ###  ####  ###    ####  #### #
print "                         "        #   ###      ###  ####  ###    ####  ###  #
import pygame                            #     #####  ###  ####  ###    ####       #
import socket                            ###########################################
import sys                               #Revision number: 2                       # 
import os                                ###########################################
from time import gmtime, strftime, sleep
from pygame.locals import *

##########################################
# All Variables used in script being     #
#  set to zero so that it is recognised  #
#   by the except statements.            #
##########################################

init = 0            #
question_one = 0
question_two = 0    #
question_three = 0
network_one = 0
network_two = 0
network_value = 0
motor_a =0
motor_b = 0
a = 0               #
b = 0               #
x = 0
y = 0
manual_input = 0
debug_value = 0     #
i = 0
motor_a_prev = 0    #
motor_b_prev = 0    #
dir_y_prev = 0      #
servo_prev = 0      #
dir_y = 0
connection = 0
robot_detection = 0 #
servo = 90

#################################
# Pygame Mixer / Music Modules! #
#################################

pygame.mixer.init()
pygame.mixer.music.load('WELCOME BACK.wav')  #NOTE: one must have the sound file to make this work.
pygame.mixer.music.play()

############################
# Declearing sendcommmand. #
############################

# This is for sending all values onto the TCP Server.

def sendcommand(): # took out servo, motor_a,motor_b,dir_y
    byte1 = chr(int(motor_a))
    byte2 = chr(int(motor_b))
    byte3 = chr(int(dir_y))
##    byte4 = chr(int(servo))
    sock.send(byte1+byte2+byte3) # took out byte4

##################
#Asset Detection!#
##################

# Checks whose computer is being used.  These directories were manually made.
#  No users called Cian or Tom, just an empty folder.

if os.path.exists("C:\Users\Tom"):
    commander_name = "Ingram"
elif os.path.exists("C:\Users\Cian"):
    commander_name = "Byrne"
else:
    commander_name = ""

# Gets the time.
time = strftime("%H:%M:%S")

# Checks what OS one is using and then works out which version.

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

#############################
#  DIALOGUE OUTPUT ON START #
#############################

print ("Welcome back Commander " + commander_name)
print ("You are running on " + os_type + " " + os_name + " with kernel version " + kernel_version)
print " "
print ("The current time is " + time)
print " "


##########################################
# Manual functionality specification     #
# Ingram & Byrne's idea                  #
##########################################

# This section askes the user a series of questions before deciding which robot to use.
#  This takes a while.

try:
    robot_detection = raw_input("Which Robot do you wish to control? (overwatch = '1' / recon = '2' / butterfly = '3'): ")
    
    while robot_detection != '1' or robot_detection != '2' or robot_detection == '3':
        if robot_detection == '3':
            print 'Support for CMDbutterfly will be coming in a later release.  Please select another option from the ones provided. '
        elif robot_detection == '1' or robot_detection == '2' or robot_detection == '50':
            break
        else:
            print 'Enter a valid value! '
        robot_detection = raw_input("Which Robot do you wish to control? (overwatch = '1' / recon = '2' / butterfly = '3'): ")
        
        
    if robot_detection == '1':
        robot_detection = 'CMDoverwatch'
    elif robot_detection == '2':
        robot_detection = 'CMDrecon'
    elif robot_detection == '50':
        robot_detection = 'home'
    
    print " "
    print  "Controlling " +robot_detection
    print " "
    question_one = raw_input("Would you like to use Default Settings? (y/n): ")   
    if question_one == "y":
        question_two = "y"
        question_three = "y"
        network_value = "y"
        #debug_value = "y"
        i = "pos"

    if question_one != "y":
        network_value = "n"
        if question_one != "n":
            while question_one != "y" and question_one != "n":
                print "Please enter a valid value"
                question_one = raw_input("Would you like to start both the TCP client and Joystick? (y/n): ")
                if question_one == "y":
                    question_two = "y"
                    question_three = "y"
                elif question_one == "n":
                    break
        question_two = raw_input("Would you like to enable TCP client for this sesson? (y/n): ")

        while question_two != "y" and question_two != "n":
            if question_two == "y" or question_two == "n":
                break
            print "Please enter a valid value"
            question_two = raw_input("Would you like to enable TCP client for this sesson? (y/n): ")

        question_three = raw_input("Would you like to enable the Joystick Controller? (y/n): ")
        while question_three != "y" and question_three != "n":
            if question_three == "y" or question_three == "n":
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
            print " "
            print "[ SUCCESS ] Joystick Detected! [ SUCCESS ] "    
        j = pygame.joystick.Joystick(0)
        j.init()
        print " "
        print " ************************************************ " 
        print ' * Initialized Joystick : %s' % j.get_name() + " * "
        print " ************************************************ "
    else:
        print "                                                                          "
        print "**************************************************************************"
        print "*                                                                        *"
        print "* [ WARNING ]  Manual input method will now be activated!  [ WARNING ]   *" 
        print "*                                                                        *"
        print "**************************************************************************"
        manual_input = 1



    #########################
    # TCP client is  below. #
    #########################

    ######################################
    # Check for TCP connection settings. #
    ######################################

    while question_two == "y":
        if network_value == "n":
            print " "
            print " "
            network_one = raw_input("Would you like to use a pre-set IP address? ('n' or 'adhoc'/'local') : ")
            while network_one != "n" and network_one != "adhoc" and network_one != "local":
                print "Please enter a valid value"
                network_one = raw_input("Would you like to use a pre-set IP address? ('n' or 'adhoc'/'local') : ")
                if network_one == "n" or network_one == "adhoc" or network_one == "local":
                     break
            if network_one == "adhoc":
                HOST, PORT = "192.168.12.37", 8999
                sockname = robot_detection
            elif network_one == "local":
                HOST, PORT = 'localhost', 9999
                sockname = str(socket.gethostname())
            elif network_one == "n":
                HOST = raw_input("Enter the Desired IP Address. (FORMAT: e.g. 192.168.12.1): ")
                PORT = input("Enter the Desired Port number. (FORMAT: e.g. 9999): ")
                sockname = robot_detection
        elif network_value == "y":
            if robot_detection == 'CMDoverwatch':
                HOST, PORT = "10.0.0.1", 8999
                sockname = "CMDoverwatch"
            elif robot_detection == 'CMDrecon':
                HOST, PORT = "10.0.0.50", 9999
                sockname = "CMDrecon"
            elif robot_detection == 'home':
                HOST, PORT = "192.168.12.37", 8999
                sockname = "HOME DEVICE!"

        connection = 0
        connection_attempt = 1
        con_attempted = 0
        while connection == 0:
            print " "
            print "[ ALERT ]  Stand by for TCP connection on " + str(HOST) + ":" + str(PORT)+ "!  Attempt: " + str(connection_attempt) + "  [ ALERT ]"
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sock.connect((HOST, PORT)) #'''Added in a try command for unsucessful TCP connection'''
                print " "
                print "[ ALERT ]   Connected to " +str(sockname)+" @ "+ str(HOST) + ":" + str(PORT)+"  [ ALERT ]   "
                connection = 1
            
            except:
                #print " "
                print "[ ALERT ]  Unable to connect to " + HOST +", please check your connection!   [ ALERT ]"
                connection_attempt = connection_attempt + 1
                sleep(5)
                if connection_attempt > 2 and con_attempted == 0:
                    print " "
                    con_attempt = raw_input("Are you sure " + str(HOST) + ":" + str(PORT) + " is your desired address? (y/n)")
                    con_attempted = 1
                    while con_attempt != "y" and con_attempt != "n":
                        print "Please input a valid value!"
                        con_attempt = raw_input("Are you sure " + str(HOST) + ":" + str(PORT) + " is your desired address? (y/n)")
                        
                    if con_attempt == "n":
                        HOST = raw_input("Enter the Desired IP Address. (FORMAT: e.g. '192.168.12.1'): ")
                        PORT = input("Enter the Desired Port number. (FORMAT: e.g. 9999): ")
                        
                    
                if connection_attempt > 5:
                    print "[ WARNING ]  Connection attempts have failed, the script will now exit!  [ WARNING ] "
                    sleep(3)
                    sys.exit("Connection Failed!")
        break #Discovered flaw, once completed that section would continue the while loop!

    else:
        print " "
        print "[ WARNING ]  No TCP Client this sesson!  [ WARNING ] "
except KeyboardInterrupt:
        if question_two == "y":
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        sys.exit("Closing Application...")


#########################################
# The mode that you want to enter which #
#  can be one of the following:         #
#########################################

try:
    if question_one != "y":
        if str(question_three) == "y":
            print " "
            i = raw_input("What do you want to detect? (button/pos/all): ")
        elif str(question_three) == "n":
            print " "
            debug_value = raw_input("Do you want to enter debug mode? (y/n): ")
        else:
            print "Enter a correct value next time!"
            sys.exit("Value Error!")
except KeyboardInterrupt:
        if question_two == "y":
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        sys.exit("Closing Application...")


######################################
#                                    #
#       D E B U G   M O D E          #
#                                    #
#      Advanced out of ALPHA         #
######################################

#  Not used very offen / at all.
try:
    if debug_value == "n":
        print " Loading WASD Full Speed Control..."
        pygame.init()
        screen = pygame.display.set_mode((64, 64))
        pygame.display.set_caption('WASD Control of CMD-ROBOT')
        pygame.mouse.set_visible(0)
        done = False
        while not done:
           for event in pygame.event.get():
                if (event.type == KEYUP):
                    if (event.key == K_a):
                        print "Moving Left!"
                        motor_b = 255
                        motor_a = 0
                        dir_y = 1
                        servo = 90
                    elif (event.key == K_s):
                        print "Moving Backwards!"
                        dir_y = 2
                        motor_a = 255
                        motor_b = 255
                        servo = 90
                    elif (event.key == K_d):
                        print "Moving Right!"
                        dir_y = 1
                        motor_b = 0
                        motor_a = 255
                        servo = 90
                    elif (event.key == K_w):
                        print "Moving Forwards!"
                        dir_y = 1
                        motor_a = 255
                        motor_b = 255
                        servo = 90
                    elif (event.key == K_ESCAPE):
                        done = True
                    else:
                        motor_a = 0
                        motor_b = 0                
                    if question_two == "y":
                        sendcommand()
                    print (motor_a,motor_b)
except KeyboardInterrupt:
        if question_two == "y":
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        sys.exit("Closing Application...")

try:    
    if debug_value == "y":
        print " "
        print "Welcome to Debug mode for CMD robots...Use with caution!!! "
        print "Loading... "
        sleep(3)
        print " "
        print "[ ALERT ]  Script Loaded Successfully!  [ ALERT ]  "
        print " "
        print " ******************* "
        print " * BEGIN DEBUGGING * "
        print " ******************* "
        while True:
            print " "
            motor_a = input("LEFT MOTOR: Enter value between -255 and 255: ")
            motor_b = input("RIGHT MOTOR: Enter value between -255 and 255: ")
            if motor_a < 0 and motor_a > -256 or motor_b < 0 and motor_b > -256:
                dir_y = 2
##                motor_a = 255 - abs(motor_a)
                motor_a = abs(motor_a)
##                motor_b = 255 - abs(motor_b)
                motor_b = abs(motor_b)
                print "Going Backwards!"
                if question_two == "y":
                    sendcommand()
                    print "Sent to server!"
            elif motor_a >= 0 and motor_a < 256 or motor_b >= 0 and motor_b < 256:               
                dir_y = 1
                motor_a = abs(motor_a)
                motor_b = abs(motor_b)
                print "Going Forwards!"
                if question_two == "y":
                    sendcommand()
                    print "Sent to server!"
            elif motor_a == "" or motor_b == "": # Will work once we change input to raw_input otherwise we get an error!
                motor_a = 0
                motor_b = 0
                dir_y = 1
                if question_two == "y":
                    sendcommand()
                    print "Reset values command sent to server!"
            else:
                print "Number not in range, value not sent to server"
                print "Not sent to TCP Server!"
            print (motor_a, motor_b)
except KeyboardInterrupt:
        if question_two == "y":
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        sys.exit("Closing Application...")





#########################################################
#  MAIN CLIENT SCRIPT TO CONTROL ROBOTS WITH JOYSTICK.  #
#########################################################

try:
    while i == "pos":
        if question_two == "y":
            sockname = str(sockname)
        else:
            sockname = "nothing"
        init = 1
        if init == 0:
            print " "
            print "[ WARNING ]  Initiating Control of " + str(sockname) + " in...  [ WARNING ] "
            print " "
            print " ************************************* "
            print " "
            print " * Initiated Control of " + str(sockname) + "!"
            print " "
            print " ************************************* "
            init = init + 1
            sleep (1.5)


        pygame.event.pump()
        x = j.get_axis(0)
        x = round(x,4)
        y = j.get_axis(1)
        y = round(y,4)
        z = j.get_axis(2)   
        z = round(z,1)
        #print(x,y,z)
       
        if y < 0:               ############################
            y = abs(y)          #New Y-axes inversion code!#
        elif y > 0:             ############################
            y = y*-1
            
    #############################################
    # Formulas for working out the speed of the #
    # motor in certain areas of the Joystick!   #
    #############################################

        f = 1
        sy = f*(y)
        sx = f*(x)
        

    #############################################
    ## Joystick Control Registry and Conversion!#
    #############################################

        #if j.get_button(0):
        #if j.get_name() != 'wide':
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
        #if j.get_name() == 'wide':
            #a = x
            #b = x
        else:
            a = 0
            b = 0
               

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

    ####################################
    # NEW: Single PWM Channel LOW fix! #
    ####################################
        if robot_detection == 'CMDoverwatch' or robot_detection == 'home':
            if y < 0:           
                y = 2                # Backwards
            else:               
                y = 1                # Forewards
            dir_y = y
        elif robot_detection == 'CMDrecon':
            if y < 0:           
                y = 2                # Backwards
                motor_a = 255 - abs(motor_a)
                motor_a = abs(motor_a)
                motor_b = 255 - abs(motor_b)
                motor_b = abs(motor_b)
            else:               
                y = 1                # Forewards
            dir_y = y
    ###############################
    #  NEW: Servo Control Script! #
    ###############################

    # Commented due to fire started.
    
    ##        servo_control = 45*abs(x)
    ##    
    ##        if x > 0:
    ##            servo = 90 + servo_control
    ##        elif x < 0:
    ##            servo = 90 - servo_control
    ##        else:
    ##            servo = 90
    ##        servo = round(servo, 0)


    ##########################################
    # Sends data ONLY when data is different!#
    ##########################################

        if question_two == "y":
            if motor_a != motor_a_prev:
                sendcommand()
            elif motor_b != motor_b_prev:
                sendcommand()
            elif dir_y != dir_y_prev:
                sendcommand()
    ##            elif servo != servo_prev:
    ##                sendcommand()


            motor_a_prev = motor_a
            motor_b_prev = motor_b
            dir_y_prev = dir_y
    ##            servo_prev = servo


    ####################################
    # Printing Output - Only used in   #
    # development of Joystick Control. #
    ####################################
    
        print (int(a),int(b)) # Comment this line for no speed output.
    
except KeyboardInterrupt:
    if question_two == "y":
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
    sys.exit("Closing Application...")

#####################################################
##@@@@@@@@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@ ##
#####################################################

    
##################
#CUSTOM FUNCTIONS#  Currently unstable, to make usable in coming updates
##################


while i == "button":
    pygame.event.pump()
    if j.get_button(1):
        print "Left"
    if j.get_button(0):
        print "Kill"
    if j.get_button(2):
        print "Right"

###################################################

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
###     #####    ##    #####      ###
##  ########   #    #   ####  ###  ##
##  ########  ###  ###  ####  #### ##
##  ########  ###  ###  ####  ###  ##
###     ####  ###  ###  ####      ###
#####################################
'''
endstatement = raw_input("You have reached the end of the script! (exit/ *) ")
if endstatement == "exit":
    sys.exit("End of script!")
