import pyautogui
import time


def treinarmp():
    mana_cheia = 'imagens/condicoes/mana_full.png'
    while 1:
        if pyautogui.locateOnScreen(mana_cheia, confidence=0.9):
            pyautogui.press('F1')
            time.sleep(1.5)
        else:
            print('\033[01;31mMana Vazia\033[0m')
            time.sleep(8)
