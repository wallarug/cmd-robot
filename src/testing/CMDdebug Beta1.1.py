import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
print("Welcome to CMDdebug module")
i=input("Please enter the pin you would like to test!")
try
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
except KeyboardInterrupt
    GPIO.cleanup()
    


'''Ingramator's code bitches'''
