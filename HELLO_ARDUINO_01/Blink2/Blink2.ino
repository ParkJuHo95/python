
void setup() {
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
}

void loop() {
  digitalWrite(7, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(100);   
  digitalWrite(7, LOW);  // turn the LED on (HIGH is the voltage level)
  delay(100);           
  digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(100); 
  digitalWrite(8, LOW);  // turn the LED on (HIGH is the voltage level)
  delay(100); 
  // digitalWrite(7, HIGH);   // turn the LED off by making the voltage LOW
  // digitalWrite(8, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(100);      
  // digitalWrite(7, LOW);  // turn the LED on (HIGH is the voltage level)
  // digitalWrite(8, LOW);  // turn the LED on (HIGH is the voltage level)
  // delay(100); 
}
