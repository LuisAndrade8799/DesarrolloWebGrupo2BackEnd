class Retiro:

    def __init__(self,
            numeroExpediente,
            codigoAlumno,
            codigoSemestre,
            codigoAsignatura,
            retiro,
            observacion
    ):
        self.numeroExpediente = numeroExpediente
        self.codigoAlumno = codigoAlumno
        self.codigoSemestre = codigoSemestre
        self.codigoAsignatura = codigoAsignatura
        self.retiro = retiro
        self.observacion = observacion

    def toDict(self):
        return {
            "numeroExpediente":self.numeroExpediente,
            "codigoAlumno":self.codigoAlumno,
            "codigoSemestre":self.codigoSemestre,
            "codigoAsignatura":self.codigoAsignatura,
            "retiro":self.retiro,
            "observacion":self.observacion
        }