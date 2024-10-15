from sqlite3 import Connection
from modelo.Usuario import Usuario
from modelo.Respuesta import Respuesta


class RepositorioUsuario:

    def getUsuario(conexion: Connection, usuario: str, contrasenia : str):
        cursor = conexion.cursor()
        cursor.execute(f"""
                            select id_usuario,Alumno.correo_alumno, contraseña, Rol.nombre from Usuario 
                            inner join Alumno
                            on Alumno.correo_alumno collate Latin1_General_Bin = '{usuario}' collate Latin1_General_Bin or Usuario.id_usuario collate Latin1_General_Bin = '{usuario}' collate Latin1_General_Bin
                            inner join Rol
                            on Rol.id_rol = Usuario.id_rol;
                        """)
        resultado = cursor.fetchall()
        cursor.close()
        if not resultado:
            datoUsuario = None
            respuesta = False
            return Respuesta(respuesta,datoUsuario).toDict()
        else:
            dato = resultado.pop()
            if contrasenia != dato[2]:
                datoUsuario = None
                respuesta = False
                return Respuesta(respuesta,datoUsuario).toDict()
            else:
                respuesta = True
                datoUsuario = Usuario(dato[0],dato[1],dato[2],dato[3])
                return Respuesta(respuesta,datoUsuario).toDict()
            
