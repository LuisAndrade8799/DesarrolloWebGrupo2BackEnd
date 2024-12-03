from sqlite3 import Connection
from modelo.IngresoCambio import IngresoCambio
from modelo.Respuesta import Respuesta
from modelo.Ingreso import Ingreso
from modelo.Retiro import Retiro
from modelo.Retiro2 import Retiro2


class RepositorioRectificar:

    def insertarRecti(conexion: Connection, datos):
        cursor = conexion.cursor()
        codigo = datos.get("codigoAlumno")
        expediente = datos.get("expediente")
        idMatricula = datos.get("idMatricula")
        rectificar = datos.get("rectificar")
        ingreso = datos.get("cursosNuevos")
        try:
            cursor.execute(
                f"""
                    insert into Rectificacion (numero_expediente, id_matricula, codigo_alumno)
                    values ('{expediente}','{idMatricula}','{codigo}')
                """
            )
            
            # Procesar cursos para rectificación, retiro y nuevos ingresos
            for curso in rectificar:
                codigoAsignatura = curso.get("codigo")
                cambio = curso.get("cambio")
                retiro = curso.get("retiro")
                seccion = curso.get("seccion")
                motivo = curso.get("motivo")
                nuevaSeccion = curso.get("nuevaSeccion")
                nuevaSeccion2 = curso.get("nuevaSeccion2")

                if cambio:
                    cursor.execute(
                        f"""
                            insert into IngresoCambio (numero_expediente,codigo_curso,seccion,ingresa,ingresa_2, observacion, aprobado)
                            values ('{expediente}','{codigoAsignatura}',{seccion},{nuevaSeccion},{nuevaSeccion2},'{motivo}', null)
                        """
                    )
                    
                if retiro:
                    cursor.execute(
                        f"""
                            insert into Retiro (numero_expediente,codigo_curso,retiro, observacion, aprobado)
                            values ('{expediente}','{codigoAsignatura}',{seccion},'{motivo}', null)
                        """
                    )
                
            # Nuevo curso: Insertar en IngresoCambio con el campo "ingresa1" para la sección del nuevo curso
            if ingreso:
                for curso in ingreso:
                    codigoAsignatura = curso.get("codigo")
                    seccion = curso.get("seccion")
                    print(seccion)
                    motivo = curso.get("motivo")
                    nuevaSeccion = curso.get("nuevaSeccion")
                    nuevaSeccion2 = curso.get("nuevaSeccion2")
                    cursor.execute(
                        f"""
                            insert into IngresoCambio (numero_expediente,codigo_curso,seccion,ingresa,ingresa_2, observacion, aprobado)
                            values ('{expediente}','{codigoAsignatura}',{seccion},{nuevaSeccion},{nuevaSeccion2},'{motivo}', null)
                        """
                    )
            conexion.commit()
            cursor.close()
            return Respuesta(True, None).toDict()
        except Exception as e:
            print(f"Error al insertar rectificación: {e}")
            conexion.rollback()
            cursor.close()
            return Respuesta(False, None).toDict()

    
    def getIngresos(conexion: Connection):
        cursor = conexion.cursor()
        cursor.execute(
            f"""
                SELECT
                	ic.numero_expediente,
                    m.codigo_alumno,
                    m.codigo_semestre,
                    ic.codigo_curso AS codigo_curso_ingreso,
                    ic.ingresa,
                    ic.ingresa_2,
                    ic.observacion AS observacion_ingreso
                FROM
                    IngresoCambio ic
                LEFT JOIN
                    Rectificacion re ON ic.numero_expediente = re.numero_expediente
                LEFT JOIN
                	Matricula m ON re.id_matricula = m.id_matricula
                WHERE
                    (m.codigo_semestre = 20242 AND ic.aprobado is null);
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
	                r.numero_expediente,
                    m.codigo_alumno,
                    m.codigo_semestre,
                    r.codigo_curso AS codigo_curso_retiro,
                    r.retiro,
                    r.observacion AS observacion_ingreso
                FROM
                    Retiro r
                LEFT JOIN
                    Rectificacion re ON r.numero_expediente = re.numero_expediente
                LEFT JOIN
                	Matricula m ON re.id_matricula = m.id_matricula
                WHERE
                    (m.codigo_semestre = 20242 AND r.aprobado is null);
            """
        )
        resultado = cursor.fetchall()
        cursor.close()
        if not resultado:
            return Respuesta(False,None).toDict()
        else:
            cursos = [Retiro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]) for fila in resultado]
            return Respuesta(True,cursos).toDict()
        
    def listarIngresoCambio(conexion:Connection, codigo):
        cursor = conexion.cursor()
        cursor.execute(
            f"""
                select * from Rectificacion
                inner join IngresoCambio on IngresoCambio.numero_expediente = Rectificacion.numero_expediente
                where Rectificacion.codigo_alumno = '{codigo}';
            """
        )
        resultado = cursor.fetchall()
        cursor.close()
        if resultado:
            ingreso = [IngresoCambio(fila[0],fila[1],fila[2],fila[3],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10]) for fila in resultado]
            return Respuesta(True,ingreso).toDict()
        else:
            return Respuesta(False,None).toDict()
        
    def listarRetiro(conexion:Connection, codigo):
        cursor = conexion.cursor()
        cursor.execute(
            f"""
                select * from Rectificacion
                inner join Retiro on Retiro.numero_expediente = Rectificacion.numero_expediente
                where Rectificacion.codigo_alumno = '{codigo}';
            """
        )
        resultado = cursor.fetchall()
        cursor.close()
        if resultado:
            retiro = [Retiro2(fila[0],fila[1],fila[2],fila[3],fila[5],fila[6],fila[7],fila[8]) for fila in resultado]
            return Respuesta(True,retiro).toDict()
        else:
            return Respuesta(False,None).toDict()