from conexion.Conexion import Conexion
from repositorio.RepositorioUsuario import RepositorioUsuario as ru
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
conexion = Conexion().getConexion()
@app.route('/api/login', methods=['POST'])
def getUsuario():
  datos = request.get_json()
  usuario = datos.get("usuario")
  contrasenia = datos.get("contrasenia")
  resultado = ru.getUsuario(conexion,usuario,contrasenia)
  return jsonify(resultado)

@app.route('/api/matriculado', methods=['POST'])
def getMatriculado():
  dato = request.get_json()
  codigo = dato.get("codigo")
  resultado = ru.getMatriculado(conexion,codigo)
  return jsonify(resultado)

@app.route('/api/registro', methods=['POST'])
def registrar():
  datos = request.get_json()
  usuario = datos.get("usuario")
  codigo = datos.get("codigo")
  contraseina =datos.get("contrasenia")
  resultado = ru.registrar(conexion,usuario,codigo,contraseina)
  return jsonify(resultado)

if __name__ == '__main__':
  app.run(debug=True)
