import pyautogui
import random
import time
# move mouse up, pause 2 second, and move mouse down, pause 2 second
# also, move mouse top left will stop the program. Godly tool right here ngl

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 180


while(True):
    
    pyautogui.moveTo(random.randint(0, 500),
                     random.randint(0, 500), duration=2)
    pyautogui.click(button='right')
    pyautogui.moveTo(random.randint(0, 500),
                     random.randint(5, 500), duration=2)
    
