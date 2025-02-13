import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        self.host = 'localhost'  
        self.user = 'root'  
        self.password = ''  
        self.database = 'ventas_2025'  # Base de datos
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar_conexion(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")
