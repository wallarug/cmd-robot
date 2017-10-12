# Joystick all regions defined #

## RELEASE NOTES ##

This installment of the Control Module Client is the first set of releases that are in the Alpha stages of development.   �Joystick ... defined� changes its name to �Control Module Beta 1.x.x� when it reaches the �Beta stage� of development within the project, this is why it �disappears� from the download site.  Below are the changes and notes for each of the four releases of this software.  The last version of �Joystick all regions defined� is the first beta version of �Control Module�.

## 1st Development Version of Joystick controller - Alpha 0.1 ##

This was the first script that was written to receive data from the joystick and then print out the translated data.  No TCP Server or Client was used in this script A basic TCP server and Client were used in this script but there were limitations as to what it could do.  It could only send �raw data� to the server and the Client was based off a text messaging TCP set-up.  Below are its features:

* Detect the users Operating System as only Windows (no other OS supported)
* Ask a single question �What do you want to detect?� (only developers would know the answer)
* Four options to the question:

* Speed 
    * Didn�t work correctly and not much work done on it. UNSTABLE

* Pos 
    * Main feature with:
    * Joystick interpretation
    * Y-axis inversion code
    * Formulas for working out motor speed
    * Send raw data to TCP server
* All 
    * printed out the three axis positions without any number manipulation
* button
    * detect if a button was pressed and then print out a command
    * e.g. If you pushed the trigger button, the expected output would be �KILL�.

* The Pulse Width Modulation Formula was present but was commented out and not active.  (also incorrect � hence why it was commented out)


## 2nd Development Version of Joystick controller - Alpha 0.3 ##

This is an upgrade from the first version but experienced issues with the TCP server due to new features added (explained below).  This version could send data to the Arduino which used 4 LEDs to show what was going on.  The LEDs acted as a substitute to the motors.

Dated: Before 26.10.12 

*Change Log*

* Added in the �def sendcommand():� to the script.  This is based off @aonsquared�s project on the Dark Pi Rises.  
    * This command broke down each part of the three pieces of data (motor_a, motor_b, dir_y) into individual bytes.
    * It uses the chr() command, which only allows integers between 0 and 256 to be sent through the TCP.
* This caused a problem, because the joystick number conversion code had a flaw on the lines: y =|x| and y = -|x|
    * Condenses a set of instructions into one command.

* Changed the TCP client to suit these new changes expressed above.  I don�t think that it was stable in this version though. UNSTABLE
* The Pulse Width Modulation formula is activated in this version. UNSTABLE
* Direction is set for Arduino as either:
    * Y = 1 for forward
    * Y = 2 for backwards
    * This allows for the Arduino coding to be easier and fewer errors can occur.

* Send Only When Active is present but is commented out due to a lack of confidence by @Ingramator. UNSTABLE
* The old TCP client is commented out but still present.
* @Ingramator�s OS detection was deleted from this version due to it slowing down development. 
* Option to send data straight to Arduino was added but could only be used through commenting and un-commenting that section and the TCP server.  NOTE: It could only be used on a single computer due to the device being registered as �COM10�.
* General Clean-up of code


## 3rd Development Version of Joystick controller - Alpha 0.4 ##

This version was highly bugged.  chr() value errors were all over this script and occurred on the |x| and -|x| lines.  It was very noticeable but took time to discover exactly where the problem was.  Basically everything is commented out while @wallarug was debugging the issue.  This code is a mess and it is suggested that it should NEVER be used again.  Nothing else was changed between this version and the previous. 

Dated: 26.10.12


## 4th Development Version of Joystick controller - Beta 1.0.1 ##

This version eradicated the chr() command issue through the total re-writing of Joystick controller code by @wallarug.  The problem that was occurring on the lines �|x| was that in a bit of the joystick control, the numbers where going through twice and then doubling each time it when through.  Here is an extract from the issue:


```
(212, 5)
(214, 3)
(214, 3)
(54570, 765)
(13915350, 195075)
(3548414250L, 49744125)
(904845633750L, 12684751875L)
(230735636606250L, 3234611728125L)
(58837587334593752L, 824825990671875L)
(15003584770321405952L, 210330627621328128L)
(3825914116431958507520L, 53634310043438669824L)
(975608099690149408931840L, 13676749061076860010496L)
(248780065420988108270206976L, 3487571010574599227179008L)
(63438916682351966681189842944L, 889330607696522753538523136L)
(16176923753999750694462851907584L, 226779304962613308749393166336L)
(214, 3)
(54570, 765)
(13915350, 195075)
(212, 5)
(212, 5)
```

As you can see above, the output doubled each time it went through the loop, meaning that the value fell outside of the range allowed by the chr() command.  This was debugged through disabling the chr() command and seeing what would happen.  As stated above, it was fixed by totally re-writing the section that converted the numbers from the joystick into a speed.
This is the last version of the script before it turned Beta and is basically version Beta1.0.1

Dated: 27.10.12 - 31.10.12


