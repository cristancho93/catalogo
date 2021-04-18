from flask import Flask, render_template, redirect, url_for

from decorador import *
from fabricas import *
from random import choice


app = Flask(__name__)

@app.route('/')
def principal():
    return redirect(url_for("principal_decorador"))

@app.route('/original')
def principal_original():
    fabricas = [FabricaHumanos(), FabricaOrcos()]
    fabrica = choice(fabricas)
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()

    productos = []

    productos.append(arma)
    productos.append(escudo)
    return render_template("productos.html", productos = productos)

@app.route('/decorador')
def principal_decorador():

    cHumanos = ComponenteHumanos()
    cOrcos = ComponenteOrcos()

    fabricas = [DecoradorHumanos(cHumanos, cOrcos), DecoradorOrcos( cHumanos, cOrcos)]
    fabrica = choice(fabricas)
    cuerpo = fabrica.crear_cuerpo()
    montura = fabrica.crear_montura()
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()

    productos = []

    productos.append(cuerpo)
    productos.append(montura)
    productos.append(arma)
    productos.append(escudo)

    return render_template("productos.html", productos = productos)

if __name__ == '__main__':
    app.run(debug=True)