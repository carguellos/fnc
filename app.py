from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def home():
    return render_template('pages/home.html',
        pagina={
            "productos": [
                    {
                        "title":"Silla Nordik",
                        "price":"$90.000"
                    },
                    {
                        "title":"Silla Nordik",
                        "price":"$110.000"
                    },
                    {
                        "title":"Silla Nordik",
                        "price":"$120.000"
                    }
            ]
        }
    )

@app.route('/producto')
def producto():
    return render_template('pages/producto.html')


@app.route('/catalogo')
def catalogo():
    return render_template('pages/catalogo.html')


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