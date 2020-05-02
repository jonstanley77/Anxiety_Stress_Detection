# Anxiety_Stress_Detection
Independent Study for Stress and Anxiety Detection and Mitigation
This repo includes several files to conduct a study for collecting data for Stress and Anxiety Detection

#Sketches

All of the sketches run in the Arudino IDE

##HeartBeat

Detects heart rate in BPS with Polar T34 heart rate band, this is wireless and connect to a sensor on the board

##ECG

Records the electrical signal from your heart, connects to Gravity Heart Rate Monitor 

##TEMP

Detects ambient skin temperature, connects to Lilypad Temperature Sensor, Fahrenheit values can be easily converted to Celsius

##GSR

Detects galvanic skin response which is the electrical resistance of the skin, connects to Grove GSR v1.0 Sensor

#Data_Recorder

Python script used to record data values from each sketch and save to a CSV file 

1. Make sure serial monitor in Arduino is closed and run script in Terminal with Python3 "python3 Data_Recorder.py"

2. Enter the name of the CSV file you would like to save to

3. Script will run for X specified seconds 

4. Once finished it will save the CSV file to the local repository 
