from typing import Text
import pyautogui

# enter password gui
# pyautogui.password(text='enter your password',title='password', default='', mask='*')

# paramters are the definition on top of the entry bar, the actual name of program and the default values
pyautogui.prompt(text='enter your password', title='--', default='!')
