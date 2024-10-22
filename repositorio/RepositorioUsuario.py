from sqlite3 import Connection
from warnings import catch_warnings
from modelo.Alumno import Alumno
from modelo.Usuario import Usuario
from modelo.Respuesta import Respuesta


class RepositorioUsuario:

    def getUsuario(conexion: Connection, usuario: str, contrasenia : str):
        cursor = conexion.cursor()
        cursor.execute(f"""
                            select id_usuario,Usuario.codigo_alumno,Alumno.correo_alumno, contraseña, Rol.nombre from Usuario 
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
            if contrasenia != dato[3]:
                datoUsuario = None
                respuesta = False
                return Respuesta(respuesta,datoUsuario).toDict()
            else:
                respuesta = True
                datoUsuario = Usuario(dato[0],dato[1],dato[2],dato[4])
                return Respuesta(respuesta,datoUsuario).toDict()
            
    def getMatriculado(conexion: Connection, codigo: str):
        cursor = conexion.cursor()
        cursor.execute(f"""
                            select * from Alumno where codigo_alumno = '{codigo}';
                        """)
        resultado = cursor.fetchall()
        cursor.close()
        if not resultado:
            respuesta = False
            return Respuesta(respuesta,None).toDict()
        else:
            fila = resultado.pop()
            respuesta = True
            dato = Alumno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            return Respuesta(respuesta,dato).toDict()
        
    def registrar(conexion: Connection, id_usuario: str,codigo_alumno: str, contrasenia: str):
        cursor = conexion.cursor()
        try:
            cursor.execute(f"""
                            insert into Usuario (id_usuario, codigo_alumno, contraseña, id_rol)
                            values ('{id_usuario}', '{codigo_alumno}', '{contrasenia}', 1);
                        """)
            cursor.commit()
            cursor.close()
            return Respuesta(True,None).toDict()
        except:
            cursor.commit()
            cursor.close()
            return Respuesta(False,None).toDict()