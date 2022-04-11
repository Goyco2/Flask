from flask import Flask, render_template, request, send_file, make_response, url_for, Response, redirect
app = Flask(__name__)
import io
import geopandas
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tram_bus = geopandas.read_file("/workspace/Flask/VerificaC/tpl_percorsi_shp (2).zip")
milano = geopandas.read_file("/workspace/Flask/VerificaC/ds964_nil_wm/NIL_WM.dbf")

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["Scelta"]
    if scelta == "Es1":
        return redirect(url_for("lunghezza"))
    elif scelta == "Es2":
        return redirect(url_for("ricerca"))
    else:
        return redirect(url_for("dropdown"))

@app.route('/lunghezza', methods=['GET'])
def lunghezza():
    return render_template("valori.html")

@app.route('/lunghezzaCompresa', methods=['GET'])
def lunghezzaCompresa():
    val1 = request.args["Valore1"]
    val2 = request.args["Valore2"]
    tram_bus_compresi = tram_bus[tram_bus["lung_km"].astype("float") > float(val1)]
    tram_bus_compresi = tram_bus_compresi[tram_bus_compresi["lung_km"].astype("float") < float(val2)].sort_values(by = "linea", ascending = True)
    return render_template("elenco_compresi.html", tabella = tram_bus_compresi.to_html())

@app.route('/ricerca', methods=['GET'])
def ricerca():
    return render_template("input.html")

@app.route("/lineeQuart", methods=["GET"])
def lineequart():
    quartiere = request.args["Quartiere"]
    mappa_quartiere = milano[milano["NIL"].str.contains(quartiere)]
    linee_quartiere = tram_bus[tram_bus.intersects(mappa_quartiere.geometry.squeeze())].sort_values(by = "linea", ascending = True)
    return render_template("tabella_linee.html", tabella = linee_quartiere.to_html())

@app.route('/dropdown', methods=['GET'])
def dropdown():
    return render_template("dropdown.html", linee = tram_bus["linea"].drop_duplicates().sort_values(ascending=True))

@app.route("/mappa", methods=["GET"])
def mappa():
    global mappa_linea
    linea = int(request.args["Linea"])
    mappa_linea = tram_bus[tram_bus["linea"].astype("int") == linea]
    return render_template("mappa.html")

@app.route("/linea.png", methods=["GET"])
def lineaPng():
    fig, ax = plt.subplots(figsize = (12,8))

    mappa_linea.to_crs(epsg=3857).plot(ax=ax, edgecolor="r")
    milano.to_crs(epsg=3857).plot(ax=ax, alpha=0.6, edgecolor="k")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)