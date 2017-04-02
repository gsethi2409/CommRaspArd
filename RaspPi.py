import serial   //for Serial communication between the Arduino and Pi.
import time     //for delay
while True:
    choice = input("Would you like to change the value of 'n' (y/n)?")
    if choice == 'y':
        ArduinoPort = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5")    //open port
        while True:
            ArduinoPort.write(n);   //send value
    time.sleep(60)
