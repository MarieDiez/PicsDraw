from tkinter import *

def deplace(evt) :
    global choix, FichCH1, FichCH2, FichCH3
    if 230 <= evt.x <530 :
        if 30 <= evt.y < 180 :
            nouvchoix = 1
        elif 210 <= evt.y < 360 :
            nouvchoix = 2
        elif 390 <= evt.y < 540 :
            nouvchoix = 3
        else :
            nouvchoix = 0
    else :
        nouvchoix = 0
    if choix != nouvchoix :
        if choix == 1 :
            FichCH1=PhotoImage(file="CH1_OFF.gif")
            Fond.itemconfig(CH1,image=FichCH1)
        elif choix == 2 :
            FichCH2=PhotoImage(file="CH2_OFF.gif")
            Fond.itemconfig(CH2,image=FichCH2)
        elif choix == 3 :
            FichCH3=PhotoImage(file="CH3_OFF.gif")
            Fond.itemconfig(CH3,image=FichCH3)
        if nouvchoix == 1 :
            FichCH1=PhotoImage(file="CH1_ON.gif")
            Fond.itemconfig(CH1,image=FichCH1)
        elif nouvchoix == 2 :
            FichCH2=PhotoImage(file="CH2_ON.gif")
            Fond.itemconfig(CH2,image=FichCH2)
        elif nouvchoix == 3 :
            FichCH3=PhotoImage(file="CH3_ON.gif")
            Fond.itemconfig(CH3,image=FichCH3)
    choix = nouvchoix
def nouvfen():
    fen2= Tk()
    text1= Label(fen2,text="Salut")
    text1.pack()
    fen2.mainloop()
    fen2.destroy()

fen1 = Tk()

bouton1 = Button(fen1,text="Nouvelle Fenetre",command=nouvfen)
bouton1.pack()
fen1.mainloop()
fen1.destroy()
def valide(evt) :
    if choix > 0 :
        print ("Vous avez validé le choix",choix)
    else :
        print ("Un peu de concentration !")

fenetre=Tk()

Fond = Canvas(fenetre,width=760,height=570,bg="white")
Fond.grid()

FichFond=PhotoImage(file="menu_fond.gif")
FichCH1=PhotoImage(file="CH1_OFF.gif")
FichCH2=PhotoImage(file="CH2_OFF.gif")
FichCH3=PhotoImage(file="CH3_OFF.gif")

Fond.create_image(0,0,image=FichFond,anchor='nw')
CH1 = Fond.create_image(230,30,image=FichCH1,anchor='nw')
CH2 = Fond.create_image(230,210,image=FichCH2,anchor='nw')
CH3 = Fond.create_image(230,390,image=FichCH3,anchor='nw')

choix = 0

Fond.bind('<Motion>',deplace)
Fond.bind('<ButtonPress-1>',valide)

fenetre.mainloop()