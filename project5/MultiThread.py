import threading
import random
import time

temp=[]
s=2
class Labone(threading.Thread):
    def __init__(self,a):
        super(Labone,self).__init__()
        self.a=1
      
    def run(self):
        
        while(True):
            
            time.sleep(1.0)
            self.a = random.randint(0, 20)
          #  print(random.randint(0, 10))
         #   print("something happens")


def f(x):
    
    while(True):
        
        time.sleep(1.0)
       
            #print(temp)
        if (x.a==10):
                    print(x.a,'= 10')
        elif (x.a<10):
                    print(x.a,'< 10')
        elif(x.a>10):
                    print(x.a,'>10')        
thread2=Labone(2)
thread= threading.Thread(target=f,args=(thread2,))


#thread3= threading.Thread(target=f,args=(5,))
#thread4=Labone(5)

thread.start()
thread2.start()
#thread3.start()
#thread4.start()

thread.join()
thread2.join()
#thread3.join()
#thread4.join()