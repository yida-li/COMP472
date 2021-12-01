import pyautogui

answer = pyautogui.confirm('Enter option Gfg', buttons =['choice a', 'choice b', 'choice c','choice d'])

print('you answered',answer)