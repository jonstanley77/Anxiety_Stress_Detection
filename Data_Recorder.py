#run with C:\Python34\py.exe serial_test.py

import sys
import serial
import time

start = time.time()
duration = 20 #specify how long you would like the code the run

print("modules start")
print(serial.__file__)
print("modules end")

data_type = input("what data is this? :") #specify what csv file you are saving to 

try:
    # open the serial port, you will have to change this line; only do this once as most arduinos reset when the serial port is opened
    ser = serial.Serial('/dev/ttyACM0', baudrate=9600) #baudrate must match the one in your arduino IDE
    # e.g. remove remains of Arduino bootloader or old data while the application was not running
    # not sure yet if it's 100% reliable; robin's approach is probably safer
    ser.flushInput()

    while time.time() < start + duration:
        # check if bytes received
        numBytes = ser.inWaiting()
        if(numBytes > 0):
            serBytes = ser.readline()
            print(serBytes)
            # open file for binary (!) appending; not using binary results in
            # 1) error telling you 'must be str, not bytes'
            # 2) convering using str(ser_bytes) results in unwanted quotation marks in the file (as shown in the result of above print)
            file = open(data_type+'.csv', 'ab')
            file.write(serBytes
)           file.close()

    # close serial port
    ser.close
except:
    print("Unexpected error:", sys.exc_info()[0])
    print("Unexpected error:", sys.exc_info()[1])

    # maybe todo: close serial port; this might need a little rework of above code moving 'ser = serial.Serial('COM4', baudrate=57600)' to outside the try