﻿# Créé par LoïcetMarie, le 19/05/2017 en Python 3.2
# Créé par LoïcetMarie, le 19/05/2017 en Python 3.2

# Créé par abardin, le 12/05/2017 en Python 3.2

from lycee import*
from tkinter import *
from tkinter.filedialog import*
from tkinter.messagebox import *
from PIL import Image, ImageTk, ImageGrab

Fenetre=Tk()
Fenetre.title("PicsDraw")
Fond = Canvas(Fenetre,width=750,height=502,bg="white")
Fond.grid()
Fenetre.protocol("WM_DELETE_WINDOW", Fenetre.destroy)

#INITIALISATION VARIABLE
b1 = "up"
xold, yold = None,None
police="arial"
u="black"
w=1

#Fonction position pour l'activation du choix
def deplace(evt) :
    global choix, nouvchoix, FichCH1, FichCH2

    if 120 <= evt.y < 200:
        if 100 <= evt.x < 300 :
            nouvchoix = 1
        elif 550<= evt.x < 730 :
            nouvchoix = 2
        else :
            nouvchoix = 0
    else :
      nouvchoix = 0

    if choix != nouvchoix :
        if choix == 1 :
            FichCH1=PhotoImage(file="RP_OFF.gif")
            Fond.itemconfig(CH1,image=FichCH1)
        elif choix == 2 :
            FichCH2=PhotoImage(file="D_OFF.gif")
            Fond.itemconfig(CH2,image=FichCH2)

        if nouvchoix == 1 :
            FichCH1=PhotoImage(file="RP_ON.gif")
            Fond.itemconfig(CH1,image=FichCH1)
        elif nouvchoix == 2 :
            FichCH2=PhotoImage(file="D_ON.gif")
            Fond.itemconfig(CH2,image=FichCH2)
    choix = nouvchoix

