#realizare un server web che permetta di effetuare login 
#l'utente inserice lo username e la password:
#se lo username e admin e la password e xxx123## 
#il sito ci saluta con un mesaggio di benvenuto
#altrimenti un mesaggio di erorre

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("datiUtente.html")

@app.route('/data', methods=['GET'])
def Data():
    name = request.args['username']
    psw = request.args['psw']
    if name == 'Admin' and psw == 'xxx123##':
        return render_template("Giusto.html",nome=name)
    else:
        return render_template("Sbagliato.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)