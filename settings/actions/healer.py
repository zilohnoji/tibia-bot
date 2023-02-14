import pyautogui
import time


def healing():
    imagem = 'imagens/condicoes/heal_life.png'

    while 1:
        if pyautogui.locateOnScreen(imagem, confidence=0.9, region=(1836, 141, 15, 14)):
        # if pyautogui.locateOnScreen(imagem, confidence=0.9, region=(1836,141,15,14)): 1920 x 1080
            time.sleep(1)
        else:
            print('\033[01;31mVida Baixa\033[0m')
            pyautogui.press('F1')
            time.sleep(1.2)
