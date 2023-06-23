import webbrowser
import time
import pyautogui, sys
def clever():
  webbrowser.open('https://clever.com/in/ecusd7')
  time.sleep(3)
  pyautogui.moveTo(800, 540)
  pyautogui.click()
  time.sleep(2)
  pyautogui.moveTo(1300, 565)
  pyautogui.click()
clever()