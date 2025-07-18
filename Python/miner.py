import pyautogui
import time
import os
import copilot
from PIL import Image

pyautogui.hotkey('ctrl', 'win', 'right')
time.sleep(1)
location = copilot.finder('mp.png')
pyautogui.moveTo(location)
location = copilot.finder('rhino.png')

x = input(int())
time.sleep(3)
while True:
    pyautogui.moveTo(location)
    pyautogui.click()
    x+=1
    print(x)
    botchecker = copilot.botid()
    if botchecker > 0.90:
        pyautogui.hotkey('ctrl', 'win', 'right')

        pause = input()
        pyautogui.hotkey('ctrl', 'win', 'right')
        time.sleep(1)
        square = copilot.botkiller()
        pyautogui.moveTo(square)

    time.sleep(x)

