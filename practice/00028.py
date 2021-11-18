# 28. : Sound system
####################################################

import multiprocessing
import sys
from playsound import playsound


def playmusic():

    playsound('practice/practice_music.mp3')


def Bernard():
    # <--- Here's the magic line...you'll need to "import sys" above too
    sys.stdin = open(0)
    while True:
        string = input("Enter a string: ")
        print(string)


if __name__ == "__main__":

    # creating multiple processes

    proc1 = multiprocessing.Process(target=Bernard)

    proc2 = multiprocessing.Process(target=playmusic)

# Initiating process 1

    proc1.start()

# Initiating process 2

    proc2.start()

# Waiting until proc1 finishes

    proc1.join()

# Waiting until proc2 finishes

    proc2.join()

# Processes finished

    print(" once you wake up which you wont")