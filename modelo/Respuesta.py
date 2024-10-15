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
            return {
                "resultado": self.__resultado,         
                "objeto": self.__objeto.toDict()
            }