class Curso:
    def __init__ (self,
            idMatricula,
            codigoCurso,
            nombreCurso,
            docente,
            seccion,
            dia,
            hora
    ):
        self.idMatricula = idMatricula
        self.codigoCurso = codigoCurso
        self.nombreCurso = nombreCurso
        self.docente = docente
        self.seccion = seccion
        self.dia = dia
        self.hora = hora
    
    def toDict(self):
        return {
            "codigoCurso" : self.codigoCurso,
            "nombreCurso" : self.nombreCurso,
            "docente" : self.docente,
            "seccion" : self.seccion,
            "dia" : self.dia,
            "hora" : self.hora
        }