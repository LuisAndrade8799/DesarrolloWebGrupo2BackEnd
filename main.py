from conexion.Conexion import Conexion
from repositorio.RepositorioUsuario import RepositorioUsuario as ru
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
conexion = Conexion().getConexion()
@app.route('/api/data', methods=['POST'])
def getUsuario():
  datos = request.get_json()
  usuario = datos.get("usuario")
  contrasenia = datos.get("contrasenia")
  resultado = ru.getUsuario(conexion,usuario,contrasenia)
  return jsonify(resultado)

if __name__ == '__main__':
  app.run(debug=True)
