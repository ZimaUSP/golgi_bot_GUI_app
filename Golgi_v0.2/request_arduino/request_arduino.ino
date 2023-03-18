char c;
char str[255];
int i = 0;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);

  Serial.println("STAND-BY");
}
 
void loop() {
  // Serial.println("Hello world!");
   
  if(Serial.available() > 0){
    c = Serial.read();

    if(c != '\n'){
        str[i++] = c;
    } else {
      str[i] = '\0';
      i = 0;

      Serial.print("Arduino: ");
      Serial.println(str);
      Serial.println("STAND-BY");
    }
    
  }
   
}