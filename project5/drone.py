import pyautogui
import random
import time
import keyboard
pyautogui.FAILSAFE = False
start = time.time()


def closeBank():
    arbitraryMovement(random.randint(551, 556),random.randint(111, 125),random.uniform(0.78,1.12))
    pyautogui.click()
    temp = random.randint(1, 2)
    for i in range(temp):
        pyautogui.click()
        time.sleep(0.2)
def closeBank2():
    arbitraryMovement(random.randint(551, 556),random.randint(111, 125)+534,random.uniform(0.78,1.12))
    pyautogui.click()
    temp = random.randint(1, 2)
    for i in range(temp):
        pyautogui.click()
        time.sleep(0.2)
def login():
    check=pyautogui.locateOnScreen('authenticatorRecognition/login.png')
    time.sleep(random.uniform(3.3, 3.780))
    if check:
        pyautogui.leftClick(x=449,y=319,duration=1)
        check2=pyautogui.locateOnScreen('authenticatorRecognition/enterusername.png')
        time.sleep(random.uniform(3.3, 3.780))    
        if check2:
            pyautogui.leftClick(x=357,y=291,duration=1)
            pyautogui.typewrite('password',interval=1)
            pyautogui.leftClick(x=312,y=349,duration=1)
            pyautogui.moveTo(random.randint(0,700),random.randint(0,200))
            time.sleep(random.uniform(5.3, 6.780))
            

            pyautogui.leftClick(x=371,y=348,duration=2)
            check4=pyautogui.locateOnScreen('authenticatorRecognition/clickhere.png')
            time.sleep(random.uniform(3.3, 3.780))
            if not check4:
                pyautogui.keyDown('down')
                time.sleep(random.uniform(1.3, 2.380))
                pyautogui.keyUp('down')
                pyautogui.moveTo(x=51,y=142,duration=1)
                
                pyautogui.dragTo(x=227,y=147,duration=2,button='right')

def logout():
    closeBank()
    time.sleep(random.uniform(1.3, 2.380))
    arbitraryMovement(random.randint(640,647),random.randint(502,517),random.uniform(0.5,1.5))
    time.sleep(random.uniform(1.3, 2.380))
    pyautogui.leftClick()
    time.sleep(random.uniform(1.3, 2.380))
    arbitraryMovement(random.randint(607,689),random.randint(453,463),random.uniform(0.5,1.5))
    pyautogui.leftClick()


def checkVPN():
    check=pyautogui.locateOnScreen('authenticatorRecognition/forti.png')
    if check:
        pyautogui.leftClick(x=1434,y=525,duration=2)
        pyautogui.typewrite('password', interval=1)
        pyautogui.leftClick(x=1490,y=587,duration=1)

def normalDeposit():
    X_herbArray = [
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
    ]
    Y_herbArray = [
        random.randint(247, 258),
        random.randint(283, 296),
        random.randint(321, 332),
        random.randint(358, 371),
        random.randint(389, 406),
        random.randint(431, 444),
        random.randint(463, 479),
        random.randint(247, 258),
        random.randint(283, 296),
        random.randint(321, 332),
        random.randint(358, 371),
        random.randint(389, 406),
        random.randint(431, 444),
        random.randint(463, 479),
        random.randint(247, 258),
        random.randint(283, 296),
        random.randint(321, 332),
        random.randint(358, 371),
        random.randint(389, 406),
        random.randint(431, 444),
        random.randint(463, 479),
        random.randint(247, 258),
        random.randint(283, 296),
        random.randint(321, 332),
        random.randint(358, 371),
        random.randint(389, 406),
        random.randint(431, 444),
        random.randint(463, 479),
    ]
    counter1 = 0

    while (counter1 < 4):
        destiny = random.randint(0, 27)
        if (X_herbArray[destiny] != 0 and Y_herbArray[destiny] != 0):
            arbitraryMovement(
                X_herbArray[destiny], Y_herbArray[destiny], random.uniform(0.50, 0.150))
            pyautogui.click()
            time.sleep(random.uniform(0.50, 0.150))
            X_herbArray[destiny] = 0
            Y_herbArray[destiny] = 0

            counter1 = counter1+1

    if (X_herbArray[0] != 0):
        arbitraryMovement(
            X_herbArray[0], Y_herbArray[0], random.uniform(0.50, 0.150))
        pyautogui.click()


