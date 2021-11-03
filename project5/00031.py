import pyautogui
import random

# move mouse up, pause 2 second, and move mouse down, pause 2 second
# also, move mouse top left will stop the program. Godly tool right here ngl

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2.5


while(True):
    random.randint(0, 20)
    pyautogui.moveTo(random.randint(0, 1800),
                     random.randint(0, 300), duration=2)
    print(pyautogui.position())
    pyautogui.moveTo(random.randint(0, 1800),
                     random.randint(300, 600), duration=2)
    print('phase')
