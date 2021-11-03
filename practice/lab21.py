import socket # for sockets
import sys
client_host ='0.0.0.0'
client_port = 8889

#UDP client

try:
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

s.bind((client_host,client_port))
host= '0.0.0.0'
port =8885

 

while(1):
    msg= input('Enter message to send:')
    
    try: 
        s.sendto(msg,(host,port))
        d= s.recvfrom(1024)
        reply=d[0]
        addr=d[1]
        print('Server reply:'+reply)
    except:
        print(socket.error)
    #except socket.error,msg:
