
void setup() {
  pinMode(7, OUTPUT);
}

void loop() {
  digitalWrite(7, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(3000);                      // wait for a second
  digitalWrite(7, LOW);   // turn the LED off by making the voltage LOW
  delay(3000);                      // wait for a second
}
