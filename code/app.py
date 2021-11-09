from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
#estudiantes = [{
#    'nombre': 'Pedro Perez',
#    'edad': 18
#    }
#]
estudiantes = []

class Estudiante(Resource):
    def get(self, nombre):
        #estudiante = next(filter(lambda x: x['nombre'], estudiantes), None)
        #return {'Estudiante': estudiante}, 200 if nombre else 404
        for estudiante in estudiantes:
            if estudiante['nombre'] == nombre:
                return estudiante
        return {'Estudiante': None}, 404


    def post(self, nombre):
        data = request.get_json()
        estudiante = {'nombre': nombre, 'edad': data['edad']}
        estudiantes.append(estudiante)
        return estudiante, 201

class ListaEstudiantes(Resource):
    def get(self):
        return {'estudiante': estudiantes}

api.add_resource(Estudiante, '/estudiante/<string:nombre>')
api.add_resource(ListaEstudiantes, '/estudiantes')