import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# server TCP




server_address =('localhost',20000)
print(sys.stderr,'starting up on %s port %s'% server_address)
s.bind(server_address)


#server starts listening on the port
s.listen(1)
while True:
        #Wait for a connection
        print (sys.stderr,'waiting for connection')
        connection, client_address= s.accept()



        try: 
            print ( sys.stderr,'connection from', client_address)

            while True:
                data= connection.recv(16)
                #print(sys.stderr,'receive"%s"' % data)

                if data:
                    print( sys.stderr,'pong')
                    connection.sendall(data)
                else:
                    print( sys.stderr,'no more data from', client_address)
                    break
        finally:
            connection.close()
