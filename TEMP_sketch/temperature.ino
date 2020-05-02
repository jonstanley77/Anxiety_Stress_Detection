int sensorPin = A12;

void setup()
{
  Serial.begin(9600);
  pinMode(sensorPin, INPUT);
}

void loop()
{
  int reading = analogRead(sensorPin);
  float voltage = reading * (5000 / 1024); //5000mV supplied by USB
  float tempC = (voltage - 500)/10;

  float tempF = (tempC * 9 / 5) + 32;
  Serial.println(tempF);
  delay(1000);
}
