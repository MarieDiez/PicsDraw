﻿"""BIBLIOTHEQUE"""
from tkinter import*
from PIL import Image, ImageTk,ImageGrab

"""DUBUT PROGRAMME"""
#FENETRE
fenetre=Tk()
fenetre.geometry("1200x600")
fenetre.title("Paint")
Fond = Canvas(fenetre,width=1200,height=600,bg="gainsboro")
Fond.grid()

#VAIRABLE GLOBAL
global Candessin1,x,cann1,Cann2,Cann3,Cann33,Cann333,Cann44,Cann55,Cann66,Cann77,Cann88,Cannn1,Cannn2,Cannn3,Cann33,Cannn33,Cannn333,Cannn44,Cannn55,Cannn66,Cannn77,Cannn88

#CREATION DES CANEVAS PRINCIPAUX AFFICHAGE
Candessin=Canvas(fenetre,width=800,height=500,bg="black")
Candessin.place(x=200,y=50)
Candessin1=Canvas(fenetre,width=790,height=490,bg="white")
Candessin1.place(x=205,y=55)


#INITIALISATION VARIABLE DE DEPART
Candessin1.img=PhotoImage()
b1 = "up"
xold, yold = None,None # pas de valeurs
police="arial"
u="black"
w=1
##initialisation image pour gomme-crayon
Fich1=PhotoImage(file="1.gif")
Fich2=PhotoImage(file="2.gif")
Fich3=PhotoImage(file="3.gif")
Fich4=PhotoImage(file="4.gif")
Fich5=PhotoImage(file="5.gif")
Fich6=PhotoImage(file="Fich6.gif")

#CANEVAS
##creation canvas gomme-crayon
Can4 = Canvas(fenetre,width=45,height=45)
Can4.create_image(0,0,image=Fich1,anchor='nw')
Can4.place(x=10,y=290)
Can5 = Canvas(fenetre,width=45,height=45)
Can5.create_image(0,0,image=Fich2,anchor='nw')
Can5.place(x=10,y=350)
Can6 = Canvas(fenetre,width=45,height=45)
Can6.create_image(0,0,image=Fich3,anchor='nw')
Can6.place(x=10,y=410)
Can7 = Canvas(fenetre,width=45,height=45)
Can7.create_image(0,0,image=Fich4,anchor='nw')
Can7.place(x=10,y=470)
Can3333 = Canvas(fenetre,width=45,height=45)
Can3333.create_image(0,0,image=Fich5,anchor='nw')
Can3333.place(x=10,y=230)
Cany = Canvas(fenetre,width=45,height=45)
Cany.create_image(0,0,image=Fich6,anchor='nw')
Cany.place(x=10,y=535)

##Canvas avec les couleurs de base possibles
Can1 = Canvas(fenetre,width=20,height=20,bg="RED")
Can1.place(x=10,y=50)
Can2 = Canvas(fenetre,width=20,height=20,bg="Blue")
Can2.place(x=10,y=80)
Can3 = Canvas(fenetre,width=20,height=20,bg="green")
Can3.place(x=10,y=110)
Can33 = Canvas(fenetre,width=20,height=20,bg="white")
Can33.place(x=10,y=140)
Can333 = Canvas(fenetre,width=20,height=20,bg="black")
Can333.place(x=10,y=170)
Can44 = Canvas(fenetre,width=20,height=20,bg="orange")
Can44.place(x=35,y=50)
Can55 = Canvas(fenetre,width=20,height=20,bg="yellow")
Can55.place(x=35,y=80)
Can66 = Canvas(fenetre,width=20,height=20,bg="purple")
Can66.place(x=35,y=110)
Can77 = Canvas(fenetre,width=20,height=20,bg="brown")
Can77.place(x=35,y=140)
Can88 = Canvas(fenetre,width=20,height=20,bg="thistle")
Can88.place(x=35,y=170)

