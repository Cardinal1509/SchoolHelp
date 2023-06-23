import webbrowser
import time
import pyautogui, sys
def schoology():
  webbrowser.open('https://ecusd7.schoology.com/login/ldap?&school=1126349310')
  time.sleep(3)
  pyautogui.moveTo(775, 645)
  pyautogui.click()
schoology()