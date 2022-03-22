#realizare un sito web che restituisca la mappa dei quartieri di milano.
#ci deve essere una home page con un link "quartieri di mialno":
#cilccando su questo link si devev visualizzare la mappa dei quartieri di milano
from flask import Flask, render_template, send_file, make_response, url_for, Response
app = Flask(__name__)
import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

quartieri = gpd.read_file('/workspace/Flask/ds964_nil_wm')

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('simple.html')

@app.route('/plot.png', methods=['GET'])
def plot_png():

    fig, ax = plt.subplots(figsize = (12,8))

    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/plot', methods=("POST", "GET"))
def mpl():
    return render_template('plot.html',
                           PageTitle = "Matplotlib")

@app.route('/data', methods=("GET"))
def data():
    quartInp = request.args["quartInp"]
    df3 = quartieri[quartieri['NIL']== quartInp]
    return df3.plot


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)