##creation canevas por couleurs supplementaires
Cann1 = Canvas(fenetre,width=20,height=20,bg="deep sky blue")
Cann2 = Canvas(fenetre,width=20,height=20,bg="cyan")
Cann3 = Canvas(fenetre,width=20,height=20,bg="blueviolet")
Cann33 = Canvas(fenetre,width=20,height=20,bg="lavender")
Cann333 = Canvas(fenetre,width=20,height=20,bg="turquoise")
Cann44 = Canvas(fenetre,width=20,height=20,bg="sandybrown")
Cann55 = Canvas(fenetre,width=20,height=20,bg="lightpink")
Cann66 = Canvas(fenetre,width=20,height=20,bg="lemonchiffon")
Cann77 = Canvas(fenetre,width=20,height=20,bg="tomato")
Cann88 = Canvas(fenetre,width=20,height=20,bg="coral")
Cannn1 = Canvas(fenetre,width=20,height=20,bg="indianred")
Cannn2 = Canvas(fenetre,width=20,height=20,bg="tan")
Cannn3 = Canvas(fenetre,width=20,height=20,bg="mediumblue")
Cannn33 = Canvas(fenetre,width=20,height=20,bg="lightskyblue")
Cannn333 = Canvas(fenetre,width=20,height=20,bg="lightsteelblue")
Cannn44 = Canvas(fenetre,width=20,height=20,bg="palegreen")
Cannn55 = Canvas(fenetre,width=20,height=20,bg="darkgrey")
Cannn66 = Canvas(fenetre,width=20,height=20,bg="orangered")
Cannn77 = Canvas(fenetre,width=20,height=20,bg="lightgray")
Cannn88 = Canvas(fenetre,width=20,height=20,bg="beige")

##creation des canvas pour si clic rouge texte
poli = Canvas(fenetre,width=5,height=5,bg="gainsboro")
poli.place(x=1115,y=298)
poli['highlightthickness']=0
poli1 = Canvas(fenetre,width=5,height=5,bg="gainsboro")
poli1.place(x=1115,y=350)
poli1['highlightthickness']=0
poli2 = Canvas(fenetre,width=5,height=5,bg="gainsboro")
poli2.place(x=1115,y=410)
poli2['highlightthickness']=0


#TEXTE
##Affichage paramete texte
txt=Label(fenetre, text="Texte :",bg="gainsboro")
txt.place(x=1030,y=50)
nom1= StringVar()
saisie1= Entry(textvariable = nom1, width=15)
saisie1.place(x= 1075,y=50)
txt=Label(fenetre, text="x =",bg="gainsboro")
txt.place(x=1032,y=90)
nom2= StringVar()
saisie2= Entry(textvariable = nom2, width=5)
saisie2.place(x=1060,y=90)
txt=Label(fenetre, text="y =",bg="gainsboro")
txt.place(x=1032,y=120)
nom3= StringVar()
saisie3= Entry(textvariable = nom3, width=5)
saisie3.place(x= 1060,y=120)

#TEXTE-Choix police
##Arial
C=Canvas(fenetre,width=100,height=20,bg="gainsboro")
C.place(x=1020,y=290)
texte=C.create_text(10,10,text="Arial",font="Arial", fill="black")
C.coords(texte, 20,10)
C['highlightthickness']=0
##ITALIC
C1=Canvas(fenetre,width=100,height=20,bg="gainsboro")
C1.place(x=1020,y=350)
texte=C1.create_text(1,1,text="Italic",font="President 18 italic", fill="black")
C1.coords(texte, 25,10)
C1['highlightthickness']=0
##GRAS
C2=Canvas(fenetre,width=100,height=20,bg="gainsboro")
C2.place(x=1020,y=410)
texte=C2.create_text(1,1,text="Gras",font="Verdana 14 bold", fill="black")
C2.coords(texte, 25,10)
C2['highlightthickness']=0

