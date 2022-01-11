from serial import Serial
import pynmea2
import time
import serial
import csv

def print_all_fields(rmc_obj):
    for i in range(len(rmc.fields)):
            print(i, rmc.fields[i][0], rmc.data[i])
counter=0
ser = serial.Serial('/dev/ttyACM0', 115200,timeout =6.2)
x0 = 'Timestamp' 
x1 = 'Status V'
x2 = 'Latitude' 
x3 = 'Latitude Direction' 
x4 = 'Longitude' 
x5 = 'Longitude Direction' 
x6 = 'Speed Over Ground' 
x7 = 'True Course' 
x8 = 'Datestamp'
x9 = 'Magnetic Variation' 
x10 = 'Magnetic Variation Direction' 
with open('GPRMC.csv','w',encoding='UTF8',newline='') as f:



    fieldnames=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    writer= csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    while counter<700:
        line = ser.readline()
        line = str(line,encoding='utf-8')
        if line.startswith('$GPRMC'):
            print(counter)        
            rmc= pynmea2.parse(line)
            writer.writerow({x0:rmc.data[0],x1:rmc.data[1],x2:rmc.data[2],x3:rmc.data[3],x4:rmc.data[4],x5:rmc.data[5],x6:rmc.data[6],x7:rmc.data[7],x8:rmc.data[8],x9:rmc.data[9],x10:rmc.data[10]})
            counter=counter+1