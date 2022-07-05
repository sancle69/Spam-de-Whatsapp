# importante no olviden instalar el paquete de pyautogui o no les va a servir el codigo
from unittest import addModuleCleanup
import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=AQUIVAELNUMERO')
sleep(10)

with open ("spam.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
