from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/grafico.png')
def grafico():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], marker='o')
    ax.set_title("Gráfico con Matplotlib")

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
