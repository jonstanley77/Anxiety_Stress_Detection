
import serial
import time
import csv

device = '/dev/ttyACM0'
baudrate = 115200 # or whatever you use

arduino_port = serial.Serial (device,
                              baudrate = baudrate,
                              parity   = serial.PARITY_NONE,
                              stopbits = serial.STOPBITS_ONE,
                              bytesize = serial.EIGHTBITS,
                              rtscts   = False,
                              dsrdtr   = False,
                              xonxoff  = False,
                              timeout  = 0)
print('reading data...')
time.sleep(3)
with open('heart_rate_data.csv', 'w', newline=' ') as file:
  while True:
    writer = csv.writer(file)
    line = arduino_port.readline ()
    writer.writerow([line])


