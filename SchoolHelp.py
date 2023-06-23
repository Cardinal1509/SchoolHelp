import keyboard
import os
import webbrowser
import time
import pyautogui

keyboard.add_hotkey("ctrl+alt+s", lambda: exec(open("./schoology.py").read()))
keyboard.add_hotkey("ctrl+alt+c", lambda: exec(open("./clever.py").read()))
keyboard.add_hotkey("ctrl+alt+t", lambda: exec(open("./tigerview.py").read()))
keyboard.wait('esc') 
