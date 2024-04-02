#include <Servo.h>

String inputString = "";
bool stringComplete = false;
Servo bottom;
Servo arm1;
Servo arm2;
Servo grip;

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);

  bottom.attach(8);
  arm1.attach(9);
  arm2.attach(10);
  grip.attach(11);

  bottom.write(100);
  arm1.write(100);
  arm2.write(100);
  grip.write(100);

  
}

void loop() {
   if (stringComplete) {
    Serial.println(inputString);
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == 'a') {
      stringComplete = true;
      arm2.write(60);
    }
    if (inChar == 'b') {
      stringComplete = true;
      arm2.write(130);
    }
  }
}
