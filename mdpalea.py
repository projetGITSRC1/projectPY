###On import tkinter pour l'interface graphique et le random pour générer les données aléatoire
from tkinter import *
from tkinter.ttk import Combobox
import random

###Cette partie affiche le titre de l'interface graphique.
screen = Tk()
screen.title("Générateur de mot de passe")
screen.geometry('650x350')
screen.configure(background ="gray")

###Cette partie regroupe les caractères majuscule/minuscule, caractères spéciaux et chiffres.
def gen():
    global sc1
    sc1.set("")
    passw=""
    length=int(c1.get())
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'+lowercase
    mixs='0123456789'+lowercase+uppercase+'@#$%&*&()[]'

    ###Cette partie est une interface qui permet de choisir la force du mot de passe
    if c2.get()=='Low Strength':
        for i in range(0,length):
            passw=passw+random.choice(lowercase)
        sc1.set(passw)
    elif c2.get()=='Medium Strength':
        for i in range(0,length):
            passw=passw+random.choice(uppercase)
        sc1.set(passw)
    elif c2.get()=='High Strength':
        for i in range(0,length):
            passw=passw+random.choice(mixs)
        sc1.set(passw)

###Cette partie est l'interface graphique qui nous affiche le titre
sc1=StringVar('')
t1=Label(screen,text='Générateur de mot de passe',font=('Arial',25),fg='black',background ="gray")
t1.place(x=130,y=0)

###Cette partie nous affiche la case du mot de passe qui va être générer
t2=Label(screen,text='Password:',font=('Arial',14),background ="gray")
t2.place(x=145,y=90)
il=Entry(screen,font=('Arial',14),textvariable=sc1,width=24)
il.place(x=240,y=90)

###Cette partie nous affiche l'endroit où l'on va rentrez la taille de notre mot de passe
t3=Label(screen,text='Length: ',font=('Arial',14),background ="gray")
t3.place(x=145,y=120)
c1=Entry(screen,font=('Arial',14),width=10)
c1.place(x=240,y=120)

###Cette partie permet de choisir la force de notre mot de passe
t4=Label(screen,text='Strength:',font=('Arial',14),background ="gray")
t4.place(x=145,y=150)
c2=Combobox(screen,font=('Arial',14),width=15)
c2['values']=('Low Strength','Medium Strength','High Strength')
c2.current(2)
c2.place(x=240,y=150)

###Cette partie nous sert à générer le mot de passe une fois les configuration sont faites
b=Button(screen,text='Générer',font=('Arial',14),fg='black',background ="white",command=gen)
b.place(x=250,y=190)

screen.mainloop()