def advancedDeposit1():
    X_herbArray = [
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(576, 586),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(616, 630),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(656, 670),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
        random.randint(699, 716),
    ]
    Y_herbArray = [
        random.randint(247, 258),
        random.randint(283, 296),
        random.randint(321, 332),
        random.randint(358, 371),
        random.randint(389, 406),
        random.randint(431, 444),
        random.randint(463, 479),
        random.randint(247, 258),
        random.randint(283, 296),
        random.randint(321, 332),
        random.randint(358, 371),
        random.randint(389, 406),
        random.randint(431, 444),
        random.randint(463, 479),
        random.randint(247, 258),
        random.randint(283, 296),
        random.randint(321, 332),
        random.randint(358, 371),
        random.randint(389, 406),
        random.randint(431, 444),
        random.randint(463, 479),
        random.randint(247, 258),
        random.randint(283, 296),
        random.randint(321, 332),
        random.randint(358, 371),
        random.randint(389, 406),
        random.randint(431, 444),
        random.randint(463, 479),
    ]

    counter1 = 0

    while (counter1 < 7):
        destiny = random.randint(0, 27)
        if (X_herbArray[destiny] != 0 and Y_herbArray[destiny] != 0):
            arbitraryMovement(
                X_herbArray[destiny], Y_herbArray[destiny], random.uniform(0.50, 0.150))
            pyautogui.click()
            time.sleep(random.uniform(0.50, 0.150))
            X_herbArray[destiny] = 0
            Y_herbArray[destiny] = 0

            counter1 = counter1+1

    if (X_herbArray[0] != 0):
        arbitraryMovement(
            X_herbArray[0], Y_herbArray[0], random.uniform(0.50, 0.150))
        pyautogui.click()

    time.sleep(random.uniform(0.601, 0.799))
    if (X_herbArray[17] != 0):
        arbitraryMovement(
            X_herbArray[10], Y_herbArray[10], random.uniform(0.50, 0.150))
        pyautogui.click()

    time.sleep(random.uniform(0.601, 0.799))
    if (X_herbArray[27] != 0):
        arbitraryMovement(
            X_herbArray[27], Y_herbArray[27], random.uniform(0.50, 0.150))
        time.sleep(random.uniform(0.101, 0.199))
        pyautogui.click


def arbitraryMovement(x, y, z):
    temp = random.randint(0, 12)
    if temp == 0:
        pyautogui.moveTo(x, y, z, pyautogui.easeInBack)
    elif temp == 1:
        pyautogui.moveTo(x, y, z, pyautogui.easeInBounce)
    elif temp == 2:
        pyautogui.moveTo(x, y, z, pyautogui.easeInCirc)
    elif temp == 3:
        pyautogui.moveTo(x, y, z, pyautogui.easeInCubic)
    elif temp == 4:
        pyautogui.moveTo(x, y, z, pyautogui.easeInElastic)
    elif temp == 5:
        pyautogui.moveTo(x, y, z, pyautogui.easeInExpo)
    elif temp == 6:
        pyautogui.moveTo(x, y, z, pyautogui.easeInOutBack)
    elif temp == 7:
        pyautogui.moveTo(x, y, z, pyautogui.easeInExpo)
    elif temp == 8:
        pyautogui.moveTo(x, y, z, pyautogui.easeInOutBounce)
    elif temp == 9:
        pyautogui.moveTo(x, y, z, pyautogui.easeInOutCirc)
    elif temp == 10:
        pyautogui.moveTo(x, y, z, pyautogui.easeInOutCubic)
    elif temp == 11:
        pyautogui.moveTo(x, y, z, pyautogui.easeInOutElastic)
    elif temp == 12:
        pyautogui.moveTo(x, y, z, pyautogui.easeInOutExpo)

def sleepsegment():
    temp= random.randint(0,4)
    if temp ==0:
        time.sleep(random.uniform(0.700, 0.800))
    elif temp == 1:
        time.sleep(random.uniform(0.500, 0.900))
    elif temp == 2:
        time.sleep(random.uniform(0.500, 0.600))
    elif temp == 3:
        time.sleep(random.uniform(0.800, 0.900))    
    elif temp == 4:
        time.sleep(random.uniform(0.600, 0.800))  
