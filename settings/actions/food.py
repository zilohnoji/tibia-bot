import pyautogui
import time


def comer():
    fome = 'imagens/condicoes/fome.png'
    while 1:
        if pyautogui.locateOnScreen(fome, confidence=0.7):
            print('\033[01;31mFome\033[0m')
            pyautogui.press('F9')
            time.sleep(0.7)
        else:
            time.sleep(10)
