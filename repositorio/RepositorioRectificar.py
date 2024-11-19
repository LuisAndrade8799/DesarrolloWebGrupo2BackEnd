from sqlite3 import Connection
from modelo.Respuesta import Respuesta
from modelo.Ingreso import Ingreso
from modelo.Retiro import Retiro


class RepositorioRectificar:

    def insertarRecti(conexion: Connection, datos):
        cursor = conexion.cursor()
        codigo = datos.get("codigoAlumno")
        expediente = datos.get("expediente")
        idMatricula = datos.get("idMatricula")
        try:
            cursor.execute(
                f"""
                    insert into Rectificacion (numero_expediente, id_matricula, codigo_alumno)
                    values ('{expediente}','{idMatricula}','{codigo}')
                """
            )
            
            for curso in datos.get("rectificar"):
                codigoAsignatura = curso.get("codigo")
                print("codigo asignatura: "+codigoAsignatura)
                cambio = curso.get("cambio")
                retiro = curso.get("retiro")
                seccion = curso.get("seccion")
                motivo = curso.get("motivo")
                nuevaSeccion = curso.get("nuevaSeccion")
                nuevaSeccion2 = curso.get("nuevaSeccion2")

                if cambio:
                    print("Se ingreso el cambio")
                    cursor.execute(
                        f"""
                            insert into IngresoCambio (numero_expediente,codigo_asignatura,ingresa,ingresa_2, observacion, aprobado)
                            values ('{expediente}','{codigoAsignatura}',{nuevaSeccion},{nuevaSeccion2},'{motivo}', null)
                        """
                    )
                    

                if retiro:
                    print("Se ingreso el retiro")
                    cursor.execute(
                        f"""
                            insert into Retiro (numero_expediente,codigo_asignatura,retiro, observacion, aprobado)
                            values ('{expediente}','{codigoAsignatura}',{seccion},'{motivo}', null)
                        """
                    )
            cursor.commit()
            cursor.close()
            return Respuesta(True,None).toDict()
        except:
            cursor.commit()
            cursor.close()
            return Respuesta(False,None).toDict()
    
    def getIngresos(conexion: Connection):
        cursor = conexion.cursor()
        cursor.execute(
            f"""
                SELECT
                	re.numero_expediente,
                    m.codigo_alumno,
                    m.codigo_semestre,
                    ic.codigo_asignatura AS codigo_asignatura_ingreso,
                    ic.ingresa,
                    ic.ingresa_2,
                    ic.observacion AS observacion_ingreso
                FROM
                    Matricula m
                LEFT JOIN
                    Rectificacion re ON m.id_matricula = re.id_matricula
                LEFT JOIN
                    IngresoCambio ic ON re.numero_expediente = ic.numero_expediente
                WHERE
                    m.codigo_semestre = 20242 AND ic.aprobado is null;
            """
        )
        resultado = cursor.fetchall()
        cursor.close()
        if not resultado:
            return Respuesta(False,None).toDict()
        else:
            cursos = [Ingreso(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6]) for fila in resultado]
            return Respuesta(True,cursos).toDict()
        
    def getRetiro(conexion: Connection):
        cursor = conexion.cursor()
        cursor.execute(
            f"""
                SELECT
                	re.numero_expediente,
                    m.codigo_alumno,
                    m.codigo_semestre,
                    r.codigo_asignatura AS codigo_asignatura_retiro,
                    r.retiro,
                    r.observacion AS observacion_retiro
                FROM
                    Matricula m
                LEFT JOIN
                    Rectificacion re ON m.id_matricula = re.id_matricula
                LEFT JOIN
                  Retiro r ON re.numero_expediente = r.numero_expediente
                WHERE
                    m.codigo_semestre = 20242 AND r.aprobado is null;
            """
        )
        resultado = cursor.fetchall()
        cursor.close()
        if not resultado:
            return Respuesta(False,None).toDict()
        else:
            cursos = [Retiro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]) for fila in resultado]
            return Respuesta(True,cursos).toDict()