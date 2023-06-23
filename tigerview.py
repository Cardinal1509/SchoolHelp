import webbrowser
import time
import pyautogui, sys
def tigerview():
  webbrowser.open('https://tigerview.ecusd7.org/')
  time.sleep(3)
  pyautogui.moveTo(950, 840)
  pyautogui.scroll(-1000)
  time.sleep(.5)
  pyautogui.moveTo(950, 840)
  pyautogui.click()
tigerview()