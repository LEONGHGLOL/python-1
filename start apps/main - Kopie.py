
import os
import subprocess
import time
import customtkinter

def minecraft():
    os.system("start spotify:")
    print("startet")

def spotify():
    os.system("start spotify")

app= customtkinter.CTk()
app.geometry("800x500")
app.title("W")
label = customtkinter.CTkLabel(app, text="CTkLabel", fg_color="transparent")
label.pack(padx=20, pady=20)
button = customtkinter.CTkButton(app, text="minecraft", command=minecraft)
button.pack(padx=20, pady=20)

button = customtkinter.CTkButton(app, text="spotify", command=spotify)
button.pack(padx=20, pady=20)
app.mainloop()

