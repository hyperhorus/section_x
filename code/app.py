from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

estudiantes = [{
    'nombre': 'Pedro Perez',
    'edad': 18
    }
]


@app.route('/estudiantes')
def get_estudiantes():
    return jsonify({'estudiantes': estudiantes})

@app.route('/estudiante', methods=['POST'])
def crea_estudiante():
    data = request.get_json()
    nuevo_estudiante = {
        'nombre':data['nombre'],
        'edad': data['edad']
    }
    estudiantes.append(nuevo_estudiante)
    return jsonify(nuevo_estudiante)
