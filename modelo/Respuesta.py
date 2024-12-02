from modelo.Curso import Curso
class Respuesta:

    def __init__(self, resultado, objeto):
        self.__resultado = resultado
        self.__objeto = objeto

    def toDict(self):
        if self.__objeto is None:
            return {
                "resultado": self.__resultado,         
                "objeto": None
            }
        else:
            if isinstance(self.__objeto, list):
                if isinstance(self.__objeto[0],Curso):
                    return {
                        "resultado":self.__resultado,
                        "idMatricula": self.__objeto[0].idMatricula,
                        "objetos": [objeto.toDict() for objeto in self.__objeto]
                    }
                else:
                    if isinstance(self.__objeto[0],str):
                        return{
                            "resultado":self.__resultado,
                            "nombres": [nombre for nombre in self.__objeto]
                        }
                    else:
                        return {
                            "resultado":self.__resultado,
                            "objetos": [objeto.toDict() for objeto in self.__objeto]
                        }
            return {
                "resultado": self.__resultado,         
                "objeto": self.__objeto.toDict()
            }