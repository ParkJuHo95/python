
String inputString = ""; 
bool stringComplete = false;

void setup() {c:\workspace_python\HELLO_ARDUINO_02\SerialEvent2\SerialEvent2.ino
  Serial.begin(9600);
  inputString.reserve(200);
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
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
