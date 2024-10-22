import json

class Usuario:

    def __init__ (self,
                 idUsuario,
                 codigo,
                 correoAlumno,
                 nombreRol):
        self.idUsuario = idUsuario
        self.codigo = codigo
        self.correoAlumno = correoAlumno
        self.nombreRol = nombreRol
    
    def toDict(self):
        return {
            "idUsuario": self.idUsuario,
            "codigo": self.codigo,
            "correoAlumno": self.correoAlumno,
            "nombreRol": self.nombreRol
        }