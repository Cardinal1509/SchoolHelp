import keyboard
import os
import webbrowser
import time
import pyautogui

with open('SchoologyUsername.txt', 'r') as file:
    SchoologyUsername = file.read().rstrip()
with open('SchoologyPassword.txt', 'r') as file:
    SchoologyPassword = file.read().rstrip()
def schoology():
  webbrowser.open('https://ecusd7.schoology.com/login/ldap?&school=1126349310')
  time.sleep(3)
  pyautogui.moveTo(775, 645)
  pyautogui.click()
def schoologyauto():
  webbrowser.open('https://ecusd7.schoology.com/login/ldap?&school=1126349310')
  time.sleep(3)
  pyautogui.moveTo(835, 440)
  pyautogui.write(SchoologyUsername)
  time.sleep(.5)
  pyautogui.moveTo(1300, 565)
  pyautogui.click()
  pyautogui.moveTo(770, 505)
  pyautogui.click()
  pyautogui.write(SchoologyPassword)
  time.sleep(.5)
  pyautogui.moveTo(775, 645)
  pyautogui.click()

def clever():
  webbrowser.open('https://clever.com/in/ecusd7')
  time.sleep(3)
  pyautogui.moveTo(800, 540)
  pyautogui.click()
  time.sleep(2)
  pyautogui.moveTo(1300, 565)
  pyautogui.click()

def tigerview():
  webbrowser.open('https://tigerview.ecusd7.org/')
  time.sleep(3)
  pyautogui.moveTo(950, 840)
  pyautogui.scroll(-1000)
  time.sleep(.5)
  pyautogui.moveTo(950, 840)
  pyautogui.click()
with open('V_1.3.0_Update.txt', 'r') as file:
    version = file.read().replace('\n', '')
keyboard.add_hotkey("ctrl+alt+s", lambda: schoology())
keyboard.add_hotkey("ctrl+alt+a", lambda: schoologyauto())
keyboard.add_hotkey("ctrl+shift+h", lambda: commands())
keyboard.add_hotkey("ctrl+alt+c", lambda: clever())
keyboard.add_hotkey("ctrl+alt+t", lambda: tigerview())
keyboard.wait('esc') 