#COORDONNEES
## Horizontale
txt=Label(fenetre, text="0|",bg="gainsboro")
txt.place(x=200,y=29)
txt=Label(fenetre, text="100|",bg="gainsboro")
txt.place(x=300,y=29)
txt=Label(fenetre, text="200|",bg="gainsboro")
txt.place(x=400,y=29)
txt=Label(fenetre, text="300|",bg="gainsboro")
txt.place(x=500,y=29)
txt=Label(fenetre, text="400|",bg="gainsboro")
txt.place(x=600,y=29)
txt=Label(fenetre, text="500|",bg="gainsboro")
txt.place(x=700,y=29)
txt=Label(fenetre, text="600|",bg="gainsboro")
txt.place(x=800,y=29)
txt=Label(fenetre, text="700|",bg="gainsboro")
txt.place(x=900,y=29)
txt=Label(fenetre, text="780|",bg="gainsboro")
txt.place(x=980,y=29)

##Vertical
txt=Label(fenetre, text="0-",bg="gainsboro")
txt.place(x=180,y=41)
txt=Label(fenetre, text="100-",bg="gainsboro")
txt.place(x=172,y=139)
txt=Label(fenetre, text="200-",bg="gainsboro")
txt.place(x=172,y=239)
txt=Label(fenetre, text="300-",bg="gainsboro")
txt.place(x=172,y=339)
txt=Label(fenetre, text="400-",bg="gainsboro")
txt.place(x=172,y=439)
txt=Label(fenetre, text="500-",bg="gainsboro")
txt.place(x=172,y=539)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""Fonction"""
#ouvrir image
def ouvrir():
    global Cn,Im
    global Candessin1,Im,fichier
    fichier=str()
    fichier=askopenfilename()
    Im=Image.open(fichier)
    Cn=Im.resize((790,490))
    Candessin1.image=ImageTk.PhotoImage(Cn)
    Candessin1.create_image(0,0,image=Candessin1.image,anchor='nw')

#sauvegarder image
def save():
    New=Image.open(fichier)
    data= list(New.getdata())
    mdata=[]
    i=0
    while i <= len(data)-1:
       R= data[i][0]
       V= data[i][1]
       B= data[i][2]
       mdata.append((R,V,B))
       i=i+1

    imNew= Image.new(New.mode,New.size)
    imNew.putdata(mdata)
    png=options={}
    options['defaultextension']='.png'
    save=asksaveasfile('w',**png)
    imNew.save(save.name)
    askokcancel("Sauver dans",save)





#effacer canevas
def eff():
    Candessin1.delete(ALL)

#police ariane
def ariane():
    global police
    police="Arial"
    poli = Canvas(fenetre,width=5,height=5,bg="red")
    poli.place(x=1115,y=298)
    poli2 = Canvas(fenetre,width=10,height=10,bg="gainsboro")
    poli2.place(x=1115,y=358)
    poli2['highlightthickness']=0
    poli3 = Canvas(fenetre,width=10,height=10,bg="gainsboro")
    poli3.place(x=1115,y=418)
    poli3['highlightthickness']=0

#police italic
def italic():
    global police
    police="President 18 italic"
    poli = Canvas(fenetre,width=10,height=10,bg="gainsboro")
    poli.place(x=1115,y=298)
    poli['highlightthickness']=0
    poli1 = Canvas(fenetre,width=5,height=5,bg="red")
    poli1.place(x=1115,y=358)
    poli2 = Canvas(fenetre,width=10,height=10,bg="gainsboro")
    poli2.place(x=1115,y=418)
    poli2['highlightthickness']=0

#police gras
def gras():
    global police
    police="Verdana 14 bold"
    poli = Canvas(fenetre,width=10,height=10,bg="gainsboro")
    poli.place(x=1115,y=298)
    poli['highlightthickness']=0
    poli2 = Canvas(fenetre,width=10,height=10,bg="gainsboro")
    poli2.place(x=1115,y=358)
    poli2['highlightthickness']=0
    poli3 = Canvas(fenetre,width=5,height=5,bg="red")
    poli3.place(x=1115,y=418)

"""
def plus():
    global t,t1
    t=t+10
    t1=t1+10
    print(t,t1)

