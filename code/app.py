from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
#estudiantes = [{
#    'nombre': 'Pedro Perez',
#    'edad': 18
#    'materias': [{
#       'titulo':'matematicas'
#    }]
#    }
#]
estudiantes = []

class Estudiante(Resource):
    def get(self, nombre):
        estudiante = next(filter(lambda x: x['nombre'] == nombre, estudiantes), None)
        return {'Estudiante': estudiante}, 200 if nombre else 404


    def post(self, nombre):
        if next(filter(lambda x: x['nombre'] == nombre, estudiantes), None):
            return {'message': f"Un estudiante con el nombre {nombre} ya existe"}, 400

        data = request.get_json()
        estudiante = {'nombre': nombre, 'edad': data['edad'], 'materias':[]}
        estudiantes.append(estudiante)
        return estudiante, 201

class MateriasEstudiante(Resource):
    def get(self, nombre):
        estudiante = next(filter(lambda x: x['nombre'] == nombre, estudiantes), None)
        if estudiante == None:
            return {'estudiante': estudiante}, 404
        else:
            return {'estudiante': estudiante}, 200


    def put(self, nombre):
        estudiante = next(filter(lambda x: x['nombre'] == nombre, estudiantes), None)
        if estudiante != None:
            data = request.get_json()
            estudiante['materias'].append({'titulo': data['titulo']})
            return {'materia':estudiante['materias']}, 201
        return {'message': f'El estudiante {nombre} no existe'}, 404



class ListaEstudiantes(Resource):
    def get(self):
        return {'estudiante': estudiantes}

api.add_resource(Estudiante, '/estudiante/<string:nombre>')
api.add_resource(ListaEstudiantes, '/estudiantes')
api.add_resource(MateriasEstudiante, '/estudiante/<string:nombre>/materia')