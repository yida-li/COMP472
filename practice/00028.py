####################################################
# 28. : Sound system
####################################################

import multiprocessing
import sys
import random
import time

#from playsound import playsound


#def playmusic():

 #   playsound('practice/practice_music.mp3')

layer=[2]

def Bernard():
    # <--- Here's the magic line...you'll need to "import sys" above too
    sys.stdin = open(0)
    while True:
        string = input("Enter a string: ")
        print(string)

def random3():
    layer.insert(random.randint(0, 10))
    #print(random.randint(0, 10))
    

def random2():
    while not layer:
        temp = layer.pop()
        if(temp==10):
            print("temp is equal to 10")
        elif (temp>=10):
            print("temp is bigger than 10")
        elif (temp<=10):
            print("temp is smaller than 10")
    #print(random.randint(0, 20))

if __name__ == "__main__":

    while(True):
        # creating multiple processes
       
        proc1 = multiprocessing.Process(target=random2)

        proc2 = multiprocessing.Process(target=random3)

    # Initiating process 1

        proc1.start()

    # Initiating process 2

        proc2.start()

    # Waiting until proc1 finishes

        proc1.join()

    # Waiting until proc2 finishes

        proc2.join()
        time.sleep(1.0)
    # Processes finished
        print(layer)
        print(" -----------------")
