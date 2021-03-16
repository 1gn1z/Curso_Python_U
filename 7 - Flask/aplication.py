import json
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route("/")
#@app.route("/<nombre>")
def hola(name="Invitado"):
    try:
        data = json.loads(request.cookies.get('data'))
    except TypeError:
        data = {}
    else:
        name = data.get('name')
    context = {'name':name}
    return render_template("index.html", **context)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<int:num2>")

def suma(num1=0 ,num2=0):
    nums = {'num1':num1, 'num2':num2}
    return render_template("suma.html", **nums)                           


@app.route("/resta/<int:num1>/<int:num2>")
@app.route("/resta/<float:num1>/<float:num2>")
@app.route("/resta/<int:num1>/<float:num2>")
@app.route("/resta/<float:num1>/<int:num2>")

def resta(num1=0 ,num2=0):
    nums = {'num1':num1, 'num2':num2}
    return render_template("resta.html", **nums) 


@app.route("/multiplicacion/<int:num1>/<int:num2>")
@app.route("/multiplicacion/<float:num1>/<float:num2>")
@app.route("/multiplicacion/<int:num1>/<float:num2>")
@app.route("/multiplicacion/<float:num1>/<int:num2>")

def multiplicacion(num1=0 ,num2=0):
    nums = {'num1':num1, 'num2':num2}
    return render_template("multiplicacion.html", **nums) 


@app.route("/division/<int:num1>/<int:num2>")
@app.route("/division/<float:num1>/<float:num2>")
@app.route("/division/<int:num1>/<float:num2>")
@app.route("/division/<float:num1>/<int:num2>")

def division(num1=0 ,num2=0):
    nums = {'num1':num1, 'num2':num2}
    return render_template("division.html", **nums) 


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

    
@app.route("/submit", methods=['POST'])
def submit():
    response = redirect(url_for('hola'))
    response.set_cookie('data', json.dumps(dict(request.form.items())))
    return response



    
"""
@app.route("/image")
def imagen():
    return render_template("image.html")
"""

if __name__ == "__main__":
    app.run(debug=True)
    