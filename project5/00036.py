import pyautogui

# foundation of a GUI

while(True):
    temp = pyautogui.confirm('Would you like to play again?')
    if temp == 'Cancel':
        break
