
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Ola. Minha primeira aplicacao'


@app.route(''/tdc')
def tdc_msg():
    return "Renderizando uma template"