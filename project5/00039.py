import time
import random
import pyautogui
pyautogui.PAUSE = 1.0
temp = 0
while(True):

    if temp == 0:
        pyautogui.moveTo(100, 100, 2, pyautogui.easeInBack)
    elif temp == 1:
        pyautogui.moveTo(900, 100, 2, pyautogui.easeInBounce)
    elif temp == 2:
        pyautogui.moveTo(100, 900, 2, pyautogui.easeInCirc)
    elif temp == 3:
        pyautogui.moveTo(900, 900, 2, pyautogui.easeInCubic)
    elif temp == 4:
        pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)
    elif temp == 5:
        pyautogui.moveTo(900, 100, 2, pyautogui.easeInExpo)
    elif temp == 6:
        pyautogui.moveTo(100, 900, 2, pyautogui.easeInOutBack)
    elif temp == 7:
        pyautogui.moveTo(900, 900, 2, pyautogui.easeInExpo)
    elif temp == 8:
        pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutBounce)
    elif temp == 9:
        pyautogui.moveTo(900, 100, 2, pyautogui.easeInOutCirc)
    elif temp == 10:
        pyautogui.moveTo(100, 900, 2, pyautogui.easeInOutCubic)
    elif temp == 11:
        pyautogui.moveTo(900, 900, 2, pyautogui.easeInOutElastic)
    elif temp == 12:
        pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutExpo)
    temp = temp+1
