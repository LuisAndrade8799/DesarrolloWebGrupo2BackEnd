from conexion.Conexion import Conexion
from repositorio.RepositorioUsuario import RepositorioUsuario as ru
from repositorio.RepositorioCurso import RepositorioCurso as rc
from repositorio.RepositorioRectificar import RepositorioRectificar as rr
from flask import Flask, jsonify, request
from flask_cors import CORS

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

@app.route('/api/cursos',methods=['POST'])
def getCursos():
  datos = request.get_json()
  codigo = datos.get("codigo")
  resultado = rc.getCursos(conexion,codigo)
  return jsonify(resultado)

@app.route('/api/rectificar', methods=['POST'])
def rectificar():
  datos = request.get_json()
  resultado = rr.insertarRecti(conexion,datos)
  return jsonify(resultado)

@app.route('/api/ingreso', methods=['GET'])
def getIngreso():
  resultado = rr.getIngresos(conexion)
  return jsonify(resultado)

@app.route('/api/retiro', methods=['GET'])
def getRetiro():
  resultado = rr.getRetiro(conexion)
  return jsonify(resultado)

@app.route('/api/obtenernombres', methods=['GET'])
def getNombre():
  resultado = rc.getNombreCursos(conexion)
  return jsonify(resultado)

@app.route('/api/estadoIngreso', methods=['POST'])
def listarIngreso():
  datos = request.get_json()
  codigo = datos.get("codigo")
  resultado = rr.listarIngresoCambio(conexion,codigo)
  return jsonify(resultado)

@app.route('/api/estadoRetiro', methods=['POST'])
def listarRetiro():
  datos = request.get_json()
  codigo = datos.get("codigo")
  resultado = rr.listarRetiro(conexion,codigo)
  return jsonify(resultado)

if __name__ == '__main__':
  app.run(debug=True)

