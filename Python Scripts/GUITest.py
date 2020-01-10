import tkinter as tk
from random import randint
from win32api import GetSystemMetrics

def Movewindow():
    windowX = randint(0, GetSystemMetrics(0) - window.winfo_width())
    windowY = randint(0, GetSystemMetrics(1) - window.winfo_height())
    window.geometry('+%d+%d'%(windowX, windowY))

window = tk.Tk()
window.title("Can\'t catch me!")
button = tk.Button(window, text='Click!', width=50, height=10, command=Movewindow)
button.pack()

window.mainloop()

