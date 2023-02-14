import pyautogui
from time import sleep

no_monsters = 'imagens/monstros/lista.png'
positions = [[809, 314], [873, 314], [938, 314],
             [874, 444], [807, 444], [809, 372],
             [938, 380], [938, 444]]


def lt():
    while 1:
        print("\033[01;32mComeçou lootear\033[0m")
        for i in positions:
            pyautogui.rightClick(x=i[0], y=i[1])
            print("\033[01;32mLoot feito\033[0m")
            sleep(0.5)
        break
