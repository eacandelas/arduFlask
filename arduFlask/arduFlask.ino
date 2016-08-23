void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(500);

}

void loop() {
  // put your main code here, to run repeatedly:
  if( Serial.available()>0){
    char c = Serial.read();
    if (c == 'a'){
      int val = analogRead(0);
      Serial.println(val);
    }
  }

}
