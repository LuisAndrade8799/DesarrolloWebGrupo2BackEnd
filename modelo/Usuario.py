import json

class Usuario:

    def __init__ (self,
                 idUsuario,
                 correoAlumno,
                 contrasenia,
                 nombreRol):
        self.idUsuario = idUsuario
        self.correoAlumno = correoAlumno
        self.contrasenia = contrasenia
        self.nombreRol = nombreRol
    
    def toDict(self):
        return {
            "idUsuario": self.idUsuario,
            "correoAlumno": self.correoAlumno,
            "contrasenia": self.contrasenia,
            "nombreRol": self.nombreRol
        }