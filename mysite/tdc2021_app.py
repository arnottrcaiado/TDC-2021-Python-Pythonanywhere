
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Ola. Minha primeira aplicacao'

@app.route('/tdc')
def tdc_msg():
    return render_template( "index.html" )

@app.route('/tdc/api')
def tdc_api():
    return {"Api":"exemplo"}
