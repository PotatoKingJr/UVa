import pyautogui, sys
import keyboard
import time
import os

recorded = keyboard.record(until='esc')

os.system('start notepad.exe')

time.sleep(1)
keyboard.play(recorded, speed_factor=10)
