#Module

import os
from ftplib import FTP
import os.path
#Login et IP fonction

def login():
    ftp_host=(input("Host : "))
    ftp_login=(input("Login : "))
    ftp_password=(input('Password: '))
    ftp=FTP(ftp_host,ftp_login,ftp_password)
    print(ftp.getwelcome())
    return ftp
ftp=login()

#Liste répertoire
def repertoire():
    print("Liste des répéetoires et fichiers sur le serveur FTP : ")
    print(ftp.dir())
    print(ftp.nlst())
    print(os.getcwd())
    return ftp
repertoire()

#Envoyer un fichier :
def upload ():
    source = "C:\\TEST\\gg.txt"
    source_file= open(source, 'rb')
    ftp.storbinary('STOR '+source, source_file)
    source_file.close()
upload()

#Renommage des fichier :
def renommage ():
    source_file12=(input("Fichier renommer : "))
    ftp.rename(source_file12,(input("Nouveau nom : ")))
    return ftp
renommage()

#Supprimer un fichier :
def supprimer ():
    source_file1=(input("Fichier à supprimer :"))
    ftp.delete(source_file1)
supprimer()

#créer un répertoire :
def crer_rep():
    nouveau_repertoire=(input("Donner un nom au répertoire :"))
    ftp.mkd(nouveau_repertoire)
crer_rep()

def supprimer_rep():
    supprimer_repertoire=(input("Donner le nom du répértoire à supprimer :"))
    ftp.rmd(supprimer_repertoire)
supprimer_rep()

#Quitter la session ftp
def close():
    ftp.quit()
    ftp.close()
close()

