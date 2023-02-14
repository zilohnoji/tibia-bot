import threading
import pyautogui as gui
import settings.actions.attack as at
import settings.actions.loot as lt
from settings.actions.food import comer
from settings.actions.healer import healing
from settings.actions.rope import corda
from settings.actions.train import treinarmp
from settings.configss import find_zones

gui.FAILSAFE = False
monstro = 'imagens/monstros/atacando.png'
list = 'imagens/monstros/lista.png'


def walk() -> None:
    cura_thread = threading.Thread(target=healing, args=())
    comer_thread = threading.Thread(target=comer, args=())   
    treinar_thread = threading.Thread(target=treinarmp, args=())
    corda_thread = threading.Thread(target=corda, args=())
    cura_thread.start()
    comer_thread.start()
    treinar_thread.start()
    corda_thread.start()

    while 1:
        find_zones("mark1", "\033[01;31m", at, lt)
        find_zones("mark2", "\033[01;34m", at, lt)
        find_zones("mark3", "\033[01;34m", at, lt)
        find_zones("mark4", "\033[01;34m", at, lt)
        find_zones("mark5", "\033[01;34m", at, lt)
        find_zones("mark6", "\033[01;31m", at, lt)


walk()
