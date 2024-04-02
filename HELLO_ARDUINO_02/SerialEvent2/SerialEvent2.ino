
String inputString = "";
bool stringComplete = false;

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);
  pinMode(13, OUTPUT);
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
      digitalWrite(13, HIGH);
    }
    if (inChar == 'b') {
      stringComplete = true;
      digitalWrite(13, LOW);
    }
  }
}
