from typing import Text
import pyautogui

# enter password gui
# pyautogui.password(text='enter your password',title='password', default='', mask='*')


pyautogui.prompt(text='enter your password', title='--', default='!')
