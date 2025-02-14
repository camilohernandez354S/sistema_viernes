import re

class PersonaModel:
    def __init__(self, conexion):
        self.conexion = conexion

    def agregar_persona(self, pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_registro, fecha_nacimiento, genero):
        try:
            cursor = self.conexion.conexion.cursor()
            query = """INSERT INTO personas (pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, 
                                             correo_electronico, direccion_residencia, fecha_registro, fecha_nacimiento, genero) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            valores = (pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_registro, fecha_nacimiento, genero)
            cursor.execute(query, valores)
            self.conexion.conexion.commit()
            cursor.close()
            return True  
        except Exception as e:
            print(f"\033[31mError al agregar persona: {e}")  # Ahora mostrará el error exacto
            return False  


    def obtener_personas(self):
        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute("SELECT * FROM personas")
            personas = cursor.fetchall()
            cursor.close()
            return personas
        except Exception:
            return []
