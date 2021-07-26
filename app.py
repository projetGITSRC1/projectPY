#le module os fournit une interface de système d'exploitation
from os import name
#le module re est principalement pour la recherche et la manipulation de chaines
import re
#module flask qui nous servira pour générer une sortie pour notre application web
from flask import Flask, render_template, request, redirect, url_for, session
#c'est une extension MySQLdb pour Flask 
from flask_mysqldb import MySQL,MySQLdb

import bcrypt

# Configuration MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

#ajout d'une route qui nous permet en générale de faire le lien entre la requêtre envoyer par l'utilisateur et la réponde.
@app.route('/')
def home():
    return render_template("home.html")

#rediriger l'utilisateur vers l'URL de inscription en HTML
@app.route('/inscription', methods=["GET", "POST"]) #spécifier qu'une page fonctionne à la fois avec les requêtes POST et GET. POST, cela signifie que nous avons soumis le formulaire. GET, ce signifie que nous avons reçus le formulaire
def inscription():
    if request.method == 'GET':
        return render_template("inscription.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",(name,email,hash_password,))
        
        mysql.connection.commit()
        session['name'] = name
        session['email'] = email
        return redirect(url_for('home'))
#rediriger l'utilisateur vers l'URL de connexion  en HTML
@app.route('/connexion', methods=["GET", "POST"]) 
def connexion():    
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = cur.fetchone()
        cur.close()
        #fonction qui nous dit que si le mot de passe ne correspond pas alors returnouner la page connexion sinon il est renvoyé à la page home avec son nom
        if len(user) > 0:
            if bcrypt.hashpw(password, user['password'].encode("utf-8")) == user['password'].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return render_template("home.html")
        else:
            return "le mot de passe ne correspond pas" 
    else:
        return render_template("connexion.html")

#rediriger l'utilisateur vers l'URL de Deconnexion en HTML
@app.route('/Deconnexion')
def deconnexion():
    session.clear()
    return render_template("home.html")

if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)