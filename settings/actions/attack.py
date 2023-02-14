import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

monster_atack = 'imagens/monstros/atacando.png'
no_monsters = 'imagens/monstros/lista.png'


def atacar(lt):
    while 1:
        if pyautogui.locateOnScreen(monster_atack, confidence=0.9):
            pass

        elif pyautogui.locateOnScreen(no_monsters, confidence=0.9):
            pass

        else:
            pyautogui.press("esc")
            pyautogui.press("0")
            print("\033[01;31mMonsters Found\033[0m")
            print("\033[01;31mMonster Atack\033[0m")
            if pyautogui.locateOnScreen(no_monsters, confidence=0.9):
                lt.lt()
        break
