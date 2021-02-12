'''
Simple pyautogui test.

'''
import pyautogui
#2.5 second pause after each call
pyautogui.PAUSE = 2.5

#move mouse to upper left will stop program
pyautogui.FAILSAFE = True


screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
