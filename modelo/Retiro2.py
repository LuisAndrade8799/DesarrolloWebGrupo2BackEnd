class Retiro2:
    
    def __init__(self,
                 numeroExpediente,
                 idMatricula,
                 codigoAlumno,
                 idRetiro,
                 codigoCurso,
                 retiro,
                 observacion,
                 estado
                 ):
        self.numeroExpediente= numeroExpediente
        self.idMatricula= idMatricula
        self.codigoAlumno= codigoAlumno
        self.idRetiro= idRetiro
        self.codigoCurso= codigoCurso
        self.retiro= retiro
        self.observacion= observacion
        self.estado= estado

    def toDict(self):
        return {
            "numeroExpediente":self.numeroExpediente,
            "idMatricula":self.idMatricula,
            "codigoAlumno":self.codigoAlumno,
            "idRetiro":self.idRetiro,
            "codigoCurso":self.codigoCurso,
            "retiro":self.retiro,
            "observacion":self.observacion,
            "estado":self.estado
        }