from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    categories = os.listdir('articles')

    return render_template('index.html', categories=categories)

@app.route('/categorie/<nom>')
def categorie(nom):
    categories = os.listdir('articles')
    articles = os.listdir('articles/' + nom)

    return render_template('articles.html', categorie=nom, categories=categories, articles=articles)

@app.route('/article/<categorie>/<article>')
def article(categorie, article):

    return send_file('articles/' + categorie + '/' + article)


@app.route('/somme/<nombre1>/<nombre2>')
def somme(nombre1, nombre2):
    return f'<h1>La somme de {nombre1} et {nombre2} donne {int(nombre1) + int(nombre2)}'

@app.route('/produit/<nombre1>/<nombre2>')
def produit(nombre1, nombre2):
    return render_template('produit.html', nombre1=nombre1, nombre2=nombre2,
        produit=int(nombre1)+int(nombre2))

if __name__ == '__main__':
    print('http://127.0.0.1:5000/') # domain name server
    # os.chdir(os.path.dirname(__file__))
    app.run(debug=True)

