import socket
import sys
import json
import datetime
import random
HOST = '0.0.0.0'
PORT = 11112
print('Initialiting server at port the default UDP PORT: ',PORT)
print('IP ADDRESS: ',socket.gethostbyname(socket.gethostname()))


requestNumber=random.randint(0,40000)
# check if client_list exists, if not create one with empty dictionary inside
try:
    with open('client_list.json', 'r+') as reader:
        rereader = json.load(reader)
        print(rereader)
    reader.close()
except:
    currentTime = datetime.datetime.now()
    with open('log.txt', 'a+') as logfile:   
        logfile.write(str(currentTime)+' : Creating an empty clientlist')
        logfile.write('\n')
    logfile.close()
    f6 = {}
    with open('client_list.json', 'w+') as writer:
            writer.write(json.dumps(f6))
    writer.close()

# Initialize socket
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
    currentTime = datetime.datetime.now()
    with open('log.txt', 'a+') as logfile:   
        logfile.write(str(currentTime)+' : Sucessfully created socket')
        logfile.write('\n')
    logfile.close() 
except socket.error as msg:
    print('Failed to created socket. Error code :' + str(msg[0]) + ' Message ' + msg[1])
    currentTime = datetime.datetime.now()
    with open('log.txt', 'a+') as logfile:   
        logfile.write(str(currentTime)+' : Failed to initialize socket')
        logfile.write('\n')
    logfile.close()    
    sys.exit()

# Initialize bind
try:
    serverSocket.bind((HOST, PORT))
    currentTime = datetime.datetime.now()
    with open('log.txt', 'a+') as logfile:   
        logfile.write(str(currentTime)+' : Scoket bind complete')
        logfile.write('\n')
    logfile.close()    
    print ('Socket bind complete')
except socket.error as msg:
    print ('Bind Failed. Error code: ' + str(msg[0]) + ' Message ' + msg[1])
    currentTime = datetime.datetime.now()
    with open('log.txt', 'a+') as logfile:   
        logfile.write(str(currentTime)+' : Socket bind error')
        logfile.write('\n')
    logfile.close()
    sys.exit()


