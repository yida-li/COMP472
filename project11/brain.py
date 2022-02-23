
import pyautogui
import random
import time

pyautogui.PAUSE = 4.0
pyautogui.FAILSAFE=False

def processing():
    x = random.randint(0, 10)
    if x!=0:
        y=random.randint(30,400)
        time.sleep(y)
    else:
        y=random.randint(600,1800)
        time.sleep(y)

def tachypsychia():
    x = random.randint(0, 1)
    time.sleep(x)

while(True):
    x = random.randint(0, 4)
    if x==0:
        pyautogui.moveTo(135, 121, 2, pyautogui.easeInElastic)
        processing()
        #tachypsychia()
        pyautogui.click()
        pyautogui.moveTo(599, 323, 2, pyautogui.easeInElastic)
        pyautogui.click()

    if x==1:
        pyautogui.moveTo(135, 143, 2, pyautogui.easeInElastic)
        processing()
        #tachypsychia()
        pyautogui.click()
        pyautogui.moveTo(599, 323, 2, pyautogui.easeInElastic)
        pyautogui.click()
    if x==2:
        pyautogui.moveTo(135, 170, 2, pyautogui.easeInElastic)
        processing()
        #tachypsychia()
        pyautogui.click()
        pyautogui.moveTo(599, 323, 2, pyautogui.easeInElastic)
        pyautogui.click()
    if x==3:
        pyautogui.moveTo(135, 191, 2, pyautogui.easeInElastic)
        processing()
        #tachypsychia()
        pyautogui.click()
        pyautogui.moveTo(599, 323, 2, pyautogui.easeInElastic)
        pyautogui.click()
    if x==4:
        pyautogui.moveTo(135, 209, 2, pyautogui.easeInElastic)
        processing()
        #tachypsychia()
        pyautogui.click()
        pyautogui.moveTo(599, 323, 2, pyautogui.easeInElastic)
        pyautogui.click()


