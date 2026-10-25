
import os
import customtkinter

def startApp(appName):
    os.system(f"start {appName}")

app= customtkinter.CTk()
app.geometry("800x500")
app.title("W")
label = customtkinter.CTkLabel(app, text="App starter", fg_color="transparent")
label.pack(padx=20, pady=20)
button = customtkinter.CTkButton(app, text="spotify", command=lambda: startApp("spotify"))
button.pack(padx=20, pady=20)

button = customtkinter.CTkButton(app, text="VS code", command=lambda: startApp("code"))
button.pack(padx=20, pady=20)

button = customtkinter.CTkButton(app, text="Discord", command=lambda: startApp("discord"))
button.pack(padx=20, pady=20)

button = customtkinter.CTkButton(app, text="IntelliJ IDEA", command=lambda: startApp("Intelij"))
button.pack(padx=20, pady=20)

button = customtkinter.CTkButton(app, text="Roblox", command=lambda: startApp("roblox"))
button.pack(padx=20, pady=20)

button = customtkinter.CTkButton(app, text="Google", command=lambda: startApp("Google Chrome"))
button.pack(padx=20, pady=20)

button = customtkinter.CTkButton(app, text="Medal", command=lambda: startApp("Medal.tv"))
button.pack(padx=20, pady=20)
app.mainloop()

