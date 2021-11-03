import pyautogui
# this is where the gui starts to appear


pyautogui.alert('This displays some text with an OK button.')

# cancel string if cancel is clicked, ok string if ok is clicked
# print(pyautogui.confirm('This displays text and has an OK and Cancel button.'))


# is this consider programming? to use the function, someone could literally type their birthday date here in string literals
#print(pyautogui.prompt('Type Yes and click ok'))


# to make this 3 functions into a game? does it takes imagination?
# With everything i've learned from 30-35?


pyautogui.FAILSAFE = True

while(True):
    temp = pyautogui.prompt('To play again, type Yes and click ok')
    if temp == 'Yes':
        print('Smart')

    else:
        print('Dumb')
        break
