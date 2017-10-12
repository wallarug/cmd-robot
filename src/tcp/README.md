# TCP servers #

## RELEASE NOTES ##

This document describes the changes that have occurred with the TCP servers within the CMD robot program.  This will discuss the changes and the issues associated with certain aspects and versions of the script.  The latest version is always going to be on the download site.  Below are the changes and notes for each of the four releases of this software.  There are two versions of the TCP server: one with only Arduino support and the other with support for both the Arduino and the 16x2 Character display.

### 1st Development Version of TCP Server - Alpha 1.0 - Arduino only: ###

This was the first script that was written to receive data from client from the Control Module and then send the data onto the Arduino using the serial command and library.  The issues that were faced in this development were:
* Would not ‘free’ up the Serial connection after use (could only use once before having to restart computer)
* Would not ‘free’ up the TCP port (could only use once before having to restart computer)

*Features*

* Receive three bytes of data then write to Arduino via ‘COM10’ or ‘dev/ttyACM0’ on the Raspberry Pi.
* Continually loop until it lost connection.

### 2nd Development Version of TCP Server - Alpha 1.1 – with Display support ###

This is the second version of the TCP server which added support for data to be send to the Arduino and the 16x2 Character Display.  It merges the Adafruit Character Display Library with the TCP server above to give us a way to see what is happening with the speed on the Display.  This did not occur correctly and lead to trial and error of different methods to do this.  Below are the some of the issues faced:

* Would not ‘free’ up the Serial connection after use (could only use once before having to restart computer)
* Would not ‘free’ up the TCP port (could only use once before having to restart computer)
* Display information could not be read due the constant refreshing of the display.  The display must be turned off and then on in order to clear the information on it.  This meant that when it was receiving data at constant bases, it would not be on at all.
* The above issue was fixed by commenting out the “lcd.clear()” command.  Then the information being printed was converted to ASCII by the chr() command, making it again impossible to get the information on the display.
* Adding to these issues, the information was combined into 3 bytes and would not be separated.


*Features*

* Same as version Alpha 1.0
* Added support for 16x2 Display.  UNSTABLE

### 3rd Development Version of TCP Server - Alpha 1.4 – with Display support ###

This was an improvement on Alpha 1.1 with support for closing TCP connection and serial connection.  The Display set-up was improved through adding in a check for different data.  It also used the Desktop Client to send individual pieces of information to the displays.  This worked fine for individually entered information but when we used the same set-up with the joystick, the display was filled with a build up of numbers, making the use of the display not a viable option.  Below are the updated features:
* Added in a “try” and “except” commands to assist in the closing of connections when the user wanted to terminate the script.
* Dashboard Client send and receive data

*Features*

* Same as version Alpha 1.0
* Added support for 16x2 Display.  UNSTABLE
