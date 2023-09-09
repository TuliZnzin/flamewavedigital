from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    # Suponha que você tenha uma lista de produtos para exibir
    products = [
        {'id': 1, 'name': 'Produto 1', 'price': 19.99},
        {'id': 2, 'name': 'Produto 2', 'price': 15.00},
        {'id': 3, 'name': 'Produto 3', 'price': 20.00},
    ]
    return render_template('homepage.html', products=products)

@app.route("/cardapiobebe")
def cardapiobebe():
    return render_template("cardapiobebe.html")

@app.route("/curso-canva")
def cursocanva():
    return render_template("curso-canva.html")

if __name__ == '__main__':
    app.run(debug=True)