def moins():
    global t,t1
    t=t-10
    t1=t1-10
    print(t,t1)"""

#Texte
## Horizontal
def texte():
    global texte
    A=(saisie1.get())
    B=int(saisie2.get())
    C=int(saisie3.get())
    cox=B
    coy=C
    texte=Candessin1.create_text(10,10,width=0,text=A,font=police, fill=u)
    Candessin1.coords(texte, cox,coy)

##Vertical
def vert():
    global texte1
    A=(saisie1.get())
    B=int(saisie2.get())
    C=int(saisie3.get())
    cox=B
    coy=C
    texte1=Candessin1.create_text(10,10,width=10,text=A,font=police, fill=u)
    Candessin1.coords(texte1, cox,coy)

#Efface dernier texte
##horizontal
def efftexteH():
        Candessin1.delete(texte)

## Vertical
def efftexteV():
    Candessin1.delete(texte1)

#Affichage Couleur
def clic1(evt) :
 global u,w,Candessin1,x
 if evt.widget==Can1 :
    u="red"
    Can1['highlightthickness']=4
    Can2['highlightthickness']=2
    Can3['highlightthickness']=2
    Can33['highlightthickness']=2
    Can333['highlightthickness']=2
    Can44['highlightthickness']=2
    Can77['highlightthickness']=2
    Can88['highlightthickness']=2
    Cann1['highlightthickness']=2
    Cann2['highlightthickness']=2
    Cann3['highlightthickness']=2
    Cann33['highlightthickness']=2
    Cann333['highlightthickness']=2
    Cann44['highlightthickness']=2
    Cann55['highlightthickness']=2
    Cann66['highlightthickness']=2
    Can55['highlightthickness']=2
    Cann77['highlightthickness']=2
    Cannn1['highlightthickness']=2
    Cannn2['highlightthickness']=2
    Cann88['highlightthickness']=2
    Cannn3['highlightthickness']=2
    Cannn33['highlightthickness']=2
    Cannn333['highlightthickness']=2
    Cannn44['highlightthickness']=2
    Can66['highlightthickness']=2
    Cannn55['highlightthickness']=2
    Cannn66['highlightthickness']=2
    Cannn77['highlightthickness']=2
    Cannn88['highlightthickness']=2

 if evt.widget==Can2 :
        u="Blue"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=4
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can77['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Can55['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Can66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2


 if evt.widget==Can3 :
        u="green"
        Can1['highlightthickness']=2
        Can55['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=4
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can77['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cann88['highlightthickness']=2
        Can66['highlightthickness']=2
        Cannn88['highlightthickness']=2
 if evt.widget==Can33 :
        u="white"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=4
        Can333['highlightthickness']=2
        Can66['highlightthickness']=2
        Can44['highlightthickness']=2
        Can77['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Can55['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Can333 :
        u="black"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=4
        Can44['highlightthickness']=2
        Can77['highlightthickness']=2
        Can88['highlightthickness']=2
        Can55['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Can66['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2


 if evt.widget==Can44 :
        u="orange"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=4
        Can77['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Can55['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Can66['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Can77 :
        u="brown"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=4
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Can66['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Can55 :
        u="yellow"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=4
        Can66['highlightthickness']=2
        Can77['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Can66 :
        u="purple"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=4
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Can88 :
        u="thistle"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=4
        Cann1['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann1 :
        u="deep sky blue"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=4
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann2 :
        u="cyan"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=4
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann3 :
        u="blueviolet"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=4
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann33 :
        u="lavender"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=4
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann333 :
        u="turquoise"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=4
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann44:
        u="sandybrown"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=4
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann55 :
        u="lightpink"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=4
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann66 :
        u="lemonchiffon"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=4
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann77 :
        u="tomato"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=4
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cann88 :
        u="coral"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=4
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn1 :
        u="indianred"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=4
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn2 :
        u="tan"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=4
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn3 :
        u="mediumblue"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=4
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn33 :
        u="lightskyblue"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=4
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn333 :
        u="lightsteelblue"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=4
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn44 :
        u="palegreen"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=4
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn55 :
        u="darkgrey"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=4
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn66 :
        u="orangered"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=4
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn77 :
        u="lightgray"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=4
        Cannn88['highlightthickness']=2

 if evt.widget==Cannn88 :
        u="beige"
        Can1['highlightthickness']=2
        Can2['highlightthickness']=2
        Can3['highlightthickness']=2
        Can33['highlightthickness']=2
        Can333['highlightthickness']=2
        Can44['highlightthickness']=2
        Can55['highlightthickness']=2
        Can77['highlightthickness']=2
        Can66['highlightthickness']=2
        Can88['highlightthickness']=2
        Cann1['highlightthickness']=2
        Cann2['highlightthickness']=2
        Cann3['highlightthickness']=2
        Cann33['highlightthickness']=2
        Cann333['highlightthickness']=2
        Cann44['highlightthickness']=2
        Cann55['highlightthickness']=2
        Cann66['highlightthickness']=2
        Cann77['highlightthickness']=2
        Cann88['highlightthickness']=2
        Cannn1['highlightthickness']=2
        Cannn2['highlightthickness']=2
        Cannn3['highlightthickness']=2
        Cannn33['highlightthickness']=2
        Cannn333['highlightthickness']=2
        Cannn44['highlightthickness']=2
        Cannn55['highlightthickness']=2
        Cannn66['highlightthickness']=2
        Cannn77['highlightthickness']=2
        Cannn88['highlightthickness']=4

 ##cree fond de la couleur choisit
 if evt.widget==Cany:
    Candessin1.create_line(0,2000,0,0,fill=u,width=10000)


#Condition activation gomme-crayon
 if evt.widget==Can3333 :
        u="white"
        Can3333['highlightthickness']=5
        Can4['highlightthickness']=2
        Can5['highlightthickness']=2
        Can6['highlightthickness']=2
        Can7['highlightthickness']=2


 if evt.widget==Can4:
        w=1
        Can4['highlightthickness']=5
        Can5['highlightthickness']=2
        Can6['highlightthickness']=2
        Can3333['highlightthickness']=2
        Can7['highlightthickness']=2

 if evt.widget==Can5 :
        w=3
        Can4['highlightthickness']=2
        Can5['highlightthickness']=5
        Can6['highlightthickness']=2
        Can7['highlightthickness']=2
        Can3333['highlightthickness']=2

 if evt.widget==Can6 :
        w=5
        Can4['highlightthickness']=2
        Can5['highlightthickness']=2
        Can6['highlightthickness']=5
        Can3333['highlightthickness']=2
        Can7['highlightthickness']=2

 if evt.widget==Can7 :
        w=10
        Can3333['highlightthickness']=2
        Can4['highlightthickness']=2
        Can5['highlightthickness']=2
        Can6['highlightthickness']=2
        Can7['highlightthickness']=5


#clic sur souris
def b1down(evt):
        global b1
        b1 = "down"

#Clic laché
def b1up(evt):
        global b1, xold, yold
        b1 = "up"
        xold = None          #reecrit pas de valeur
        yold = None

#mouvement souris
def motion(evt):
        if b1 == "down":
            global xold, yold
            if xold != None and yold != None: #si c = c que c up
                evt.widget.create_line(xold,yold,evt.x,evt.y,fill=u,width=w)
            xold = evt.x
            yold = evt.y

#Ouverture Couleur supplementaire
def coul():
        global Cann1,Cann2,Cann3,Cann33,Cann333,Cann44,Cann55,Cann66,Cann77,Cann88,Cannn1,Cannn2,Cannn3,Cann33,Cannn33,Cannn333,Cannn44,Cannn55,Cannn66,Cannn77,Cannn88
        cann = Canvas(fenetre,width=95,height=320,bg="white")
        cann.place(x=70,y=10)
        Cann1 = Canvas(fenetre,width=20,height=20,bg="deep sky blue")
        Cann1.place(x=80,y=30)
        Cann2 = Canvas(fenetre,width=20,height=20,bg="cyan")
        Cann2.place(x=80,y=60)
        Cann3 = Canvas(fenetre,width=20,height=20,bg="blueviolet")
        Cann3.place(x=80,y=90)
        Cann33 = Canvas(fenetre,width=20,height=20,bg="lavender")
        Cann33.place(x=80,y=120)
        Cann333 = Canvas(fenetre,width=20,height=20,bg="turquoise")
        Cann333.place(x=80,y=150)
        Cann44 = Canvas(fenetre,width=20,height=20,bg="sandybrown")
        Cann44.place(x=80,y=180)
        Cann55 = Canvas(fenetre,width=20,height=20,bg="lightpink")
        Cann55.place(x=80,y=210)
        Cann66 = Canvas(fenetre,width=20,height=20,bg="lemonchiffon")
        Cann66.place(x=80,y=240)
        Cann77 = Canvas(fenetre,width=20,height=20,bg="tomato")
        Cann77.place(x=80,y=270)
        Cann88 = Canvas(fenetre,width=20,height=20,bg="coral")
        Cann88.place(x=80,y=300)
        Cannn1 = Canvas(fenetre,width=20,height=20,bg="indianred")
        Cannn1.place(x=115,y=30)
        Cannn2 = Canvas(fenetre,width=20,height=20,bg="tan")
        Cannn2.place(x=115,y=60)
        Cannn3 = Canvas(fenetre,width=20,height=20,bg="mediumblue")
        Cannn3.place(x=115,y=90)
        Cannn33 = Canvas(fenetre,width=20,height=20,bg="lightskyblue")
        Cannn33.place(x=115,y=120)
        Cannn333 = Canvas(fenetre,width=20,height=20,bg="lightsteelblue")
        Cannn333.place(x=115,y=150)
        Cannn44 = Canvas(fenetre,width=20,height=20,bg="palegreen")
        Cannn44.place(x=115,y=180)
        Cannn55 = Canvas(fenetre,width=20,height=20,bg="darkgrey")
        Cannn55.place(x=115,y=210)
        Cannn66 = Canvas(fenetre,width=20,height=20,bg="orangered")
        Cannn66.place(x=115,y=240)
        Cannn77 = Canvas(fenetre,width=20,height=20,bg="lightgray")
        Cannn77.place(x=115,y=270)
        Cannn88 = Canvas(fenetre,width=20,height=20,bg="beige")
        Cannn88.place(x=115,y=300)
        button1= Button(fenetre, text="X",command=clear)
        button1.place(x=150,y=10)

#Ferme les choix des couleurs supplementaire
def clear():
    Canh = Canvas(fenetre,width=100,height=330,bg="gainsboro")
    Canh.place(x=70,y=10)
    Canh['highlightthickness']=0

#Efface donne pour le texte
def ef():
    saisie1.delete(0,END)
    saisie2.delete(0,END)
    saisie3.delete(0,END)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""Menu-Barre"""
