import multiprocessing
import sys
import time


def playmusic():
        time.sleep(10)
        print('thread 1 sleeping')


def Bernard():
    # <--- Here's the magic line...you'll need to "import sys" above too
    sys.stdin = open(0)
    while True:
        string = input("Enter a string: ")
        print(string)

def William():
        time.sleep(1)
        print('T1')

def Arthur():
        time.sleep(4)
        print('T2')       

def Ford():
        time.sleep(5)
        print('T3')          

if __name__ == "__main__":

    # creating multiple processes

    proc1 = multiprocessing.Process(target=Bernard)

    proc2 = multiprocessing.Process(target=playmusic)

    proc3 = multiprocessing.Process(target=Ford)

    proc4 = multiprocessing.Process(target=Arthur)

    proc5 = multiprocessing.Process(target=William)

# Initiating process 1

    proc1.start()

# Initiating process 2

    proc2.start()
    proc3.start()
    proc4.start()
    proc5.start()

# Waiting until proc1 finishes

    proc1.join()

# Waiting until proc2 finishes

    proc2.join()
    proc3.join()
    proc4.join()
    proc5.join()
# Processes finished

    print(" once you wake up which you wont")