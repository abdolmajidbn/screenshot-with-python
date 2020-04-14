# pip install pyautogui

import pyautogui

try:
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot2.png") # name and format(only accepts format)
    print("the screenshot saved")
except:
    print("error: please check your codes")