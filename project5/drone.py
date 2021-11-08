import pyautogui
import random
import time
pyautogui.FAILSAFE = False
start = time.time()


def closeBank():
    pyautogui.moveTo(random.randint(551, 556), random.randint(111, 125))
    pyautogui.click()
    temp = random.randint(1, 2)
    for i in range(temp):
        pyautogui.click()
        time.sleep(0.2)


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


def SoloClean():
    for i in range(1000):

        arbitraryMovement(random.randint(
            429 - 4, 429 + 4), random.randint(198 - 3, 198 + 3), random.uniform(1.89, 2.11))

        pyautogui.click(button='left')
        time.sleep(random.uniform(0.700, 0.800))
        closeBank()
        # print('phase')
        time.sleep(random.uniform(0.700, 0.800))
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
            random.randint(190, 190 + 53)
        )
        pyautogui.click(button='left')
        time.sleep(random.uniform(0.100, 0.200))
        pyautogui.click(button='left')
        time.sleep(random.uniform(0.634, 0.780))
        advancedDeposit1()
        end = time.time()
        print(end - start)


def SoloMix():

    for i in range(1000):

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

        x = 3
        y = 3

        xlocation = random.randint(381 - x, 381 + x)
        ylocation = random.randint(198 - y, 198 + y)
        arbitraryMovement(xlocation, ylocation, 0.1)

        pyautogui.click(button='right')

        time.sleep(random.uniform(0.700, 0.800))
        arbitraryMovement(xlocation, ylocation + 85, 0.5)
        pyautogui.click()

        time.sleep(random.uniform(0.700, 0.800))
        arbitraryMovement(
            random.randint(429 - 4, 429 + 4),
            random.randint(198 - 3, 198 + 3), 0.1
        )
        pyautogui.click()

        closeBank()
        time.sleep(random.uniform(0.700, 0.800))
        temp = random.randint(0, 13)
        arbitraryMovement(X_firstHalf[temp], Y_firstHalf[temp], 0.2)
        pyautogui.click()
        time.sleep(random.uniform(0.700, 0.800))
        temp2 = random.randint(0, 13)
        arbitraryMovement(
            X_secondHalf[temp2], Y_secondHalf[temp2], 0.2)
        pyautogui.click()
        time.sleep(random.uniform(0.700, 0.800))
        arbitraryMovement(random.randint(
            227, 290), random.randint(433, 480), 0.2)
        pyautogui.click()
        time.sleep(random.uniform(0.100, 0.200))
        pyautogui.click()
        time.sleep(random.uniform(8.800, 9.200))

        arbitraryMovement(
            random.randint(256, 256 + 97),
            random.randint(190, 190 + 53), 0.1
        )
        pyautogui.click()
        time.sleep(random.uniform(0.634, 0.780))
        normalDeposit()
        time.sleep(random.uniform(0.634, 0.780))


SoloMix()
