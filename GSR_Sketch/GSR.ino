
int const pin = 8;
int sensorValue = 0;
int gsr_average = 0;


void setup(){
  Serial.begin(9600);
}

void loop(){
  long sum=0;
  for(int i=0;i<10;i++)           //Average the 10 measurements to remove the glitch
      {
      sensorValue=analogRead(pin);
      sum += sensorValue;
      delay(10);
      }
   gsr_average = sum/10;
   Serial.println(gsr_average);
   Serial.flush();
   delay(100);
}
