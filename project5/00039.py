import pyautogui


# 20-30 lists of mouse movements for imitation

pyautogui.PAUSE = 2.5
while(True):
    pyautogui.moveTo(700, 700, 2, pyautogui.easeInElastic)
    print(pyautogui.position())
    pyautogui.moveTo(500, 500, 2, pyautogui.easeInElastic)
    print('phase')
    pyautogui.moveTo(700, 700, 2, pyautogui.easeInBounce)
    print(pyautogui.position())
    pyautogui.moveTo(500, 500, 2, pyautogui.easeInBounce)
    print('phase 1')
    pyautogui.moveTo(900, 700, 2, pyautogui.easeInOutElastic)
    print(pyautogui.position())
    pyautogui.moveTo(900, 500, 2, pyautogui.easeInOutElastic)
    print('phase 2')
    pyautogui.moveTo(300, 400, 2, pyautogui.easeInOutCirc)
    print(pyautogui.position())
    pyautogui.moveTo(200, 100, 2, pyautogui.easeInOutCirc)
    print('phase 3')
