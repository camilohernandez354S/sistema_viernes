from conexion import Conexion

class ClienteModel:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar_cliente(self, id_persona):
        try:
            cursor = self.conexion.conexion.cursor()
            query = "INSERT INTO clientes (id_persona) VALUES (%s)"
            valores = (id_persona,)
            cursor.execute(query, valores)
            self.conexion.conexion.commit()
            cursor.close()
        except Exception as e:
            return False  # Indica que hubo un error

    def obtener_clientes(self):
        cursor = self.conexion.conexion.cursor()
        query = """
            SELECT clientes.id AS id_cliente, personas.id AS id_persona, 
                personas.documento, personas.pri_nombre, personas.pri_apellido
            FROM clientes 
            JOIN personas ON clientes.id_persona = personas.id
        """
        cursor.execute(query)
        clientes = cursor.fetchall()
        cursor.close()
        return clientes

    def actualizar_cliente(self, id, nuevo_id=None, nuevo_nombre=None, nuevo_apellido=None):
        try:
            cursor = self.conexion.conexion.cursor()
            
            # Obtener los valores actuales
            query_select = """
                SELECT clientes.id, clientes.id_persona, personas.pri_nombre, personas.pri_apellido
                FROM clientes 
                JOIN personas ON clientes.id_persona = personas.id 
                WHERE clientes.id = %s
            """
            cursor.execute(query_select, (id,))
            cliente = cursor.fetchone()
            
            if not cliente:
                return False  # Indica que el cliente no existe
            
            id_actual, id_persona, nombre_actual, apellido_actual = cliente
            
            # Usar los valores nuevos si se proporcionan, sino mantener los antiguos
            nuevo_id = nuevo_id if nuevo_id else id_actual
            nuevo_nombre = nuevo_nombre if nuevo_nombre else nombre_actual
            nuevo_apellido = nuevo_apellido if nuevo_apellido else apellido_actual
            
            # Actualizar en la base de datos
            query_update = "UPDATE clientes SET id = %s WHERE id = %s"
            cursor.execute(query_update, (nuevo_id, id))
            
            query_update_persona = "UPDATE personas SET pri_nombre = %s, pri_apellido = %s WHERE id = %s"
            cursor.execute(query_update_persona, (nuevo_nombre, nuevo_apellido, id_persona))
            
            self.conexion.conexion.commit()
            cursor.close()
            return True  # Indica que la actualización fue exitosa
            
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False  


    def eliminar_cliente(self, id):
        try:
            cursor = self.conexion.conexion.cursor()
            query = "DELETE FROM clientes WHERE id = %s"
            valores = (id,)
            cursor.execute(query, valores)
            self.conexion.conexion.commit()
            cursor.close()
            return True  # Indica que la eliminación fue exitosa
        except Exception:
            return False  # Indica que hubo un error
            
    def obtener_cliente_por_id(self, id):
        cursor = self.conexion.conexion.cursor() 
        query = "SELECT * FROM clientes WHERE id = %s"
        cursor.execute(query, (id,))
        cliente = cursor.fetchone()  
        cursor.close() 
        return cliente  # Devuelve None si el cliente no existe