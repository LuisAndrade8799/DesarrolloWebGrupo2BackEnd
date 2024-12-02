from sqlite3 import Connection

from modelo.Curso2 import Curso2
from modelo.Respuesta import Respuesta
from modelo.Curso import Curso

class RepositorioCurso:
    def getCursos(conexion: Connection, codigoAlumno: str):
        cursor = conexion.cursor()
        cursor.execute(
            f"""
                SELECT
                    M.id_matricula, 
                    C.codigo_curso,
                    C.descripcion_asignatura AS nombre_curso,
                    A.docente,
                    A.codigo_seccion AS seccion,
                    A.dia,
                    A.hora
                FROM 
                    Detalle_matricula AS DM
                JOIN 
                    Asignatura AS A ON DM.codigo_asignatura = A.codigo_asignatura
                JOIN 
                    Curso AS C ON A.codigo_curso = C.codigo_curso
                JOIN 
                    Matricula AS M ON DM.id_matricula = M.id_matricula
                WHERE 
                    M.codigo_alumno = '{codigoAlumno}'
                    AND M.codigo_semestre = 20242;
            """
        )
        resultado = cursor.fetchall()
        cursor.close()
        if not resultado:
            return Respuesta(False,None).toDict()
        else:
            cursos = [Curso(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6]) for fila in resultado]
            return Respuesta(True,cursos).toDict()

    def getNombreCursos(conexion: Connection):
        cursor=conexion.cursor()
        cursor.execute("SELECT codigo_curso, descripcion_asignatura AS NombreCurso from Curso")
        resultado = cursor.fetchall()
        if resultado:
            nombres = [Curso2(fila[0],fila[1]) for fila in resultado]
            return Respuesta(True, nombres).toDict()
        else:
            return Respuesta(False,None).toDict()