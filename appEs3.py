#realizzare un serve web che permetta di conoscere copoluoghi di regione.
#l'utente inserisce il nome della regione
#e il programma restituisce il nome del capo luogho di regione.
#caricare i capoluoghi di regione e le regioni in una opportuna struttura dati
#modificare pio l'eserciso precedente per permttere all'utente di inserire un capoluogho ed avere la regione in cui si trova
#l'utente sceglie se avere la regioneo capoluogho selezionando un radio button 
from flask import Flask, render_template, request
app = Flask(__name__)
dizionario  = {'Valle Aosta' : "Aosta", "Piemonte" : "Torino", "Liguria" : "Genova", "Lombardia" : "Milano", "Trentino-Alto Adige" : "Trento", "Veneto" : "Venezia", "Friuli-Venezia Giulia" : "Trieste", "Emilia-Romagna" : "Bologna","Toscana" : "Firenze","Marche" : "Ancona","Lazio" : "Roma","Umbria" : "Perugia","Abruzzo" : "L'Aquila","Molise" : "Campobasso","Campania" : "Napoli","Puglia" : "Bari","Basilicata" : "Potenza","Calabria" : "Catanzaro","Sicilia" :"Palermo","Sardegna" : "Cagliari"}
@app.route('/', methods=['GET'])
def hello_world():
    return render_template("datiIta.html")


@app.route('/data', methods=['GET'])
def Data():
    scelta = request.args["Scelta"]
    if scelta == "R":
        return render_template("regionees3.html")
    else:
        return render_template("capoluogoes3.html")
    

@app.route("/dataReg", methods=["GET"])
def dataReg():
    regione = request.args["Regione"]
    for key, value in dizionario.items():
        if regione == key:
            capoluogo = value
            return render_template("RispostaEs3.html", risp = capoluogo)
    return "<h1>Errore</h1>"

@app.route("/dataCap", methods=["GET"])
def dataCap():
    capoluogo = request.args["Capoluogo"]
    for key, value in dizionario.items():
        if capoluogo == value:
             regione = key
             return render_template("RispostaEs3.html", risp = regione)
    return "<h1>Errore</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)