# Keep receiving data
while 1:

    data_Received = serverSocket.recvfrom(1024)
    data = data_Received[0]
    client_Address = data_Received[1]

    # pass everything and wait for new data received in line 45
    if not data:
        pass
    
    isClient=False    
    temp = data.decode()
    with open('client_list.json', 'r+') as reader:
                    clientlistChcker = json.load(reader)
    reader.close()
    
 
    if clientlistChcker: # if it has stuff inside
        for key, values in clientlistChcker.items():

                if str(client_Address[0])==values[0]:
                    isClient=True
                    break
            
                        
    reader.close()    
    if temp =='registration':
        message = 'please enter your username'
        
        serverSocket.sendto(message.encode(),client_Address)
        flag = 0
        while flag<1:
                data_Received = serverSocket.recvfrom(1024)
                data = data_Received[0]
                client_Address = data_Received[1]
                name = data.decode()
                with open('client_list.json', 'r+') as reader:
                    clientlistObject = json.load(reader)
                yida=clientlistObject
                reader.close()
                if name in clientlistObject:    
                    message = 'REGISTER-DENIED RQ : '+str(requestNumber)+' Reason : '+name+' already exist'
                    reply = message.encode()
                    serverSocket.sendto(reply,client_Address)
                    currentTime = datetime.datetime.now()
                    with open('log.txt', 'a+') as logfile:   
                        logfile.write(str(currentTime)+' : REGISTER-DENIED RQ : '+str(requestNumber)+' Reason : '+name+' already exist')
                        logfile.write('\n')
                    logfile.close()   
                    requestNumber=requestNumber+1 
                else:
                    yida.setdefault(name, [client_Address[0],str(client_Address[1])])
                
                    message = 'REGISTERED '+str(requestNumber)
                    reply = message.encode()
                    serverSocket.sendto(reply,client_Address)
                    flag2=0
                    while flag2<1:
                        data_Received = serverSocket.recvfrom(1024)
                        data = data_Received[0]
                        
                        tcpport = data.decode()
                        yida[name].append(tcpport)
                        yida[name].append([])                        
                        with open('client_list.json', 'w+') as writer:
                            writer.write(json.dumps(yida))
                        writer.close()    
                        currentTime = datetime.datetime.now()
                        with open('log.txt', 'a+') as logfile:   
                            logfile.write(str(currentTime)+' : '+name+' REGISTERED')
                            logfile.write('\n')
                        logfile.close()                     
                        flag2=flag2+1          
                flag=flag+1 # finish loop
    elif temp == 'print' and isClient ==True:
        with open('client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)
        
        reader.close()
        reply = json.dumps(clientlistObject).encode()
        serverSocket.sendto(reply,client_Address)
    
    elif temp == 'RETRIEVE-ALL' and isClient ==True:
        with open('client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)
        
        reader.close()
        reply = json.dumps(clientlistObject).encode()
        serverSocket.sendto(reply,client_Address)

    elif temp == 'RETRIEVE-INFOT' and isClient ==True:
        with open('client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)
        message = 'enter the name of person you would like info on'
        reader.close()        
        reply = message.encode()
        serverSocket.sendto(reply,client_Address)
        data_Received = serverSocket.recvfrom(1024)
        data = data_Received[0]        
        nameChecker=False        
        for key, values in clientlistObject.items():
            if key==data.decode():
                message='name:'+key+', ip:'+values[0]+', udp port:'+values[1]+', tcp port: '+values[2]+', list of files available : '
                for i in values[3]:
                    message+= i
                    message+= ' '
                reply=message.encode()
                serverSocket.sendto(reply,client_Address)
                nameChecker=True
                break
        if nameChecker==False:
                message='this person does not exist'
                reply=message.encode()
                serverSocket.sendto(reply,client_Address)           



    elif temp == 'Publish' and isClient ==True:
        with open('client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)        
        reader.close()

        PublishChecker=False

        for key, values in clientlistObject.items():

            if str(client_Address[0])==values[0]:
                message = 'enter the name of the file'
                reply = message.encode()
                serverSocket.sendto(reply,client_Address)
                data_Received = serverSocket.recvfrom(1024)
                data = data_Received[0]
                          
                values[3].append(data.decode())
                message = 'published'
                reply = message.encode()
                serverSocket.sendto(reply,client_Address)
                PublishChecker=True
                break
        if PublishChecker==False:
                message = 'publish denied'
                reply = message.encode()
                serverSocket.sendto(reply,client_Address)  
        with open('client_list.json', 'w+') as writer:
            writer.write(json.dumps(clientlistObject))
        writer.close() 


    elif temp == 'Remove' and isClient ==True:
        with open('client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)        
        reader.close()

        RemoveChecker=False

        for key, values in clientlistObject.items():

            if str(client_Address[0])==values[0]:
                message = 'enter the name of the file to remove'
                reply = message.encode()
                serverSocket.sendto(reply,client_Address)
                data_Received = serverSocket.recvfrom(1024)
                data = data_Received[0]
                
                for i in values[3]:

                        if i == data.decode():
                            values[3].remove(i)
                                          
                
                            message = 'removed'
                            reply = message.encode()
                            serverSocket.sendto(reply,client_Address)
                            RemoveChecker=True
                            break               
        if RemoveChecker==False:
                message = 'publish denied'
                reply = message.encode()
                serverSocket.sendto(reply,client_Address)  
        with open('client_list.json', 'w+') as writer:
            writer.write(json.dumps(clientlistObject))
        writer.close()    

    elif temp == 'SEARCH-FILE' and isClient ==True:
        with open('client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)        
        reader.close()

        FileChecker=False
        fileInfo=''
        message = 'enter the name of the file to search for'
        reply = message.encode()
        serverSocket.sendto(reply,client_Address)
        data_Received = serverSocket.recvfrom(1024)
        data = data_Received[0]


        for key, values in clientlistObject.items():

                for i in values[3]:

                        if i == data.decode():
                            
                            fileInfo+='name:'+key+', ip: '+values[0]+', tcp port: '+values[2]+'    '              
                

                            FileChecker=True
                            


        if FileChecker==False:
                message = 'Search-ERROR!'
                reply = message.encode()
                serverSocket.sendto(reply,client_Address)

        
        reply = fileInfo.encode()
        serverSocket.sendto(reply,client_Address)


    elif temp == 'DE-REGISTER' and isClient ==True:
        with open('client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)        
        reader.close()
        
        for key, values in clientlistObject.items():

            if str(client_Address[0])==values[0]:
                clientlistObject.pop(key)
                break
        with open('client_list.json', 'w+') as writer:
            writer.write(json.dumps(clientlistObject))
        writer.close()          
        message = 'de-registeration'
        reply = message.encode()
        serverSocket.sendto(reply,client_Address)

    elif temp == 'UPDATE' and isClient ==True:
        with open('client_list.json', 'r+') as reader:
            clientlistObject = json.load(reader)        
        reader.close()
        updateChecker=False
        for key, values in clientlistObject.items():

            if str(client_Address[0])==values[0]:
                
                message = 'enter the new ip address, or enter nothing to stay the same'
                reply = message.encode()
                serverSocket.sendto(reply,client_Address)
                data_Received = serverSocket.recvfrom(1024)
                data = data_Received[0]
                if data.decode()=='':
                    
                    message = 'ip didnt change enter the new tcp address, or enter nothing to stay the same'
                    reply = message.encode()
                    serverSocket.sendto(reply,client_Address)
                    
                else:
                    values[0]=data.decode()                  
                    updateChecker=True
                    message = 'ip did changed to'+values[0]+' enter the new tcp address, or enter nothing to stay the same'
                    reply = message.encode()
                    serverSocket.sendto(reply,client_Address)


                data_Received = serverSocket.recvfrom(1024)
                data = data_Received[0]
                if data.decode()=='':
                    message = 'tcp didnt change, enter the new tcp address, or enter nothing to stay the same'
                    reply = message.encode()
                    serverSocket.sendto(reply,client_Address)
                else:
                    updateChecker=True
                    values[2]=data.decode() 
                    message = 'tcp did changed to'+values[2]+', enter the new tcp address, or enter nothing to stay the same'
                    reply = message.encode()
                    serverSocket.sendto(reply,client_Address)



                data_Received = serverSocket.recvfrom(1024)
                data = data_Received[0]
                if data.decode()=='':
                    pass
                    
                else:
                    updateChecker=True
                    values[1]=data.decode()                  
                    

                  

        with open('client_list.json', 'w+') as writer:
            writer.write(json.dumps(clientlistObject))
        writer.close()    

        if updateChecker==False:      
            message = 'not updated'
            reply = message.encode()
            serverSocket.sendto(reply,client_Address)
        else:
            message = 'updated'
            reply = message.encode()
            serverSocket.sendto(reply,client_Address)              

    elif isClient ==False:
        message = 'ur not a client'
        reply = message.encode()
        serverSocket.sendto(reply,client_Address)
    else:
        message = 'useless request, send something else'
        reply = message.encode()
        serverSocket.sendto(reply,client_Address)
    #print('Message[' + client_Address[0] + ':' + str(client_Address[1]) + '] - ' + str(data.strip()))
    
serverSocket.close()
