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

    def toJSON(self):
        return json.dumps(self.__dict__)