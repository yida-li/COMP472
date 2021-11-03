import socket
import sys
import time

# client tcp




s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',10010))
server_address=('localhost',20000)
print(sys.stderr,'starting up on %s port %s' % server_address)
s.connect(server_address)


try:
    while(True):
        message =' ping'
        print (sys.stderr,'sending "%s"'%message)
        s.sendall(message.encode('utf-8'))
        time.sleep(2.0)
       # amount_received=0
       # amount_expected=len(message)

        #while amount_received<amount_expected:
         #   data= s.recv(16)
          #  amount_received+=len(data)
           # print(sys.stderr,'receive "%s"'%data)
        
finally:
    print(sys.stderr,'closing socket')
    s.close()