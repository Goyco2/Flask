from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/meteo")
def meteo():
    nRandom = random.randint(0,8)
    if nRandom <= 2:
        immagine = "/static/images/pioggia.jpg"
    elif nRandom <= 5:
        immagine = "/static/images/nuvoloso.jpg"
    else:
        immagine = "static/images/sole.jpg"
    return render_template("meteo.html", meteo=immagine)
@app.route("/libro")
def libro():
    frasi = [{"Autore": "Frida Kahlo" , "Frase": "Innamorati di te, della vita e dopo di chi vuoi." },
    {"Autore": "Dietrich Bonhoeffer" , "Frase": "Contro la stupidità non abbiamo difese."},
    {"Autore": "Charlie Chaplin" , "Frase": "Un giorno senza un sorriso è un giorno perso."},{"Autore": "Francesco Bacone" , "Frase": "Sapere è potere."},
    {"Autore": "Italo Calvino" , "Frase": "Il divertimento è una cosa seria."},{"Autore": "Lewis Carroll" , "Frase": "Qui siamo tutti matti."},
    {"Autore": "Johann Wolfgang von Goethe", "Frase": "Il dubbio cresce con la conoscenza."},{"Autore": "Luis Sepùlveda" , "Frase": "Vola solo chi osa farlo."},
    {"Autore": "Lucio Anneo Seneca", "Frase": "Se vuoi essere amato, ama."},{"Autore": "Voltaire", "Frase": "Chi non ha bisogno di niente non è mai povero."}]
    fRandom = random.randint(0,9)
    return render_template("frasicelebri.html", autore = frasi[fRandom]["Autore"], frase = frasi[fRandom]["Frase"])
@app.route("/conta")
def conta():
    fine = datetime.date(2022,6,8)
    oggi = datetime.datetime.now()
    differenza_giorni = fine - oggi
    return render_template("differenza.html",differenza_giorni)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)