def SoloClean(x):    
    for i in range(x):

        arbitraryMovement(random.randint(
            429 - 4, 429 + 4), random.randint(198 - 3, 198 + 3), random.uniform(1.89, 2.11))

        pyautogui.click(button='left')
        sleepsegment()
        closeBank()
        # print('phase')
        sleepsegment()
        X_herbArray = [
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
        ]
        Y_herbArray = [
            random.randint(247, 258),
            random.randint(283, 296),
            random.randint(321, 332),
            random.randint(358, 371),
            random.randint(389, 406),
            random.randint(431, 444),
            random.randint(463, 479),
            random.randint(247, 258),
            random.randint(283, 296),
            random.randint(321, 332),
            random.randint(358, 371),
            random.randint(389, 406),
            random.randint(431, 444),
            random.randint(463, 479),
            random.randint(247, 258),
            random.randint(283, 296),
            random.randint(321, 332),
            random.randint(358, 371),
            random.randint(389, 406),
            random.randint(431, 444),
            random.randint(463, 479),
            random.randint(247, 258),
            random.randint(283, 296),
            random.randint(321, 332),
            random.randint(358, 371),
            random.randint(389, 406),
            random.randint(431, 444),
            random.randint(463, 479),
        ]
        # print('phase')
        counter = 0
        # print(X_herbArray)
        # print(Y_herbArray)
        while (counter < 27):

            destiny = random.randint(0, 27)

            if (X_herbArray[destiny] != 0 and Y_herbArray[destiny] != 0):
               # pyautogui.moveTo(X_herbArray[destiny], Y_herbArray[destiny])
                pyautogui.click(
                    button='left', x=X_herbArray[destiny], y=Y_herbArray[destiny])
                # print(destiny)
                X_herbArray[destiny] = 0
                Y_herbArray[destiny] = 0

                counter = counter+1
        # print('phase')
        time.sleep(random.uniform(2.4000, 2.500))

        pyautogui.moveTo(
            random.randint(256, 256 + 97),
            random.randint(190, 190 + 53),random.uniform(0.5,0.953)
        )
        pyautogui.click(button='left')
        time.sleep(random.uniform(0.100, 0.200))
        pyautogui.click(button='left')
        time.sleep(random.uniform(0.634, 0.780))
        normalDeposit()
        end = time.time()
        print(end - start)


def SoloMix(x):

    for i in range(x):

        X_firstHalf = [
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
        ]
        X_secondHalf = [
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
        ]
        Y_firstHalf = [
            random.randint(247, 258),
            random.randint(247, 258),
            random.randint(247, 258),
            random.randint(247, 258),
            random.randint(283, 296),
            random.randint(283, 296),
            random.randint(283, 296),
            random.randint(283, 296),
            random.randint(321, 332),
            random.randint(321, 332),
            random.randint(321, 332),
            random.randint(321, 332),
            random.randint(358, 371),
            random.randint(358, 371),
        ]
        Y_secondHalf = [
            random.randint(358, 371),
            random.randint(358, 371),
            random.randint(389, 406),
            random.randint(389, 406),
            random.randint(389, 406),
            random.randint(389, 406),
            random.randint(431, 444),
            random.randint(431, 444),
            random.randint(431, 444),
            random.randint(431, 444),
            random.randint(463, 479),
            random.randint(463, 479),
            random.randint(463, 479),
            random.randint(463, 479),
        ]

        arbitraryMovement(random.randint(0, 560), random.randint(0, 332), 0.5)

        Choice =random.randint(0,1)
        if Choice==1:
            xlocation = random.randint(380, 382)
            ylocation = random.randint(198 -1, 198+1 )
            arbitraryMovement(xlocation, ylocation, 0.3)

            pyautogui.click(button='right')

            sleepsegment()
            arbitraryMovement(xlocation, ylocation + 85, 0.5)
            pyautogui.click()

            sleepsegment()
            arbitraryMovement(
                random.randint(429 - 4, 429 + 4),
                random.randint(198 - 3, 198 + 3), random.uniform(0.25,0.45)
            )
            pyautogui.click()
        else:
            xlocation = random.randint(429 - 4, 429 + 4)
            ylocation = random.randint(198 - 3, 198 + 3)
            arbitraryMovement(
                xlocation,
                ylocation, random.uniform(0.25,0.45)
            )
            pyautogui.click(button='right')

            sleepsegment()
            arbitraryMovement(xlocation, ylocation + 85, 0.5)
            pyautogui.click()

            sleepsegment()
            arbitraryMovement(
                random.randint(380, 382),
                random.randint(198 -1, 198+1 ), random.uniform(0.25,0.45)
            )
            pyautogui.click()


        closeBank()
        sleepsegment()
        temp = random.randint(0, 13)
        arbitraryMovement(X_firstHalf[temp], Y_firstHalf[temp], 0.2)
        pyautogui.click()
        sleepsegment()
        temp2 = random.randint(0, 13)
        arbitraryMovement(
            X_secondHalf[temp2], Y_secondHalf[temp2], 0.2)
        pyautogui.click()
        sleepsegment()
        arbitraryMovement(random.randint(
            227, 290), random.randint(433, 480), 0.2)
        pyautogui.click()
        time.sleep(random.uniform(0.100, 0.200))
        pyautogui.click()
        time.sleep(random.uniform(8.800, 9.200))

        arbitraryMovement(
            random.randint(256, 256 + 97),
            random.randint(190, 190 + 53), 0.5
        )
        pyautogui.click()
        time.sleep(random.uniform(0.634, 0.780))
        
        moreRandom=random.randint(0,7)
        if moreRandom==0:
            normalDeposit()
        else:
            bankAll()
        
        time.sleep(random.uniform(0.634, 0.780))

