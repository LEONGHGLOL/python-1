import os
import time
import pyautogui

n = str(input("Name : "))

p = str(input("Paswort : "))


if n == "LeNaru"and p == "ghg":
    os.system("cls")
    print("Logt in !")

    time.sleep(5)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep("1")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    os.system("cls")
    time.sleep(2)
    print("goodbye")
    time.sleep(3)
    pyautogui.hotkey("ALT", "F4")