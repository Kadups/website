from flask import Flask, render_template
from flask.helpers import get_root_path
app = Flask(__name__)   

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pedidos")
def pedidos():  
    return render_template("/pedidos.html")

@app.route("/produtos")
def produtos():  
    return render_template("/produtos.html")

@app.route("/clientes")
def clientes():  
    return render_template("/clientes.html")

app.run(debug=True)