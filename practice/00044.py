import socket
import sys
#tcp client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 11001)
print('Connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)
try:
        while True:
            message = 'Ping'
            alert= input("enter something")
            print('Sending "%s"' % message)
            sock.sendall(alert.encode())


            data = sock.recv(16)
            
            print('Received "%s"' % data, file=sys.stderr)

finally:
        print('Closing Socket', file=sys.stderr)
        sock.close()
