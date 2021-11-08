import pyautogui

# More message box functions

while(True):
    temp = pyautogui.confirm(
        text='Would you like to play again?', title='Network Protocol Game', buttons=['Throw', 'Cancel'])
    if temp == 'Cancel':
        break
