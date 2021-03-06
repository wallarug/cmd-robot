/*
 * Robot Motor Controller script with PWM speed control - Duel Channel
 *   Control with support for 'Pivot'
 *
 *  By Cian Byrne
 *   CMD Enterprises 2013
 *
 * WARNING: ONLY USE THIS SCRIPT WITH CMDrecon!!
 */
//---------------------- variables
int motorL[] = {3, 5};
int motorR[] = {11, 6};
int ledPin = 13;
int Byte1 = 0;  //for incoming serial data
int Byte2 = 0;  //for incoming serial data
int Byte3 = 0;  //for incoming serial data
int motor_a = 0;
int motor_b = 0;
int dir_y = 0;


void setup() {
Serial.begin(9600);  // opens serial port, sets data rate at 9600bps
int i;
for(i = 0; i < 2; i++){
pinMode(motorL[i], OUTPUT);
pinMode(motorR[i], OUTPUT);
pinMode(ledPin, OUTPUT);
}

}

void loop() {
digitalWrite(ledPin, HIGH);

if(Serial.available()==3)
{
  Byte1 = Serial.read(); // Incoming data from Serial connection
  motor_a = int(Byte1);
  Byte2 = Serial.read(); // Incoming data from Serial connection
  motor_b = int(Byte2);
  Byte3 = Serial.read(); // Incoming data from Serial connection
  dir_y = int(Byte3);
  
  if (dir_y == 1) {  //Motor Forwards and Single motor Turning
  analogWrite(5, motor_a);
  analogWrite(6, motor_b);
  }
  else if (dir_y == 2) { //Motor Backwards
  analogWrite(3, motor_a);
  analogWrite(11, motor_b);
  }
  else if (dir_y == 3){ //Pivot Right
  analogWrite(3, motor_a);
  analogWrite(6, motor_b);
  }
  else if (dir_y == 4){ //Pivot Right
  analogWrite(5, motor_a);
  analogWrite(11, motor_b);
}
}
}
