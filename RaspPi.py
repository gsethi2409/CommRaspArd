import serial
import time
while True:
    choice = input("Would you like to change the value of 'n' (y/n)?")
    if choice == 'y':
        ArduinoPort = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5")
        while True:
            ArduinoPort.write(n);
    time.sleep(60)