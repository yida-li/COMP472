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

    #if line.startswith('$GPGGA'):
    #    rmc= pynmea2.parse(line)
    #    print_all_fields(rmc)
    #if line.startswith('$GPVTG'):
    #    rmc= pynmea2.parse(line)
    #    print_all_fields(rmc)
    #if line.startswith('$GPGSA'):
    #    rmc= pynmea2.parse(line)
    #    print_all_fields(rmc)
    #if line.startswith('$GPGLAA'):
    #    rmc= pynmea2.parse(line)
    #    print_all_fields(rmc)
    if line.startswith('$GPRMC'):
        rmc= pynmea2.parse(line)
        print("latitude:",rmc.latitude)
        print("longitude:",rmc.longitude)
        # print_all_fields(rmc) other parameters available
