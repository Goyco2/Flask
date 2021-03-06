from flask import Flask,render_template,request,send_file,make_response, url_for, Response,redirect
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
stazioni = pd.read_csv("/workspace/Flask/VerificaA/templates/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv" ,sep = ";")
stazionigeo = geopandas.read_file("/workspace/Flask/VerificaA/templates/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson")
quartieri = geopandas.read_file("/workspace/Flask/VerificaA/static/ds964_nil_wm/NIL_WM.dbf")

@app.route('/', methods=['GET'])
def home():
    return render_template("homeverifica1.html")


@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["scelta"]
    if scelta == "es1":
        return redirect(url_for("numero"))
    elif scelta == "es2":
        return redirect(url_for("input"))
    else:
        return redirect(url_for("dropdown"))
    return render_template("a.html")

@app.route('/numero', methods=['GET'])
def numero():
#numero stazioni per ogni municio
    global risultato
    risultato = stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()
    return render_template("link1.html",risultato = risultato.to_html())

@app.route('/grafico', methods=['GET'])
def grafico():
    
    fig, ax = plt.subplots(figsize = (12,8))
    x = risultato.MUNICIPIO
    y = risultato.OPERATORE
    ax.bar(x,y,color = "#304C89")
    plt.xlabel("MUNICIPIO")
    plt.ylabel("OPERATORE")

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')



@app.route('/input', methods=['GET'])
def input():
#quartiere in cui bisogna far vedere le stazioni radio
   return render_template("input.html")

@app.route('/ricerca', methods=['GET'])
def ricerca():
#quartiere in cui bisogna far vedere le stazioni radio
    global quartiere,stazioniquartiere
    nomequartiere = request.args["quartiere"]
    quartiere = quartieri[quartieri.NIL.str.contains(nomequartiere)]
    stazioniquartiere = stazionigeo[stazionigeo.within(quartiere.geometry.squeeze())]
    
    return render_template("elenco.html", risultato = stazioniquartiere.to_html())

@app.route('/mappastazioni.png', methods=['GET'])
def mapstazioni():
    fig, ax = plt.subplots(figsize = (12,8))

    stazioniquartiere.to_crs(epsg=3857).plot(ax=ax, facecolor = "k",edgecolor = "k")
    quartiere.to_crs(epsg=3857).plot(ax=ax,alpha = 0.5, color = "red")
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/dropdown', methods=['GET'])
def dropdown():
#Avere la posizione in citt?? di una stazione radio.
   nomistazioni = stazioni.OPERATORE.to_list()
   nomistazioni = list(set(nomistazioni))
   nomistazioni.sort()
   return render_template("dropdown.html",stazioni = nomistazioni)

@app.route('/sceltastazione', methods=['GET'])
def sceltastazione():
    global quartiere2,stazioneuser
    stazione = request.args["stazione"] 
    stazioneuser = stazionigeo[stazionigeo.OPERATORE == stazione]
    quartiere2 = quartieri[quartieri.contains(stazioneuser.geometry.squeeze())]

    return render_template("vistastazione.html",quartiere2 = quartiere2)
    
@app.route('/mappaquartiere.png', methods=['GET'])
def mappaquartiere():
    fig, ax = plt.subplots(figsize = (12,8))

    stazioneuser.to_crs(epsg=3857).plot(ax=ax, facecolor = "k",edgecolor = "k")
    quartiere2.to_crs(epsg=3857).plot(ax=ax,alpha = 0.5, color = "red")
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)