import pyodbc

class Conexion:

    __instancia = None
    __conexion = None

    def __new__(cls, *args, **kwargs):
        if cls.__instancia is None:
            cls.__instancia = super(Conexion, cls).__new__(cls)
        return cls.__instancia

    def __init__ (self):
        self.__server = 'DESKTOP-6M2RKMO'
        self.__database = 'DesarrolloWeb'
        self.__username = 'sa'
        self.__password = '12345678'

    def getConexion(self):
        if self.__conexion is None:
            conectionstring = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.__server};DATABASE={self.__database};UID={self.__username};PWD={self.__password}'
            self.__conexion = pyodbc.connect(conectionstring)
        
        return self.__conexion





