#si vuole realizare un sito web per memorizare le squadre di uuno sport a scelta
#l'utente deve poter inserie il nome della quadra e la data di fondazione e la città
#deve inoltre poter effetuare delle ricerche inserendo uno dei valori delle colonne e ottenenendo i dati presenti.
from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd

@app.route('/', methods=['GET'])
def index():
    squadre = [{'squadra':'Boston Celtics', 'Anno di Fondazione':'1946','città':'Boston'},
    {'squadra':'New York Knicks', 'Anno di Fondazione':'1946','città':'New York'},
    {'squadra':'Brooklyn Nets', 'Anno di Fondazione':'1967','città':'Brooklyn'},
    {'squadra':'Philadelphia 76ers', 'Anno di Fondazione':'1963','città':'Philadelphia'},
    {'squadra':'Toronto Raptors', 'Anno di Fondazione':'1995','città':'Toronto'},
    {'squadra':'Chicago Bulls', 'Anno di Fondazione':'1966','città':'Chicago'},
    {'squadra':'Cleveland Cavaliers', 'Anno di Fondazione':'1970','città':'Cleveland'},
    {'squadra':'Detroit Pistons', 'Anno di Fondazione':'1957','città':'Detroit'},
    {'squadra':'Indiana Pacers', 'Anno di Fondazione':'1976','città':'Indiana'},
    {'squadra':'Milwaukee Bucks', 'Anno di Fondazione':'1968','città':'Milwaukee'}]!
    return render_template("rispostaEs5.html", nome = squadre["squadra"], data = squadre["Anno di Fondazione"], citta = squadre["città")





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)