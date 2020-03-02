
import serial
import time

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
while True:
  line = arduino_port.readline ()
  print(line)