import os
import pyautogui
import time

for trys in range(3):

    n = str(input("Name : "))

    p = str(input("Paswort : "))


    if n == "LeNaru"and p == "ghg":
        os.system("cls")
        print("Logt in !")
        break
    else:
        time.sleep(3)
        os.system("cls")
        print("login failed!")

    time.sleep(2)
    print("more luck next time :D")
    time.sleep(3)
    pyautogui.press("ALT", "F4")

