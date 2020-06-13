import time
import pyautogui
from pynput.keyboard import Controller


def walk(keys):
    keyboard = Controller()
    left = keys['left']
    right = keys['right']

    for i in range(2):
        key = left if i == 0 else right
        keyboard.press(key)
        time.sleep(0.25)
        keyboard.release(key)
        time.sleep(0.5)


def attack(keys):
    keyboard = Controller()
    a = keys['a']

    keyboard.press(a)
    time.sleep(0.5)
    keyboard.release(a)
    time.sleep(0.5)


grass_picture = 'images/grass.png'
battle_picture = 'images/hp.png'

key_binds = {'left': 'a', 'right': 'd', 'a': 'e', 'b': 'f'}

time.sleep(2)
print('starting...')
while True:
    # Locate grass texture on screen
    if pyautogui.locateOnScreen(grass_picture, grayscale=True, confidence=0.8):
        walk(key_binds)

    elif pyautogui.locateOnScreen(battle_picture, grayscale=True, confidence=0.8):
        attack(key_binds)

    else:
        print('none')




