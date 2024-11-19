class Ingreso:

    def __init__(self,
            numeroExpediente,
            codigoAlumno,
            codigoSemestre,
            codigoAsignatura,
            ingresa1,
            ingresa2,
            observacion
    ):
        self.numeroExpediente = numeroExpediente
        self.codigoAlumno = codigoAlumno
        self.codigoSemestre = codigoSemestre
        self.codigoAsignatura = codigoAsignatura
        self.ingresa1 = ingresa1
        self.ingresa2 = ingresa2
        self.observacion = observacion
    
    def toDict(self):
        return {
            "numeroExpediente": self.numeroExpediente,
            "codigoAlumno": self.codigoAlumno,
            "codigoSemestre": self.codigoSemestre,
            "codigoAsignatura": self.codigoAsignatura,
            "ingresa1": self.ingresa1,
            "ingresa2": self.ingresa2,
            "observacion": self.observacion
        }