def SoloHybrid():
    time.sleep(random.uniform(5.4000, 5.500))
    login()
    time.sleep(random.uniform(1.3, 2.380))
    arbitraryMovement(
            random.randint(256, 256 + 97),
            random.randint(190, 190 + 53), 0.5
        )
    pyautogui.click()
    for i in range(2):
        SoloMix(50)
        arbitraryMovement(random.randint(318,328),random.randint(80,85),random.uniform(0.5,1.5))
        pyautogui.leftClick()
        time.sleep(random.uniform(1.3, 2.380))
        SoloClean(50)
        arbitraryMovement(random.randint(77,85),random.randint(82,89),random.uniform(0.5,1.5))
        pyautogui.leftClick()
        time.sleep(random.uniform(1.3, 2.380))
    logout()

def DoubleMix(x):
       for i in range(x):

        X_firstHalf = [
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
        ]
        X_secondHalf = [
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(699, 716),
        ]
        Y_firstHalf = [
            random.randint(247, 258),
            random.randint(247, 258),
            random.randint(247, 258),
            random.randint(247, 258),
            random.randint(283, 296),
            random.randint(283, 296),
            random.randint(283, 296),
            random.randint(283, 296),
            random.randint(321, 332),
            random.randint(321, 332),
            random.randint(321, 332),
            random.randint(321, 332),
            random.randint(358, 371),
            random.randint(358, 371),
        ]
        Y_secondHalf = [
            random.randint(358, 371),
            random.randint(358, 371),
            random.randint(389, 406),
            random.randint(389, 406),
            random.randint(389, 406),
            random.randint(389, 406),
            random.randint(431, 444),
            random.randint(431, 444),
            random.randint(431, 444),
            random.randint(431, 444),
            random.randint(463, 479),
            random.randint(463, 479),
            random.randint(463, 479),
            random.randint(463, 479),
        ]
        X1_firstHalf = [
      random.randint(576, 586),
      random.randint(616, 630),
      random.randint(656, 670),
      random.randint(699, 716),
      random.randint(576, 586),
      random.randint(616, 630),
      random.randint(656, 670),
      random.randint(699, 716),
      random.randint(576, 586),
      random.randint(616, 630),
      random.randint(656, 670),
      random.randint(699, 716),
      random.randint(576, 586),
      random.randint(616, 630),
    ]
        X1_secondHalf = [
      random.randint(656, 670),
      random.randint(699, 716),
      random.randint(576, 586),
      random.randint(616, 630),
      random.randint(656, 670),
      random.randint(699, 716),
      random.randint(576, 586),
      random.randint(616, 630),
      random.randint(656, 670),
      random.randint(699, 716),
      random.randint(576, 586),
      random.randint(616, 630),
      random.randint(656, 670),
      random.randint(699, 716),
    ]
        Y1_firstHalf = [
      random.randint(247, 258) + 534,
      random.randint(247, 258) + 534,
      random.randint(247, 258) + 534,
      random.randint(247, 258) + 534,
      random.randint(283, 296) + 534,
      random.randint(283, 296) + 534,
      random.randint(283, 296) + 534,
      random.randint(283, 296) + 534,
      random.randint(321, 332) + 534,
      random.randint(321, 332) + 534,
      random.randint(321, 332) + 534,
      random.randint(321, 332) + 534,
      random.randint(358, 371) + 534,
      random.randint(358, 371) + 534,
    ]
        Y1_secondHalf = [
      random.randint(358, 371) + 534,
      random.randint(358, 371) + 534,
      random.randint(389, 406) + 534,
      random.randint(389, 406) + 534,
      random.randint(389, 406) + 534,
      random.randint(389, 406) + 534,
      random.randint(431, 444) + 534,
      random.randint(431, 444) + 534,
      random.randint(431, 444) + 534,
      random.randint(431, 444) + 534,
      random.randint(463, 479) + 534,
      random.randint(463, 479) + 534,
      random.randint(463, 479) + 534,
      random.randint(463, 479) + 534,
    ]
        arbitraryMovement(random.randint(0, 560), random.randint(0, 332), 0.5)

        Choice =random.randint(0,1)
        if Choice==1:
            xlocation = random.randint(380, 382)
            ylocation = random.randint(198 -1, 198+1 )
            arbitraryMovement(xlocation, ylocation, 0.3)

            pyautogui.click(button='right')

            sleepsegment()
            arbitraryMovement(xlocation, ylocation + 85, 0.5)
            pyautogui.click()

            sleepsegment()
            arbitraryMovement(
                random.randint(429 - 4, 429 + 4),
                random.randint(198 - 3, 198 + 3), random.uniform(0.25,0.45)
            )
            pyautogui.click()
            

            #second screen
            arbitraryMovement(xlocation, ylocation+534, 0.3)

            pyautogui.click(button='right')

            sleepsegment()
            arbitraryMovement(xlocation, ylocation + 85+534, 0.5)
            pyautogui.click()

            sleepsegment()
            arbitraryMovement(
                random.randint(429 - 4, 429 + 4),
                random.randint(198 - 3, 198 + 3)+534, random.uniform(0.25,0.45)
            )
            pyautogui.click()


        else:
            xlocation = random.randint(429 - 4, 429 + 4)
            ylocation = random.randint(198 - 3, 198 + 3)
            arbitraryMovement(
                xlocation,
                ylocation, random.uniform(0.25,0.45)
            )
            time.sleep(random.uniform(0.1,0.2))
            pyautogui.click(button='right')

            sleepsegment()
            arbitraryMovement(xlocation, ylocation + 85, 0.5)
            pyautogui.click()

            sleepsegment()
            arbitraryMovement(
                random.randint(380, 382),
                random.randint(198 -1, 198+1 ), random.uniform(0.25,0.45)
            )
            pyautogui.click()
            #
            #

            arbitraryMovement(
                xlocation,
                ylocation+534, random.uniform(0.25,0.45)
            )
            time.sleep(random.uniform(0.1,0.2))
            pyautogui.click(button='right')

            sleepsegment()
            arbitraryMovement(xlocation, ylocation + 85+534, 0.5)
            pyautogui.click()

            sleepsegment()
            arbitraryMovement(
                random.randint(380, 382),
                random.randint(198 -1, 198+1 )+534, random.uniform(0.25,0.45)
            )
            pyautogui.click()
            

        closeBank()
        closeBank2()
        sleepsegment()
        
        temp = random.randint(0, 13)
        arbitraryMovement(X1_firstHalf[temp], Y1_firstHalf[temp], 0.2)
        pyautogui.click()
        sleepsegment()
        temp2 = random.randint(0, 13)
        arbitraryMovement(
            X1_secondHalf[temp2], Y1_secondHalf[temp2], 0.2)
        pyautogui.click()
        sleepsegment()
        arbitraryMovement(random.randint(
            227, 290), random.randint(433, 480)+534, 0.2)
        pyautogui.click()
        time.sleep(random.uniform(0.100, 0.200))
        pyautogui.click()
        
        temp = random.randint(0, 13)
        arbitraryMovement(X_firstHalf[temp], Y_firstHalf[temp], 0.2)
        pyautogui.click()
        sleepsegment()
        temp2 = random.randint(0, 13)
        arbitraryMovement(
            X_secondHalf[temp2], Y_secondHalf[temp2], 0.2)
        pyautogui.click()
        sleepsegment()
        arbitraryMovement(random.randint(
            227, 290), random.randint(433, 480), 0.2)
        pyautogui.click()
        time.sleep(random.uniform(0.100, 0.200))
        pyautogui.click()



        time.sleep(random.uniform(8.800, 9.200))

        arbitraryMovement(
            random.randint(256, 256 + 97),
            random.randint(190, 190 + 53), 0.5
        )
        pyautogui.click()
        arbitraryMovement(
            random.randint(256, 256 + 97),
            random.randint(190, 190 + 53)+534, 0.5
        )
        pyautogui.click()    





        time.sleep(random.uniform(0.634, 0.780))
        
        bankAll()
        bankAll2()
        
        time.sleep(random.uniform(0.634, 0.780))




