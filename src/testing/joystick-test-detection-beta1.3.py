print "Module loading..."
import pygame
import socket
import math
import sys
from os import name
from time import gmtime, strftime, sleep
time = strftime("%H:%M:%S")
os = name
if os == "nt":
    os = "Windows"
else:
    os = "Linux/OSX"

print ("Welcome back commander, you are running on " + os)
print ("The current time is " + time)

pygame.init()
joycount = pygame.joystick.get_count()
attempt = 1

while True:
    if joycount == 1:
        j = pygame.joystick.Joystick(0)
        j.init()
        break
    elif joycount != 1 and attempt <= 4:
        print "No joysticks detected, please connect before continuing! Attempt: " + str(attempt)
    elif attempt > 4:
        print "No joystick detected, exiting program in 2 seconds!"
        sleep(2)
        sys.exit("No joystick found!")
    
    attempt = attempt +1
    sleep(3)
    joycount = pygame.joystick.get_count()
    
 
print 'Initialized Joystick : %s' % j.get_name()

sleep(3)
print "Closing Script..."
