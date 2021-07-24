from tkinter import *


def register_user():
    
    username_info = username.get()
    password_info = password.get()

    file=open(username_info+ ".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1, text= "Registration sucess", fg="green", font = ("calibri", 11)).pack()

def register():
    global screen1
    screen1= Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text ="please enter details").pack()
    Label(screen1,text = "").pack()
    
    Label(screen1, text = "username * ").pack()
    username_entry= Entry(screen1, textvariable= username)
    username_entry.pack()
    
    Label(screen1, text = "password * ").pack()
    password_entry= Entry(screen1, textvariable= password)
    password_entry.pack() 
    Label(screen1,text = "").pack()
    
    Button(screen1, text= "Register", width=10, height=1, command=register_user).pack()
    #pensez à la securité sha 


def login(): 
    print("la session débute")



def main_screen():
    global screen
    screen =Tk()
    screen.geometry("300x250")
    screen.title("Notes V1.0")
    Label(text= "Notes V1.0", bg = "grey", width="300", height="2", font= ("Calibri", 13)).pack() #background
    Label(text = "").pack()   #chaine vide 
    Button(text="Connectez-vous", height="2", width="30", command= login ).pack()  # bouton 1 pour le login
    Label(text = "").pack()   #gestionnaire qui organise les widgets
    Button(text="Inscrivez-vous", height="2", width="30", command = register).pack()  # bouton 2 pour la connexion

    screen.mainloop() #pour savoir si notre main_screen a des erreurs

main_screen()#appelle de la fonction
