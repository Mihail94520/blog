from flask import Flask, render_template, send_file
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    categories = os.listdir('articles')

    return render_template('index.html', categories=categories)

def extraire_date_et_titre(nom_fichier):
    # Extraction de la date et du titre
    date_str, titre = nom_fichier[:8], nom_fichier[8:-5].replace('_', ' ')
    # Conversion de la date en format lisible
    date = datetime.strptime(date_str, '%Y%m%d').strftime('%d %B %Y')
    return date, titre, nom_fichier

@app.route('/categorie/<nom>')
def categorie(nom):
    categories = os.listdir('articles')
    articles = [ extraire_date_et_titre(f) for f in os.listdir('articles/' + nom) ]

    return render_template('articles.html', categorie=nom, categories=categories, articles=articles)

@app.route('/article/<categorie>/<article>')
def article(categorie, article):
    categories = os.listdir('articles')
    date_str, titre, nom_fichier = extraire_date_et_titre(article)
    # Lecture du contenu du fichier
    with open('articles/' + categorie + '/' + article, 'r', encoding='utf-8') as file:
        contenu = file.read()
    return render_template('article.html', categorie=categorie, categories=categories, contenu=contenu, titre=titre, date=date_str)

    #return send_file('articles/' + categorie + '/' + article)


@app.route('/somme/<nombre1>/<nombre2>')
def somme(nombre1, nombre2):
    return f'<h1>La somme de {nombre1} et {nombre2} donne {int(nombre1) + int(nombre2)}'

@app.route('/produit/<nombre1>/<nombre2>')
def produit(nombre1, nombre2):
    return render_template('produit.html', nombre1=nombre1, nombre2=nombre2,
        produit=int(nombre1)+int(nombre2))

if __name__ == '__main__':
    print('http://127.0.0.1:5000/') # domain name server
    app.run(debug=True)

