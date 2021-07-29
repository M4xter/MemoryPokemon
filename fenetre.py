from tkinter import *
from random import randrange

COTE=120
PAD=5
SIDE=COTE+2+PAD

NB_LIG=4
NB_COL=5

LARG=NB_COL*SIDE
HAUT=NB_LIG*SIDE

memory = Tk()
# dans le tuto

cnv = Canvas(memory, width=630, height=500, background="grey")
cnv.pack()

logo = PhotoImage(file = "images\\cover.gif")
X0=Y0=SIDE/2

for lig in range(NB_LIG):
    for col in range(NB_COL):
        centre=(col*SIDE+X0,lig*SIDE+Y0)
        cnv.create_image(centre, image=logo)

memory.mainloop()