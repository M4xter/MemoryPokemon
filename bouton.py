from random import randrange
from click import LANG
from tkinter import *

LARG = 600
HAUT = 400

fen=Tk()
cnv=Canvas(fen, width=LARG, height=HAUT, bg="ivory")
cnv.pack(side=LEFT)

logo=PhotoImage(file="aspicot.png")

def show():
    x=randrange(LARG)
    y=randrange(HAUT)
    cnv.create_image((x, y), image=logo)


btn=Button(fen, text="Nouveau", command=show)

btn.pack(padx=10, pady=10)
fen.mainloop()