import pyautogui

# move mouse relative to a position
# cuz it could be anywhere
pyautogui.moveRel(500, 199, duration=3)

# drag mouse to that place
pyautogui.dragTo(199, 500, duration=6)
