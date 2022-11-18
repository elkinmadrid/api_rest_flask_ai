from flask import Flask
from flask import jsonify, request
import json
from sistemadereglas import *
import conexion as con
from algoritmo import *

from flask_cors import CORS
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})




@app.route('/')
def hello():
    
    return 'Home'


@app.route('/algoritmo')
def algoritmo_get():

    algoritmo_ = algoritmo()
    response = algoritmo_.initialize()

    return jsonify(response)


@app.route('/systemrules', methods=['POST'])
def save_questions():

    record = json.loads(request.data)


    primeraPregunta = record['data']['primeraPregunta']
    segundaPregunta = int(record['data']['segundaPregunta'])
    terceraPregunta = record['data']['terceraPregunta']
    cuartaPregunta = record['data']['cuartaPregunta']
    quintaPregunta = record['data']['quintaPregunta']

    engine = sistemadereglas()
    engine.reset()

    engine.declare(reglas(ansiedad=primeraPregunta))
    engine.declare(reglas(perdida_interes=segundaPregunta))
    engine.declare(reglas(descontento=terceraPregunta))
    engine.declare(reglas(altibajo=cuartaPregunta))
    engine.declare(reglas(apatia=quintaPregunta))
    engine.run()

    query_insert = "INSERT INTO database1.sistemadereglas        (id_users, resp_primera_pregunta, resp_segunda_pregunta, resp_tercera_pregunta, resp_cuarta_pregunta, resp_quinta_pregunta, diagnostico)     VALUES( %s, %s, %s, %s, %s, %s, %s);  "
    data = (1, primeraPregunta, segundaPregunta, terceraPregunta, cuartaPregunta, quintaPregunta, engine.id,)    

    #query = "SELECT id, descripcion FROM database1.diagnosticos WHERE id=1;"

    data = con.conexion.run_query(query_insert, data)

    return jsonify(engine.diagnostic)
