
int a = 10;
  int b = 9;
  int c = 8;
  int enable = 2;
  
void setup() {
  // put your setup code here, to run onc
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);  
  pinMode(c, OUTPUT);
  pinMode(enable, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(a, HIGH);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(b, LOW);
  digitalWrite(c, HIGH);
  digitalWrite(enable, HIGH);
  delay(1000); 
}
