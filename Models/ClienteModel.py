from conexion import Conexion

class ClienteModel:
    def __init__(self):
        self.db = Conexion()

    def obtener_clientes(self):
        self.db.conectar()
        cursor = self.db.conexion.cursor()
        cursor.execute("SELECT id, id_cliente FROM clientes")
        clientes = cursor.fetchall()
        self.db.cerrar_conexion()
        return clientes

    def agregar_cliente(self, id_cliente):
        self.db.conectar()
        cursor = self.db.conexion.cursor()
        cursor.execute("INSERT INTO clientes (id_cliente) VALUES (%s)", (id_cliente,))
        self.db.conexion.commit()
        self.db.cerrar_conexion()

    def actualizar_cliente(self, id, id_cliente):
        self.db.conectar()
        cursor = self.db.conexion.cursor()
        cursor.execute("UPDATE clientes SET id_cliente = %s WHERE id = %s", (id_cliente, id))
        self.db.conexion.commit()
        self.db.cerrar_conexion()

    def eliminar_cliente(self, id):
        self.db.conectar()
        cursor = self.db.conexion.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        self.db.conexion.commit()
        self.db.cerrar_conexion()