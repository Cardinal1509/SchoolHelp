import keyboard
import os
import webbrowser
import time
import pyautogui

def schoology():
  webbrowser.open('https://ecusd7.schoology.com/login/ldap?&school=1126349310')
  time.sleep(3)
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

keyboard.add_hotkey("ctrl+alt+s", lambda: schoology())
keyboard.add_hotkey("ctrl+alt+c", lambda: clever())
keyboard.add_hotkey("ctrl+alt+t", lambda: tigerview())
keyboard.wait('esc') 
