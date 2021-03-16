# Ya tenemos una pseudo calculadora que permite sumar. 

# El reto es hacer la MULTIPLICACION, LA DIVISION Y LA RESTA.

# Hacerla en distintas views

#   RESTA:

#   CODIGO PYTHON:


@app.route("/resta/<int:num1>/<int:num2>")
@app.route("/resta/<float:num1>/<float:num2>")
@app.route("/resta/<int:num1>/<float:num2>")
@app.route("/resta/<float:num1>/<int:num2>")

def resta(num1=0 ,num2=0):
    nums = {'num1':num1, 'num2':num2}
    return render_template("resta.html", **nums) 


#   CODIGO HTML:

{% extends 'base_layout.html' %}

{% block title %}Resta{% endblock %}

{% block content %}<h1>{{ num1 }} - {{ num2 }} = {{ num1-num2 }}</h1>{% endblock %}


#   MULTIPLICACION:

#   CODIGO PYTHON:


@app.route("/multiplicacion/<int:num1>/<int:num2>")
@app.route("/multiplicacion/<float:num1>/<float:num2>")
@app.route("/multiplicacion/<int:num1>/<float:num2>")
@app.route("/multiplicacion/<float:num1>/<int:num2>")

def multiplicacion(num1=0 ,num2=0):
    nums = {'num1':num1, 'num2':num2}
    return render_template("multiplicacion.html", **nums)


#  CODIGO HTML:

{% extends 'base_layout.html' %}

{% block title %}Multiplicación{% endblock %}

{% block content %}<h1>{{ num1 }} * {{ num2 }} = {{ num1 * num2 }}</h1>{% endblock %}


#   DIVISION:


#   CODIGO PYTHON:


@app.route("/division/<int:num1>/<int:num2>")
@app.route("/division/<float:num1>/<float:num2>")
@app.route("/division/<int:num1>/<float:num2>")
@app.route("/division/<float:num1>/<int:num2>")

def division(num1=0 ,num2=0):
    nums = {'num1':num1, 'num2':num2}
    return render_template("division.html", **nums) 

#   CODIGO HTML:

{% extends 'base_layout.html' %}

{% block title %}División{% endblock %}

{% block content %}<h1>{{ num1 }} / {{ num2 }} = {{ num1/num2 }}</h1>{% endblock %}



# NO OLVIDAR GUARDAR LOS HTMLS EN LA CARPETA "TEMPLATES"



# RETO LISTO!!!