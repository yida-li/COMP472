from serial import Serial
import pynmea2
import time
import serial

def print_all_fields(rmc_obj):
    for i in range(len(rmc.fields)):
            print(i,rmc.fields[i][0],rmc.data[i])

ser= serial.Serial('/dev/ttyACM0', 115200, timeout = 0.2)

while True:
    line = ser.readline()
    line= str(line, encoding='utf-8')

    if line.startswith('$GPGGA'):
        rmc= pynmea2.parse(line)
        print_all_fields(rmc)
        print(rmc)
    if line.startswith('$GPRMC'): # GPVTG GPGSA GPGLAA
        rmc= pynmea2.parse(line)
        print(rmc)
        print_all_fields(rmc)

