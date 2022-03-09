#realizzare un sito web che permetta la regitrazione degli utenti
#l'utente inserice il nome username password la conferma della password e il sesso
#se le informazioni sono corette il sito salva le informazioni in una struttura dati opportuna(una lista di dizionario)
#prevedere la possibilità di fare il log in 
#inserendo username e password se sono corette un mesaggio di benvenuo diverso a seconda del sesso 
from flask import Flask, render_template, request
app = Flask(__name__)

lista = []
@app.route('/', methods=['GET'])
def hello_world():
    return render_template("datiLogin.html")

@app.route('/data', methods=['GET'])
def Data():
    print(request.args)
    name = request.args['name']
    psw = request.args['psw']
    username = request.args['username']
    VerPass = request.args['Verificapassword']
    Sex = request.args['Sex']
    if psw == VerPass:
        lista.append({"name" : name, "username" : username, "Sex" : Sex, "psw" : psw})
        return render_template('es2login.html')
    else:
        return render_template('Sbagliato.html')

@app.route("/log", methods=["GET"])
def login():
    psw_log = request.args['psw']
    username_log = request.args['username']
    for utente in lista:
        if utente['username'] == username_log and utente['psw'] == psw_log:
            if utente['Sex'] == 'M':
                return render_template("welcome.html",nome=utente['name'])
            elif utente['Sex'] == 'M':
                return render_template("welcomeses2.html",nome=utente['name'])
            else:
                return render_template("benvent*.html",nome=utente['name'])

    return render_template("Sbagliato.html", mesaggio='username o password sbagliato')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)