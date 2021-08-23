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
#  endpoint inicial     : https://tdc2021.pythonanywhere.com/
#  endpoint opções      : https://tdc2021.pythonanywhere.com/tdc
#  endpoint input       : https://tdc2021.pythonanywhere.com/tdcinput
#  endpoint botao radio : https://tdc2021.pythonanywhere.com/tdcradio
#  endpoint api         : https://tdc2021.pythonanywhere.com/tdcapi
# ------------------------------------------------

import tdc2021_func

from flask import Flask, request, json
from flask import render_template

chave_autenticacao = 'aSdrt12677489IopkljgrtrewwfghvcbnMmjgsfwety553724132788'

app = Flask(__name__)

#---------------------------------------------
# endpoint http://tdc2021.pythonanywhere.com/
@app.route('/')
def hello_world():
    return {'Home':'Ola TDC 2021. Minha primeira aplicacao'}
#--------------------------------------------------
# endpoint http://tdc2021.pythonanywhere.com/tdc
@app.route('/tdc')
def tdc():
    return render_template( "index.html" )
#-----------------------------------------------------
# endpoint http://tdc2021.pythonanywhere.com/tdcinput
@app.route('/tdcinput', methods=['GET','POST'])
def tdc_Input():
    if request.method == 'GET':
        return render_template( "tdc_input.html" )
    if request.method == 'POST':
        return json.dumps({'Nome': str(request.form.get('nome')),
                'Email': str(request.form.get('email'))},ensure_ascii=False )
#-----------------------------------------------------
# endpoint http://tdc2021.pythonanywhere.com/tdcradio
@app.route('/tdcradio', methods=['GET','POST'])
def tdc_Radio():
    if request.method == 'GET':
        return render_template( "tdc_radio_button.html" )
    if request.method == 'POST':
        return json.dumps({'Idade': str(request.form.get('idade'))}, ensure_ascii=False )
#-----------------------------------------------------
# endpoint http://tdc2021.pythonanywhere.com/tdcmenu
@app.route('/tdcmenu', methods=['GET','POST'])
def tdc_Menu():
    return render_template( "tdc_menu.html" )
#-----------------------------------------------------
# endpoint http://tdc2021.pythonanywhere.com/tdcapi
@app.route('/tdcapi')
def tdc_Api():
    ipuser = request.headers['X-Real-IP']
    chave = request.headers.get('secret-key')
    if chave == None :
        return json.dumps({"ip": str(ipuser), "Erro" : "Não envio de chave" }, ensure_ascii=False )
    if chave != chave_autenticacao :
        return json.dumps({"ip": str(ipuser), "Erro" : "Autenticação" }, ensure_ascii=False )
    else :
        return json.dumps({"ip" : str(ipuser), "Api,":"exemplo"}, ensure_ascii = False )