
import serial
import time
import csv
import os.path

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

filename = 'heart_rate_data.csv'


if not (os.path.isfile(filename)):    

  print("Making new file... ")

  with open('heart_rate_data.csv', 'w', newline='') as file:
    x = 0
    writer = csv.writer(file)

    while x < 5:
      x += 1 
      line = arduino_port.readline()
      writer.writerow([line])

  print("done")

else:

  print("Adding to existing file... ")
  with open('heart_rate_data.csv', 'a+', newline='') as file:
    x = 0
    writer = csv.writer(file)

    while x < 5:
      x += 1 
      line = arduino_port.readline()
      writer.writerow([line])

    print("done")