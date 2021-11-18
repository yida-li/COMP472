import socket
import sys
import json
HOST = '0.0.0.0'
PORT = 11112
with open('practice/practice.txt', 'w') as f:

    for f1 in f1:
        f.write(f1)
        
client_list = {}
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except socket.error as msg:
    print('Failed to created socket. Error code :' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind Failed. Error code: ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ('Socket bind complete')

while 1:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data:
        break
    
    isClient=False    
    temp = data.decode()
    with open('project6/client_list.json', 'r+') as reader:
                    clientlistChcker = json.load(reader)
    reader.close()
    for key, values in clientlistChcker.items():

        if str(addr[1])==values[1]:
            isClient=True
            break
          
                        
    reader.close()    
    if temp =='registration':
        message = 'please enter your username'
        reply = message.encode()
        s.sendto(reply,addr)
        flag = 0
        while flag<1:
                d = s.recvfrom(1024)
                data = d[0]
                addr = d[1]
                name = data.decode()
                with open('project6/client_list.json', 'r+') as reader:
                    clientlistObject = json.load(reader)
                yida=clientlistObject
                reader.close()
                if name in clientlistObject:    
                    message = 'name already exist , request denied'
                    reply = message.encode()
                    s.sendto(reply,addr)
                else:
                    yida.setdefault(name, [addr[0],str(addr[1])])
                    with open('project6/client_list.json', 'w+') as writer:
                        writer.write(json.dumps(yida))
                    writer.close()                
                    message = 'client registered'
                    reply = message.encode()
                    s.sendto(reply,addr)           
                flag=flag+1 # finish loop
    elif temp == 'print' and isClient ==True:
        with open('project6/client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)
        
        reader.close()
        reply = json.dumps(clientlistObject).encode()
        s.sendto(reply,addr)
    
    elif temp == 'RETRIEVE-ALL' and isClient ==True:
        with open('project6/client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)
        
        reader.close()
        reply = json.dumps(clientlistObject).encode()
        s.sendto(reply,addr)
    elif temp == 'DE-REGISTER' and isClient ==True:
        with open('project6/client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)        
        reader.close()
        
        for key, values in clientlistObject.items():

            if str(addr[1])==values[1]:
                clientlistObject.pop(key)
                break
        with open('project6/client_list.json', 'w+') as writer:
            writer.write(json.dumps(clientlistObject))
        writer.close()          
        message = 'de-registeration'
        reply = message.encode()
        s.sendto(reply,addr)        
        
    elif isClient ==False:
        message = 'ur not a client'
        reply = message.encode()
        s.sendto(reply,addr)
    else:
        message = 'useless request, send something else'
        reply = message.encode()
        s.sendto(reply,addr)
    #print('Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + str(data.strip()))
    
s.close()
