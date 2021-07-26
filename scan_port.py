import socket
import sys
import time
import datetime


Server = input("Entrez l'adresse IP du serveur à scanner: ")

    startport = input("Entez le premier port à scanner -->")
    print("Port de départ = ", startport)

    endport = input("Entez le dernier port à scanner -->")
    print("Dernier port = ", endport)
    endport = int(endport) + 1

    print("Lancement du scan de port sur le serveur: ", Server)

    f = open('scan.txt', 'w')

    date = datetime.datetime.now().date()
    heure = datetime.datetime.now().time()
    print("Date du scan:", date.strftime('%A %d, %B %y ') + heure.strftime('%H:%M:%S'))
    f.write("Date du scan: " + str(date.strftime('%A %d, %B %y ') + "à " + str(heure.strftime('%H:%M:%S\n'))))

    ServerIp = socket.gethostbyname(Server)
    for port in range(int(startport), int(endport)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ServerIp, port))
        if result == 0:
            print("Port {}: Ouvert".format(port))
            f.write("Le port TCP " + str(port) + " est Ouvert \n")
        else:
            print("Port {}: Fermé".format(port))
            f.write("Le port TCP " + str(port) + " est Fermé \n")
        sock.close()
    f.close()
