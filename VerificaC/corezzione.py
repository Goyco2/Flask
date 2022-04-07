from flask import Flask,render_template,request,send_file,make_response, url_for, Response,redirect
app = Flask(__name__)
import io
import os
import geopandas as gpd
import contextily as ctx
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

quartieri = gpd.read_file("/workspace/Flask/VerificaC/ds964_nil_wm/NIL_WM.dbf")
bus_tram = gpd.read_file('/workspace/Flask/VerificaC/tpl_percorsi_shp (2).zip')

@app.route('/', methods = ["GET"])
def homepage():
    return render_template("homeverificaC.html")

@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["scelta"]
    if scelta == "es1":
        return redirect("mid")
    elif scelta == "es2":
        return redirect("")
    else:
        return redirect("")
    return render_template("a.html")

@app.route('/mid', methods=['GET'])
def mid():
    return render_template("numriInp.html")

@app.route('/numero', methods=['GET'])
def numero():
    valore1 = int(request.args['valore1'])
    valore2 = int(request.args['valore2'])
    risultato1 = bus_tram[bus_tram['lung_km']< valore1 & bus_tram['lung_km']> valore2]
    return render_template('tabel1.html', table = risultato1.to_html())


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 3246, debug = True) 