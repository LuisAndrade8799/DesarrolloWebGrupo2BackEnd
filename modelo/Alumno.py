import json

class Alumno:
    

    def __init__ (self,
                  codigoAlumno,
                  apellidoPaterno,
                  apellidoMaterno,
                  nombreAlumno,
                  anioIngreso,
                  correoAlumno,
                  codigoPlan):
        self.codigoAlumno = codigoAlumno
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.nombreAlumno = nombreAlumno
        self.anioIngreso = anioIngreso
        self.correoAlumno = correoAlumno
        self.codigoPlan = codigoPlan

    def toDict(self):
        return {
            "codigoAlumno": self.codigoAlumno,
            "apellidoPaterno": self.apellidoPaterno,
            "apelligoMaterno": self.apellidoMaterno,
            "nombreAlumno": self.nombreAlumno,
            "anioIngreso": self.anioIngreso,
            "correoAlumno": self.correoAlumno,
            "codigoPlan": self.codigoPlan
        }