import os

from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


@app.route('/')
def home():
    data = json.load(open(os.path.join(SITE_ROOT, "static/content", "catalog.json")))
    return render_template('pages/home.html',
                           pagina={
                               "productos": data[:4]
                           }
                           )


@app.route('/producto')
def producto():
    return render_template('pages/producto.html')


@app.route('/catalogo')
def catalogo():
    data = json.load(open(os.path.join(SITE_ROOT, "static/content", "catalog.json")))
    return render_template(
        'pages/catalogo.html',
        products=data,
        categories=[
            {"label": "Sillas", "slug": "sillas"},
            {"label": "Sofás", "slug": "sofas"},
            {"label": "Futones", "slug": "futones"},
            {"label": "Comedores", "slug": "comedores"},
            {"label": "Alcoba", "slug": "alcoba"}
        ]
    )


@app.route('/checkout')
def checkout():
    return render_template('pages/checkout.html')


@app.post('/checkout')
def form_post():
    form = request.form
    return jsonify({
        'form': form.to_dict()
    })


if __name__ == '__main__':
    app.run(debug=True)