# Creation barre-Menu
menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Ouvrir",command=ouvrir)
menu1.add_separator()
menu1.add_command(label="Enregister image",command=save)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Effacer",command=eff)
menubar.add_cascade(label="Effacer", menu=menu2)
fenetre.config(menu=menubar)

"""Activation fonction"""
#changer de couleur et taille crayon
if'<ButtonPress-1>':
    fenetre.bind('<ButtonPress-1>',clic1)

#la fonction principale
Candessin1.bind("<Motion>", motion)
Candessin1.bind("<ButtonPress-1>", b1down)
Candessin1.bind("<ButtonRelease-1>", b1up)


"""Bouttons"""
#couleur supp
button= Button(fenetre, text=" >> ",command=coul)
button.place(x=5,y=10)

#texte
B=Button(fenetre, text=" texte horizontal ",command=texte)
B.place(x=1010,y=170)
B=Button(fenetre, text="Annuler texte",command=efftexteH)
B.place(x=1010,y=220)
B=Button(fenetre, text="Annuler texte",command=efftexteV)
B.place(x=1115,y=220)
button11= Button(fenetre, text="✓",command=ariane)
button11.place(x=1080,y=290)
button12= Button(fenetre, text="✓",command=italic)
button12.place(x=1080,y=350)
button13= Button(fenetre, text="✓",command=gras)
button13.place(x=1080,y=410)
button16= Button(fenetre, text="texte vertical",command=vert)
button16.place(x=1120,y=170)
button17= Button(fenetre, text="X",command=ef)
button17.place(x=1169,y=50)



fenetre.mainloop()

