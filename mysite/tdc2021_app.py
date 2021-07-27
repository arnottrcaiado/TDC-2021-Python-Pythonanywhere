#
# Aplicação criada para fins de exemplo
# Para: TDC 2021 - Transformation
#
# Trilha: Python
#
# Autores:  Arnott Ramos Caiado
#           Inoã de Paulo Liberato
#
# MVP, Protótipo, rápido Deploy Web com Python: uso do PythonAnywhere
#
#    Às vezes é necessário ter um protótipo rodando na web em tempo record. Ou ainda,
#    você está diante de um desafio onde o tempo para validar a idéia é curtíssimo:
#    eis que entra o PythonAnywhere como alternativa para sua solução.
#    Isto ocorreu comigo há um tempo atrás, quando tinha que resolver em equipe um problema integrando back, front e mobile com Python.
# ------------------------------------------------

from flask import Flask, request
from flask import render_template
import tdc2021_func

app = Flask(__name__)

# endpoint http://tdc2021.pythonanywhere.com/
@app.route('/')
def hello_world():
    return 'Ola TDC 2021. Minha primeira aplicacao'

# endpoint http://tdc2021.pythonanywhere.com/tdc
@app.route('/tdc')
def tdc_msg():
    return render_template( "index.html" )

# endpoint http://tdc2021.pythonanywhere.com/tdc/api
@app.route('/tdc/api')
def tdc_api():
    ipuser = request.headers['X-Real-IP']
    return {"ip" : str(ipuser),
    "Api,":"exemplo"}
