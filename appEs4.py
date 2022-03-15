
#Si vuole realizzare un sito web che permetta di visualizzare alcune informazioni sull'andamento dell'epidemia covid nel nostro paese, a partitre dai dati presenti
#nel file ("https://github.com/italia/covid19-opendata-vaccini/blob/master/dati/platea-dose-addizionale-booster.csv")
#l'utente sceglie la regione da un elenco (menù a tendina), clicca sul bottone e il sito deve visualizzare una tabella contenente le informazioni relative a quella regione
#i dati da inserire nel menù a tendina devono essere caricati automaticamente dalla pagina

from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv")

@app.route('/', methods=['GET'])
def index():
    reg = df['nome_area'].drop_duplicates().to_list()
    return render_template('regioniEs4.html', reg=reg)

@app.route('/risp', methods=['GET'])
def risp():
    regione = request.args['vaccini']
    df3 = df[df['nome_area']== regione]
    return render_template('covidEs4.html', tables=[df3.to_html()], titles=[''])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)