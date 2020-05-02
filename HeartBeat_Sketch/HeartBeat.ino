//Definitions  
const int HR_RX = 13;
byte oldSample, sample;
unsigned long newTime, oldTime = millis();

void setup() {
  Serial.begin(9600);
  pinMode (HR_RX, INPUT);  //Signal pin to input  
  //Wait until a heart beat is detected  
  while (!digitalRead(HR_RX)) {};
  
}

void loop() {
  int bpm;
  
  sample = digitalRead(HR_RX);  //Store signal output 
  if (sample && (oldSample != sample)) {
    newTime = millis();
    bpm = 60000 / abs(newTime - oldTime);
    Serial.println(bpm);
    
    oldTime = newTime;
  }
  
  oldSample = sample;           //Store last signal received 

}
  