#Fonction pour ouvrir la fenêtre demandée
def valide(evt) :
    if choix == 1 :
        #FENETRE
        fenetre=Toplevel(Fenetre)
        fenetre.geometry("1200x600")
        fenetre.title("Retouche Photo")
        global Can12
        #CANEVAS
        Fond = Canvas(fenetre,width=1200,height=600,bg="grey")
        Fond.grid()
        Can1 = Canvas(fenetre,width=465,height=465,bg="black")
        Can1.place(x=18,y=48)
        Can2 = Canvas(fenetre,width=465,height=465,bg="black")
        Can2.place(x=489,y=48)
        Can12 = Canvas(fenetre,width=450,height=450,bg="white")
        Can12.place(x=25,y=55)
        Can22 = Canvas(fenetre,width=450,height=450,bg="white")
        Can22.place(x=497,y=55)
        #INITIALISATION VARIABLES
        Can22.img=PhotoImage()


        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        """FONCTIONS"""

        # fonctions
        def save():
            png=options={}
            options['defaultextension']='.png'
            save=asksaveasfile('w',**png)
            imNew2.save(save.name)
            imNew.save(save.name)
            askokcancel("Sauver dans",save)

        def un():
            global fichier
            global Can12
            global img
            fichier=str()
            fichier=askopenfilename()
            askokcancel("Le nom du fichier est",fichier)
            Im=Image.open(fichier)
            img=Im.resize((450,450))
            Can12.image=ImageTk.PhotoImage(img)
            Can12.create_image(0,0,image=Can12.image,anchor='nw')

        def deux():
            global img, img1, img2
            CanA = Canvas(fenetre1,width=225,height=250,bg="white")
            CanB = Canvas(fenetre,width=225,height=250,bg="white")
            CanC = Canvas(fenetre,width=450,height=227,bg="white")
            fichier=str()
            fichier=askopenfilename()
            Im=Image.open(fichier)
            Im=Im.resize((225,250))
            fichier1=askopenfilename()
            im1=Image.open(fichier1)
            im1=im1.resize((225,250))
            fichier2=askopenfilename()
            im2=Image.open(fichier2)
            im2=im2.resize((450,227))
            CanA.image=ImageTk.PhotoImage(Im)
            CanA.create_image(0,0,image=CanA.image,anchor='nw')
            CanA.place(x=25,y=55)
            CanB.image=ImageTk.PhotoImage(im1)
            CanB.create_image(0,0,image=CanB.image,anchor='nw')
            CanB.place(x=250,y=55)
            CanC.image=ImageTk.PhotoImage(im2)
            CanC.create_image(0,0,image=CanC.image,anchor='nw')
            CanC.place(x=25,y=280)


        def photomaton():
            global imNew
            data= list(img.getdata())
            Ldata=[]
            L1data=[]
            x1= img.size[0]
            y1=img.size[1]
            x=0
            y=0
            a=len(data)-1

            while x<=a:
                    if x % 2 ==0:
                       R = data[x][0]
                       V= data[x][1]
                       B= data[x][2]
                       Ldata.append((R,V,B))
                       x=x+1

                    else:
                        R = data[x][0]
                        V= data[x][1]
                        B= data[x][2]
                        R1=R//2+x1//2
                        V1=V//2+x1//2
                        B1=B//2+x1//2
                        x2=((R1,V1,B1))
                        L1data.append(x2)
                        x=x+1
            while y<=a:
                if y % 2 ==0:
                    R = data[y][0]
                    V= data[y][1]
                    B= data[y][2]
                    y3=((R,V,B))
                    Ldata.append(y3)
                    y=y+1

                else:
                    R = data[y][0]
                    V= data[y][1]
                    B= data[y][2]
                    R1=R//2+y1//2
                    V1=V//2 +y1//2
                    B1=B//2 +y1//2
                    y3=((R1,V1,B1))
                    L1data.append(y3)
                    y=y+1

            imNew= Image.new(img.mode,img.size)
            imNew.putdata(Ldata)
            Can22.image=ImageTk.PhotoImage(imNew)
            Can22.create_image(0,0,image=Can22.image,anchor='nw')

        def photomaton2():
            global imNew
            data= list(imNew.getdata())
            Ldata=[]
            L1data=[]
            x1= imNew.size[0]
            y1=imNew.size[1]
            x=0
            y=0
            a=len(data)-1

            while x<=a:
                    if x % 2 ==0:
                       R = data[x][0]
                       V= data[x][1]
                       B= data[x][2]
                       r=R//2
                       v=V//2
                       b=B//2
                       Ldata.append((R,V,B))
                       x=x+1

                    else:
                        R=R//2+x1//2
                        V=V//2+x1//2
                        B=B//2+x1//2
                        x2=((R,V,B))
                        L1data.append(x2)
                        x=x+1
            while y<=a:
                if y % 2 ==0:
                    R = data[y][0]
                    V= data[y][1]
                    B= data[y][2]
                    r=R//2
                    b=B//2
                    v=V//2
                    y3=((R,V,B))
                    Ldata.append(y3)
                    y=y+1

                else:
                    R=R//2+y1//2
                    V=V//2 +y1//2
                    B=B//2 +y1//2
                    y3=((R,V,B))
                    L1data.append(y3)
                    y=y+1

            imNew= Image.new(img.mode,img.size)
            imNew.putdata(Ldata)

            Can22.image=ImageTk.PhotoImage(imNew)
            Can22.create_image(0,0,image=Can22.image,anchor='nw')



        def noiretblanc():
            global imNew2
            img=Image.open(fichier)
            data= list(img.getdata())
            mdata=[]
            i=0
            while i <= len(data)-1:
               R= data[i][0]
               V= data[i][1]
               B= data[i][2]
               M=(R+V+B)/3
               M=int(M)
               mdata.append((M,M,M))
               i=i+1

            imNew= Image.new(img.mode,img.size)
            imNew.putdata(mdata)
            imNew2=imNew.resize((450,450))
            Can22.image=ImageTk.PhotoImage(imNew2)
            Can22.create_image(0,0,image=Can22.image,anchor='nw')


        def HDR():
            img=Image.open(fichier)
            data= list(img.getdata())
            ndata=[]
            i=0
            while i <= len(data)-1: #python commence en 0 donc -1
               R= data[i][0]
               V= data[i][1]
               B= data[i][2]
               R=((R+30)+(R-40)+R)/3
               R=int(R)
               V=((V+30)+(V-40)+V)/3
               V=int(V)
               B=((B+30)+(B-40)+B)/3
               B=int(B)
               M=(R+V+B)
               M=int(M)
               ndata.append((R,V,B))
               i=i+1

            imNew= Image.new(img.mode,img.size)
            imNew.putdata(ndata)
            imNew2=imNew.resize((450,450))
            Can22.image=ImageTk.PhotoImage(imNew2)
            Can22.create_image(0,0,image=Can22.image,anchor='nw')

        def HDR1():
            global imNew
            mdata=[]
            img=Image.open(fichier)
            data= list(img.getdata())
            img1=Image.open(fichier1)
            data1= list(img1.getdata())
            img2=Image.open(fichier2)
            data2= list(img2.getdata())
            i=0
            while i <= len(data)-1: #python commence en 0 donc -1
               R= data[i][0]
               V= data[i][1]
               B= data[i][2]
               R1= data1[i][0]
               V1= data1[i][1]
               B1= data1[i][2]
               R2= data2[i][0]
               V2= data2[i][1]
               B2= data2[i][2]
               R0=(R+R1+R2)/3
               R0=int(R0)
               V0=(V+V1+V2)/3
               V0=int(V0)
               B0=(B+B1+B2)/3
               B0=int(B0)
               mdata.append((R0,V0,B0))
               i=i+1
            imNew= Image.new(img.mode,img.size)
            imNew.putdata(mdata)
            imNew2=imNew.resize((450,450))
            Can22.image=ImageTk.PhotoImage(imNew2)
            Can22.create_image(0,0,image=Can22.image,anchor='nw')

        def negatif():
            img=Image.open(fichier)
            data= list(img.getdata())
            ndata=[]
            i=0
            while i <= len(data)-1:
               R= data[i][0]
               V= data[i][1]
               B= data[i][2]
               ndata.append((255-R,255-V,255-B))
               i=i+1

            imNew= Image.new(img.mode,img.size)
            imNew.putdata(ndata)
            imNew2=imNew.resize((450,450))
            Can22.image=ImageTk.PhotoImage(imNew2)
            Can22.create_image(0,0,image=Can22.image,anchor='nw')

        def rotation180():
            img=Image.open(fichier)
            imNew = img.rotate(180)
            imNew2=imNew.resize((450,450))
            Can22.image=ImageTk.PhotoImage(imNew2)
            Can22.create_image(0,0,image=Can22.image,anchor='nw')

        def rotation90():
            img=Image.open(fichier)
            imNew = img.rotate(-90)
            imNew2=imNew.resize((450,450))
            Can22.image=ImageTk.PhotoImage(imNew2)
            Can22.create_image(0,0,image=Can22.image,anchor='nw')

        def rotationmoins90():
            img=Image.open(fichier)
            imNew = img.rotate(90)
            imNew2=imNew.resize((450,450))
            Can22.image=ImageTk.PhotoImage(imNew2)
            Can22.create_image(0,0,image=Can22.image,anchor='nw')

        def clic(evt):
            global Can, img, Can12
            if evt.widget==button :
                Can = Canvas(fenetre,width=100,height=390,bg="white")
                Can.place(x=1049,y=48)
                txt=Label(fenetre, text="       Raccourcis      ",bg="grey")
                txt.place(x=1050,y=50)
                buttona= Button(fenetre, text=" Rotation 180 ° ",command=rotation180)
                buttona.place(x=1055,y=90)
                Can = Canvas(fenetre,width=100,height=2,bg="grey")
                Can.place(x=1049,y=120)
                buttonb= Button(fenetre, text=" Rotation 90 ° ",command=rotation90)
                buttonb.place(x=1055,y=130)
                Can = Canvas(fenetre,width=100,height=2,bg="grey")
                Can.place(x=1049,y=160)
                buttonc= Button(fenetre, text=" Rotation -90 ° ",command=rotationmoins90)
                buttonc.place(x=1055,y=170)
                Can = Canvas(fenetre,width=100,height=2,bg="grey")
                Can.place(x=1049,y=200)
                buttond= Button(fenetre, text="   Noir et Blanc ",command=noiretblanc)
                buttond.place(x=1055,y=210)
                Can = Canvas(fenetre,width=100,height=2,bg="grey")
                Can.place(x=1049,y=240)
                Can = Canvas(fenetre,width=100,height=2,bg="grey")
                Can.place(x=1049,y=280)
                buttonf= Button(fenetre, text=" Photomaton    ",command=photomaton)
                buttonf.place(x=1055,y=250)
                Can = Canvas(fenetre,width=100,height=2,bg="grey")
                Can.place(x=1049,y=320)
                buttong= Button(fenetre, text=" Photomaton +",command=photomaton2)
                buttong.place(x=1055,y=290)
                Can = Canvas(fenetre,width=100,height=2,bg="grey")
                Can.place(x=1049,y=360)
                buttonh= Button(fenetre, text="     Négatif        ",command=negatif)
                buttonh.place(x=1055,y=330)
                Can = Canvas(fenetre,width=100,height=2,bg="grey")
                Can.place(x=1049,y=400)
                buttonh= Button(fenetre, text="        HDR        ",command=HDR1)
                buttonh.place(x=1055,y=370)
                buttone= Button(fenetre, text=" Tout effacer  ",command=tteff)
                buttone.place(x=1055,y=410)

        def effacer1():
            global Can12
            Can12 = Canvas(fenetre,width=450,height=450,bg="white")
            Can12.place(x=25,y=55)


        def effacer2():
            Can22.delete(ALL)

        def tteff():
            global Can12
            Can12 = Canvas(fenetre,width=450,height=450,bg="white")
            Can22.delete (ALL)
            Can12.place(x=25,y=55)


        def clear():
            Canh = Canvas(fenetre,width=105,height=400,bg="grey")
            Canh.place(x=1049,y=48)
            Canh['highlightthickness']=0


        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        """AFFICHAGE"""
        # TEXTE
        txt=Label(fenetre, text="Image Nomale",bg="grey")
        txt.place(x=156,y=26)
        txt=Label(fenetre, text="Image retouchée",bg="grey")
        txt.place(x=655,y=26)
        txt=Label(fenetre, text="Raccourcis",bg="grey")
        txt.place(x=1010,y=24)

        #BOUTTONS
        button1= Button(fenetre, text="Effacer",command=effacer1)
        button1.place(x=438,y=520)
        button1= Button(fenetre, text="Effacer",command=effacer2)
        button1.place(x=914,y=520)
        button= Button(fenetre, text=" >> ")
        button.place(x=1014,y=48)
        buttonn= Button(fenetre, text=" << ",command=clear)
        buttonn.place(x=1014,y=83)

        #MENU-BAR
        menubar = Menu(fenetre)
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Ouvrir",command=un)
        menu1.add_separator()
        menu1.add_command(label="Ouvrir HDR",command=deux)
        menu1.add_separator()
        menu1.add_command(label="Enregister image",command=save)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=fenetre.destroy)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="rotation 180°",command=rotation180)
        menu2.add_separator()
        menu2.add_command(label="rotation 90°",command=rotation90)
        menu2.add_separator()
        menu2.add_command(label="rotation -90°",command=rotationmoins90)
        menubar.add_cascade(label="Traitement", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="Mode Noir et Blanc", command=noiretblanc)
        menubar.add_cascade(label="Retouche", menu=menu3)
        menu3.add_separator()
        menu3.add_command(label="Mode Négatif", command=negatif)
        menu3.add_separator()
        menu3.add_command(label="Mode Photomaton", command=photomaton)
        menu3.add_separator()
        menu3.add_command(label="Mode Photomaton + ", command=photomaton2)
        menu3.add_separator()
        menu3.add_command(label="HDR", command=HDR1)
        fenetre.config(menu=menubar)

        """CONDITION D'ACTIVATION"""
        #Raccourcis
        if'<ButtonPress-1>':
            fenetre.bind('<ButtonPress-1>',clic)

        Fenetre.mainloop()

    if choix == 2 :
        #FENETRE
        fenetre2=Toplevel(Fenetre)
        fenetre2.geometry("1200x600")
        fenetre2.title("Dessin")
        Fond = Canvas(fenetre2,width=1200,height=600,bg="gainsboro")
        Fond.grid()

        #VAIRABLE GLOBAL
        global Candessin1,x,cann1,Cann2,Cann3,Cann33,Cann333,Cann44,Cann55,Cann66,Cann77,Cann88,Cannn1,Cannn2,Cannn3,Cann33,Cannn33,Cannn333,Cannn44,Cannn55,Cannn66,Cannn77,Cannn88


        #CREATION DES CANEVAS PRINCIPAUX AFFICHAGE
        Candessin=Canvas(fenetre2,width=800,height=500,bg="black")
        Candessin.place(x=200,y=50)
        Candessin1=Canvas(fenetre2,width=790,height=490,bg="white")
        Candessin1.place(x=205,y=55)


        #INITIALISATION VARIABLE DE DEPART
        Candessin1.img=PhotoImage()
        ##initialisation image pour gomme-crayon
        Fich1=PhotoImage(file="1.gif")
        Fich2=PhotoImage(file="2.gif")
        Fich3=PhotoImage(file="3.gif")
        Fich4=PhotoImage(file="4.gif")
        Fich5=PhotoImage(file="5.gif")
        Fich6=PhotoImage(file="Fich6.gif")

        #CANEVAS
        ##creation canvas gomme-crayon

        Can4 = Canvas(fenetre2,width=45,height=45)
        Can4.create_image(0,0,image=Fich1,anchor='nw')
        Can4.place(x=10,y=290)
        Can5 = Canvas(fenetre2,width=45,height=45)
        Can5.create_image(0,0,image=Fich2,anchor='nw')
        Can5.place(x=10,y=350)
        Can6 = Canvas(fenetre2,width=45,height=45)
        Can6.create_image(0,0,image=Fich3,anchor='nw')
        Can6.place(x=10,y=410)
        Can7 = Canvas(fenetre2,width=45,height=45)
        Can7.create_image(0,0,image=Fich4,anchor='nw')
        Can7.place(x=10,y=470)
        Can3333 = Canvas(fenetre2,width=45,height=45)
        Can3333.create_image(0,0,image=Fich5,anchor='nw')
        Can3333.place(x=10,y=230)
        Cany = Canvas(fenetre2,width=45,height=45)
        Cany.create_image(0,0,image=Fich6,anchor='nw')
        Cany.place(x=10,y=535)

        ##Canvas avec les couleurs de base possibles
        Can1 = Canvas(fenetre2,width=20,height=20,bg="RED")
        Can1.place(x=10,y=50)
        Can2 = Canvas(fenetre2,width=20,height=20,bg="Blue")
        Can2.place(x=10,y=80)
        Can3 = Canvas(fenetre2,width=20,height=20,bg="green")
        Can3.place(x=10,y=110)
        Can33 = Canvas(fenetre2,width=20,height=20,bg="white")
        Can33.place(x=10,y=140)
        Can333 = Canvas(fenetre2,width=20,height=20,bg="black")
        Can333.place(x=10,y=170)
        Can44 = Canvas(fenetre2,width=20,height=20,bg="orange")
        Can44.place(x=35,y=50)
        Can55 = Canvas(fenetre2,width=20,height=20,bg="yellow")
        Can55.place(x=35,y=80)
        Can66 = Canvas(fenetre2,width=20,height=20,bg="purple")
        Can66.place(x=35,y=110)
        Can77 = Canvas(fenetre2,width=20,height=20,bg="brown")
        Can77.place(x=35,y=140)
        Can88 = Canvas(fenetre2,width=20,height=20,bg="thistle")
        Can88.place(x=35,y=170)

        ##creation canevas por couleurs supplementaires
        Cann1 = Canvas(fenetre2,width=20,height=20,bg="deep sky blue")
        Cann2 = Canvas(fenetre2,width=20,height=20,bg="cyan")
        Cann3 = Canvas(fenetre2,width=20,height=20,bg="blueviolet")
        Cann33 = Canvas(fenetre2,width=20,height=20,bg="lavender")
        Cann333 = Canvas(fenetre2,width=20,height=20,bg="turquoise")
        Cann44 = Canvas(fenetre2,width=20,height=20,bg="sandybrown")
        Cann55 = Canvas(fenetre2,width=20,height=20,bg="lightpink")
        Cann66 = Canvas(fenetre2,width=20,height=20,bg="lemonchiffon")
        Cann77 = Canvas(fenetre2,width=20,height=20,bg="tomato")
        Cann88 = Canvas(fenetre2,width=20,height=20,bg="coral")
        Cannn1 = Canvas(fenetre2,width=20,height=20,bg="indianred")
        Cannn2 = Canvas(fenetre2,width=20,height=20,bg="tan")
        Cannn3 = Canvas(fenetre2,width=20,height=20,bg="mediumblue")
        Cannn33 = Canvas(fenetre2,width=20,height=20,bg="lightskyblue")
        Cannn333 = Canvas(fenetre2,width=20,height=20,bg="lightsteelblue")
        Cannn44 = Canvas(fenetre2,width=20,height=20,bg="palegreen")
        Cannn55 = Canvas(fenetre2,width=20,height=20,bg="darkgrey")
        Cannn66 = Canvas(fenetre2,width=20,height=20,bg="orangered")
        Cannn77 = Canvas(fenetre2,width=20,height=20,bg="lightgray")
        Cannn88 = Canvas(fenetre2,width=20,height=20,bg="beige")




        #TEXTE
        ##Affichage paramete texte
        txt=Label(fenetre2, text="Texte :",bg="gainsboro")
        txt.place(x=1030,y=50)
        nom1= StringVar()
        saisie1= Entry(fenetre2, textvariable = nom1, width=15)
        saisie1.place(x= 1075,y=50)
        txt=Label(fenetre2, text="x =",bg="gainsboro")
        txt.place(x=1032,y=90)
        nom2= StringVar()
        saisie2= Entry(fenetre2,textvariable = nom2, width=5)
        saisie2.place(x=1060,y=90)
        txt=Label(fenetre2, text="y =",bg="gainsboro")
        txt.place(x=1032,y=120)
        nom3= StringVar()
        saisie3= Entry(fenetre2, textvariable = nom3, width=5)
        saisie3.place(x= 1060,y=120)

        #TEXTE-Choix police
        ##Arial
        C=Canvas(fenetre2,width=100,height=20,bg="gainsboro")
        C.place(x=1020,y=290)
        texte=C.create_text(10,10,text="Arial",font="Arial", fill="black")
        C.coords(texte, 20,10)
        C['highlightthickness']=0
        ##ITALIC
        C1=Canvas(fenetre2,width=100,height=20,bg="gainsboro")
        C1.place(x=1020,y=350)
        texte=C1.create_text(1,1,text="Italic",font="President 18 italic", fill="black")
        C1.coords(texte, 25,10)
        C1['highlightthickness']=0
        ##GRAS
        C2=Canvas(fenetre2,width=100,height=20,bg="gainsboro")
        C2.place(x=1020,y=410)
        texte=C2.create_text(1,1,text="Gras",font="Verdana 14 bold", fill="black")
        C2.coords(texte, 25,10)
        C2['highlightthickness']=0

        #COORDONNEES
        ## Horizontale
        txt=Label(fenetre2, text="0|",bg="gainsboro")
        txt.place(x=200,y=29)
        txt=Label(fenetre2, text="100|",bg="gainsboro")
        txt.place(x=300,y=29)
        txt=Label(fenetre2, text="200|",bg="gainsboro")
        txt.place(x=400,y=29)
        txt=Label(fenetre2, text="300|",bg="gainsboro")
        txt.place(x=500,y=29)
        txt=Label(fenetre2, text="400|",bg="gainsboro")
        txt.place(x=600,y=29)
        txt=Label(fenetre2, text="500|",bg="gainsboro")
        txt.place(x=700,y=29)
        txt=Label(fenetre2, text="600|",bg="gainsboro")
        txt.place(x=800,y=29)
        txt=Label(fenetre2, text="700|",bg="gainsboro")
        txt.place(x=900,y=29)
        txt=Label(fenetre2, text="780|",bg="gainsboro")
        txt.place(x=980,y=29)

        ##Vertical
        txt=Label(fenetre2, text="0-",bg="gainsboro")
        txt.place(x=180,y=41)
        txt=Label(fenetre2, text="100-",bg="gainsboro")
        txt.place(x=172,y=139)
        txt=Label(fenetre2, text="200-",bg="gainsboro")
        txt.place(x=172,y=239)
        txt=Label(fenetre2, text="300-",bg="gainsboro")
        txt.place(x=172,y=339)
        txt=Label(fenetre2, text="400-",bg="gainsboro")
        txt.place(x=172,y=439)
        txt=Label(fenetre2, text="500-",bg="gainsboro")
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

        #sauvegarder image (fonctionne pas)
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
        ## AFFICHAGE INITIAL ARIAL
        poli = Canvas(fenetre2,width=5,height=5,bg="red")
        poli.place(x=1115,y=298)

        ## AFFICHAGE DU CHOIX DE LA POLICE
        def ariane():
            global police
            police="Arial"
            poli = Canvas(fenetre2,width=5,height=5,bg="red")
            poli.place(x=1115,y=298)
            poli2 = Canvas(fenetre2,width=10,height=10,bg="gainsboro")
            poli2.place(x=1115,y=358)
            poli2['highlightthickness']=0
            poli3 = Canvas(fenetre2,width=10,height=10,bg="gainsboro")
            poli3.place(x=1115,y=418)
            poli3['highlightthickness']=0

        #police italic
        def italic():
            global police
            police="President 18 italic"
            poli = Canvas(fenetre2,width=10,height=10,bg="gainsboro")
            poli.place(x=1115,y=298)
            poli['highlightthickness']=0
            poli1 = Canvas(fenetre2,width=5,height=5,bg="red")
            poli1.place(x=1115,y=358)
            poli2 = Canvas(fenetre2,width=10,height=10,bg="gainsboro")
            poli2.place(x=1115,y=418)
            poli2['highlightthickness']=0

        #police gras
        def gras():
            global police
            police="Verdana 14 bold"
            poli = Canvas(fenetre2,width=10,height=10,bg="gainsboro")
            poli.place(x=1115,y=298)
            poli['highlightthickness']=0
            poli2 = Canvas(fenetre2,width=10,height=10,bg="gainsboro")
            poli2.place(x=1115,y=358)
            poli2['highlightthickness']=0
            poli3 = Canvas(fenetre2,width=5,height=5,bg="red")
            poli3.place(x=1115,y=418)


        #Texte
        ## Horizontal
        def texte():
            global T
            A=(saisie1.get())
            B=int(saisie2.get())
            C=int(saisie3.get())
            cox=B
            coy=C
            T=Candessin1.create_text(10,10,width=0,text=A,font=police, fill=u)
            Candessin1.coords(T, cox,coy)

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
            Candessin1.delete(T)

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
                        Candessin1.create_line( xold,yold,evt.x,evt.y,fill=u,width=w)
                    xold = evt.x
                    yold = evt.y

        #Ouverture Couleur supplementaire
        def coul():
                global Cann1,Cann2,Cann3,Cann33,Cann333,Cann44,Cann55,Cann66,Cann77,Cann88,Cannn1,Cannn2,Cannn3,Cann33,Cannn33,Cannn333,Cannn44,Cannn55,Cannn66,Cannn77,Cannn88
                cann = Canvas(fenetre2,width=95,height=320,bg="white")
                cann.place(x=70,y=10)
                Cann1 = Canvas(fenetre2,width=20,height=20,bg="deep sky blue")
                Cann1.place(x=80,y=30)
                Cann2 = Canvas(fenetre2,width=20,height=20,bg="cyan")
                Cann2.place(x=80,y=60)
                Cann3 = Canvas(fenetre2,width=20,height=20,bg="blueviolet")
                Cann3.place(x=80,y=90)
                Cann33 = Canvas(fenetre2,width=20,height=20,bg="lavender")
                Cann33.place(x=80,y=120)
                Cann333 = Canvas(fenetre2,width=20,height=20,bg="turquoise")
                Cann333.place(x=80,y=150)
                Cann44 = Canvas(fenetre2,width=20,height=20,bg="sandybrown")
                Cann44.place(x=80,y=180)
                Cann55 = Canvas(fenetre2,width=20,height=20,bg="lightpink")
                Cann55.place(x=80,y=210)
                Cann66 = Canvas(fenetre2,width=20,height=20,bg="lemonchiffon")
                Cann66.place(x=80,y=240)
                Cann77 = Canvas(fenetre2,width=20,height=20,bg="tomato")
                Cann77.place(x=80,y=270)
                Cann88 = Canvas(fenetre2,width=20,height=20,bg="coral")
                Cann88.place(x=80,y=300)
                Cannn1 = Canvas(fenetre2,width=20,height=20,bg="indianred")
                Cannn1.place(x=115,y=30)
                Cannn2 = Canvas(fenetre2,width=20,height=20,bg="tan")
                Cannn2.place(x=115,y=60)
                Cannn3 = Canvas(fenetre2,width=20,height=20,bg="mediumblue")
                Cannn3.place(x=115,y=90)
                Cannn33 = Canvas(fenetre2,width=20,height=20,bg="lightskyblue")
                Cannn33.place(x=115,y=120)
                Cannn333 = Canvas(fenetre2,width=20,height=20,bg="lightsteelblue")
                Cannn333.place(x=115,y=150)
                Cannn44 = Canvas(fenetre2,width=20,height=20,bg="palegreen")
                Cannn44.place(x=115,y=180)
                Cannn55 = Canvas(fenetre2,width=20,height=20,bg="darkgrey")
                Cannn55.place(x=115,y=210)
                Cannn66 = Canvas(fenetre2,width=20,height=20,bg="orangered")
                Cannn66.place(x=115,y=240)
                Cannn77 = Canvas(fenetre2,width=20,height=20,bg="lightgray")
                Cannn77.place(x=115,y=270)
                Cannn88 = Canvas(fenetre2,width=20,height=20,bg="beige")
                Cannn88.place(x=115,y=300)
                button1= Button(fenetre2, text="X",command=clear)
                button1.place(x=150,y=10)

        #Ferme les choix des couleurs supplementaire
        def clear():
            Canh = Canvas(fenetre2,width=100,height=330,bg="gainsboro")
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
        menubar = Menu(fenetre2)
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Ouvrir",command=ouvrir)
        menu1.add_separator()
        menu1.add_command(label="Enregister image",command=save)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=fenetre2.destroy)
        menubar.add_cascade(label="Fichier", menu=menu1)
        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Effacer",command=eff)
        menubar.add_cascade(label="Effacer", menu=menu2)
        fenetre2.config(menu=menubar)

        """Activation fonction"""
        #changer de couleur et taille crayon
        if'<ButtonPress-1>':
            fenetre2.bind('<ButtonPress-1>',clic1)

        #la fonction principale
        Candessin1.bind("<Motion>", motion)
        Candessin1.bind("<ButtonPress-1>", b1down)
        Candessin1.bind("<ButtonRelease-1>", b1up)


        """Bouttons"""
        #couleur supp
        button= Button(fenetre2, text=" >> ",command=coul)
        button.place(x=5,y=10)

        #texte
        B=Button(fenetre2, text=" texte horizontal ",command=texte)
        B.place(x=1010,y=170)
        B=Button(fenetre2, text="Annuler texte",command=efftexteH)
        B.place(x=1010,y=220)
        B=Button(fenetre2, text="Annuler texte",command=efftexteV)
        B.place(x=1115,y=220)
        button11= Button(fenetre2, text="✓",command=ariane)
        button11.place(x=1080,y=290)
        button12= Button(fenetre2, text="✓",command=italic)
        button12.place(x=1080,y=350)
        button13= Button(fenetre2, text="✓",command=gras)
        button13.place(x=1080,y=410)
        button16= Button(fenetre2, text="texte vertical",command=vert)
        button16.place(x=1120,y=170)
        button17= Button(fenetre2, text="X",command=ef)
        button17.place(x=1169,y=50)



        Fenetre.mainloop()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Image
FichFond=PhotoImage(file="menu_fond.gif")
FichCH1=PhotoImage(file="RP_OFF.gif")
FichCH2=PhotoImage(file="D_OFF.gif")

#Position des boutons
Fond.create_image(0,0,image=FichFond,anchor='nw')
CH1 = Fond.create_image(106,115,image=FichCH1,anchor='nw')
CH2 = Fond.create_image(541,111,image=FichCH2,anchor='nw')

choix = 0
Fond.bind('<Motion>',deplace)
Fond.bind('<ButtonPress-1>',valide)
Fenetre.mainloop()

