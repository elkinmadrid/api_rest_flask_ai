from flask import Flask
from flask import jsonify, request
import json
from sistemadereglas import *

from flask_cors import CORS
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})




@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/algoritmo')
def algoritmo():
    return 'Este es el endpoint para el algoritmo!'


@app.route('/systemrules', methods=['POST'])
def save_questions():

    record = json.loads(request.data)


    print(record)
    primeraPregunta = record['data']['primeraPregunta']
    segundaPregunta = record['data']['segundaPregunta']
    terceraPregunta = record['data']['terceraPregunta']
    cuartaPregunta = record['data']['cuartaPregunta']
    quintaPregunta = record['data']['quintaPregunta']


    engine = sistemadereglas()
    engine.reset()

    engine.declare(reglas(contrato="No"))
    engine.declare(reglas(antiguedad="No"))
    engine.declare(reglas(tipo_credito="No"))
    engine.declare(reglas(meses_credito="No"))
    engine.declare(reglas(ingresos="No"))
    engine.run()

  

    return jsonify(record)
