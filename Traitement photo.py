"""PROGRAMME TRAITEMEnt D'IMAGE"""

################################################################################

"""BIBLIOTHEQUE"""
from tkinter import*
from tkinter.filedialog import*
from tkinter.messagebox import *
from PIL import Image, ImageTk


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""DEBUT PROGRAMME"""
#FENETRE
fenetre=Tk()
fenetre.geometry("1200x600")
fenetre.title("Retouche Photo")

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
    CanA = Canvas(fenetre,width=225,height=250,bg="white")
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

fenetre.mainloop()
