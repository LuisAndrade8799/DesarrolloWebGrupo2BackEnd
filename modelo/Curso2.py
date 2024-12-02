class Curso2:
    def __init__(self,
                 codigo,
                 nombre):
        self.codigo = codigo
        self.nombre=nombre

    def toDict(self):
        return {
            "codigo":self.codigo,
            "nombre":self.nombre
        }