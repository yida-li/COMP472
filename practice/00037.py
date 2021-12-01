import pyautogui
pyautogui.PAUSE = 1.0
# pixel detecion
check=pyautogui.locateOnScreen('practice/forti.png')
if check:
    pyautogui.leftClick(x=1434,y=525,duration=2)
    pyautogui.typewrite('password', interval=1)
    pyautogui.leftClick(x=1490,y=587,duration=1)
    

