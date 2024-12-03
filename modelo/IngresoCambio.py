class IngresoCambio:
    def __init__(self,
                 numeroExpediente,
                 idMatricula,
                 codigoAlumno,
                 idIngresoCambio,
                 codigoCurso,
                 seccion,
                 ingresa1,
                 ingresa2,
                 observacion,
                 estado
                 ):
        self.numeroExpediente = numeroExpediente
        self.idMatricula = idMatricula
        self.codigoAlumno = codigoAlumno
        self.idIngresoCambio = idIngresoCambio
        self.codigoCurso = codigoCurso
        self.seccion = seccion
        self.ingresa1 = ingresa1
        self.ingresa2 = ingresa2
        self.observacion = observacion
        self.estado = estado

    def toDict(self):
        return {
            "numeroExpediente":self.numeroExpediente,
            "idMatricula":self.idMatricula,
            "codigoAlumno":self.codigoAlumno,
            "idIngresoCambio":self.idIngresoCambio,
            "codigoCurso":self.codigoCurso,
            "seccion":self.seccion,
            "ingresa1":self.ingresa1,
            "ingresa2":self.ingresa2,
            "observacion":self.observacion,
            "estado":self.estado
        }
