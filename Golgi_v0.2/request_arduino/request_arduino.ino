char c;
char str[255];
int i = 0;

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);

  Serial.println("STAND-BY");
}
 
void loop() {
  // Serial.println("Hello world!");
   
  if(Serial.available() > 0){
    c = Serial.read();
    if(c != '\n'){
      if(c == '1') digitalWrite(2, HIGH);
      else if(c == '0') digitalWrite(2, LOW);
  
      Serial.print("Arduino: ");
      Serial.println(c);
      Serial.println("STAND-BY");
    }
    
  }
   
}
