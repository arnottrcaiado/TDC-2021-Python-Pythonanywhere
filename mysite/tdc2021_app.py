#
# Aplicação criada para fins de exemplo
# Para: TDC 2021 - Transformation
#
# Trilha: Python
#
# Autores:  Arnott Ramos Caiado
#           Inoã Liberato
#

from flask import Flask
from flask import render_template
import tdc2021_func

app = Flask(__name__)

# endpoint http://tdc2021.pythonanywhere.com/
@app.route('/')
def hello_world():
    return 'Ola. Minha primeira aplicacao'

# endpoint http://tdc2021.pythonanywhere.com/tdc
@app.route('/tdc')
def tdc_msg():
    return render_template( "index.html" )

# endpoint http://tdc2021.pythonanywhere.com/tdc/api
@app.route('/tdc/api')
def tdc_api():
    return {"Api":"exemplo"}
