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
    String str = Serial.readString();
    str.trim();
//    if(c != '\n'){
//      str[i++] = c;
//    } else {
//      str[i] = '\0';  
//      i = 0;
    if(str == "600") digitalWrite(2, HIGH);
    else if(str == "700") digitalWrite(2, LOW);

    Serial.print("Arduino: ");
    Serial.println(str);
    Serial.println("STAND-BY");
    
    
    
  }
    
}
