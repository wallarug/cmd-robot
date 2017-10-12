# Converting Joystick Position to a Percentage that the PWM
# Channel can simluate on the motors
# By Wallarug
# Change the input value "i" to something that relates to the Joystick

f = float(100)/float(255)
i = input("Enter a number between -255 and +255: ")

while i!="":
    x = float(f)*int(i)
    print "PWM, " + str(x) + "%"
    i = input("Enter a number between -255 and +255: ")

# By Wallarug
