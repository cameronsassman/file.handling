import tkinter as tk
from tkinter import *

window = tk()
idk = Text(window)


def idc():
    k = open('txt.txt', "w+")
    k.write(idk.get('1.0', END))
    k.close()


b = Button(window, text="f,isenfosinfmisenfi", command=idc)

b.pack()
idk.pack()
window.mainloop()