def speedclick():

    while True:
        #click all inventory
        if keyboard.is_pressed('i'):
        
            time.sleep(0.1)

            X_herbArray = [
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(576, 586),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(616, 630),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(656, 670),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
            random.randint(699, 716),
        ]
            Y_herbArray = [
                random.randint(247, 258),
                random.randint(283, 296),
                random.randint(321, 332),
                random.randint(358, 371),
                random.randint(389, 406),
                random.randint(431, 444),
                random.randint(463, 479),
                random.randint(247, 258),
                random.randint(283, 296),
                random.randint(321, 332),
                random.randint(358, 371),
                random.randint(389, 406),
                random.randint(431, 444),
                random.randint(463, 479),
                random.randint(247, 258),
                random.randint(283, 296),
                random.randint(321, 332),
                random.randint(358, 371),
                random.randint(389, 406),
                random.randint(431, 444),
                random.randint(463, 479),
                random.randint(247, 258),
                random.randint(283, 296),
                random.randint(321, 332),
                random.randint(358, 371),
                random.randint(389, 406),
                random.randint(431, 444),
                random.randint(463, 479),
            ]
            # print('phase')
            counter = 0
            # print(X_herbArray)
            # print(Y_herbArray)
            while (counter < 27):

                destiny = random.randint(0, 27)

                if (X_herbArray[destiny] != 0 and Y_herbArray[destiny] != 0):
                # pyautogui.moveTo(X_herbArray[destiny], Y_herbArray[destiny])
                    pyautogui.click(
                        button='left', x=X_herbArray[destiny], y=Y_herbArray[destiny])
                    # print(destiny)
                    X_herbArray[destiny] = 0
                    Y_herbArray[destiny] = 0
                    counter = counter+1
        #click bank area
        if keyboard.is_pressed('o'):
            arbitraryMovement(
            random.randint(256, 256 + 97),
            random.randint(190, 190 + 53), random.uniform(0.2,0.5)
        )
            pyautogui.click()
        #close bank
        if keyboard.is_pressed('u'):
            closeBank()
        #click 1 thing to withdraw
        if keyboard.is_pressed('y'):   
            arbitraryMovement( 
                    random.randint(418, 430),random.randint(193, 206), random.uniform(0.2,0.5))
            pyautogui.click()   
        #disposite allo
        if keyboard.is_pressed('p'):   
            bankAll()
def bankAll():
            arbitraryMovement( 
                    random.randint(437, 458),random.randint(333, 349), random.uniform(0.2,0.5))
            pyautogui.click() 
def bankAll2():
            arbitraryMovement( 
                    random.randint(437, 458),random.randint(333, 349)+534, random.uniform(0.2,0.5))
            pyautogui.click() 
#while True:
    #SoloMix(40)
    #checkVPN()
#SoloMix(500)
#SoloHybrid()
#login()n
#logout()
#login()speedclick()
speedclick()
#lamda for 2 cordinates
#SoloClean(200)