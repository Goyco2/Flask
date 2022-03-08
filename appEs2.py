#realizzare un sito web che permetta la regitrazione degli utenti
#l'utente inserice il nome username password la conferma della password e il sesso
#se le informazioni sono corette il sito salva le informazioni in una struttura dati opportuna(una lista di dizionario)
#prevedere la possibilità di fare il log in 
#inserendo username e password se sono corette un mesaggio di benvenuo diverso a seconda del sesso 
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("datiLogin.html")

@app.route('/data', methods=['GET'])
def Data():
    name = request.args['name']
    psw = request.args['psw']
    username = request.args['username']
    VerPass = request.args['Verificapassword']
    Sex = request.args['Sex']
    if psw == VerPass:
        utente = {'name': name, 'psw':psw, 'username':username, 'Sex':Sex}
        lst.append(utente)
        if name =='' or psw =='' or username == ''or se == ''or VerPass == '':
            return render_template("Sbagliato.html")
        elif Sex == 'M':
            return render_template("GiustoM.html",nome=name)
        elif Sex =='F':
            return render_template("GiustoF.html",nome=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)