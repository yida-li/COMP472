import socket
import sys
HOST ='0.0.0.0'
PORT = 8885

# UDP Server
 

try:
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ('Socket created')
#except socket.error, msg:
except:
    #print ('failed to create socket error :'+str(msg[0])+'Message'+msg[1])
    print ('failed to create socket error ')
    sys.exit()

try:
    #s.bind((HOST,PORT))
    s.bind(("localhost", 8081))
except:
#except socket.error, msg:
        #print('bind failed. errroer:' +str(msg[0])+'Message'+msg[1])
        print('bind fail')
        sys.exit()

        
while 1:
    d= s.recvfrom(1024)
    data=d[0]
    addr=d[1]
    print(data)
    if not data:
        break

    reply=('Ok,,,')
    s.send("received".encode(),addr)
    print ('Message['+addr[0]+':'+str(addr[1])+']-'+ data.strip())
s.close()    