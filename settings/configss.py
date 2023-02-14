import sys
from time import sleep
import pyautogui as gui
from actions.attack import atacar


def find_zones(zona, cor):
    print(f"{cor}Procurando {zona}\033[0m")
    while True:
        try:
            atacar
            if gui.locateOnScreen(f'icon_{zona}.png', confidence=0.7, region=(1800, 71, 15, 15)): 
                print(f"{cor}Região Encontrada [{zona}]\033[0m\n")
                sleep(0.5)
                break
            else:
                gui.locateOnScreen(f'icon_{zona}.png', confidence=0.9, region=(1750, 26, 112, 113)) 
                gui.click(f'icon_{zona}.png')
                sleep(0.3)

        except TypeError:
            sys.stdout.write("\r\033[01;31mPixel fora de visualização\033[0m")
            sys.stdout.flush()
            pass
