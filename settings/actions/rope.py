import pyautogui
import time


def corda():
    while True:
        if pyautogui.locateOnScreen("icon_mark6.png", confidence=0.9, region=(1750, 26, 112, 113)):
            print("\033[01;32mRegião de subida encontrada!!\033[0m")
            time.sleep(1)
            pyautogui.moveTo(1750, 26) 
            pyautogui.press("F12")
            pyautogui.leftClick(x="876", y="382")
        else:
            pass
