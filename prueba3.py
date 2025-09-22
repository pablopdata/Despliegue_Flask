import matplotlib.pyplot as plt
from flask import Flask, send_file
import io

app = Flask(__name__)

@app.route('/grafico')
def grafico():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
    ax.set_title("Ejemplo de gráfico")

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')
