
/*!
* @file HeartRateMonitor.ino
* @brief HeartRateMonitor.ino  Sampling and ECG output
*
*  Real-time sampling and ECG output
*
* @author linfeng(490289303@qq.com)
* @version  V1.0
* @date  2016-4-5
*/
const int heartPin = 4;
void setup() {
  Serial.begin(9600);
}
void loop() {
int heartValue = analogRead(heartPin);
Serial.println(heartValue);
delay(5);
}
