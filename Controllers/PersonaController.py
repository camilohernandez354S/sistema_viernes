from Models.PersonaModel import PersonaModel
from Views.PersonaView import PersonaView

class PersonaController:
    def __init__(self, conexion):
        self.modelo = PersonaModel(conexion)
        self.vista = PersonaView()

    def agregar_persona(self):
        try:
            datos = self.vista.obtener_datos_persona()
            pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_registro, fecha_nacimiento, genero = datos  # Ahora son 11 valores

            if self.modelo.agregar_persona(pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_registro, fecha_nacimiento, genero):
                self.vista.mostrar_mensaje("Persona agregada correctamente.")
            else:
                self.vista.mostrar_error("No se pudo agregar la persona.")

        except Exception as e:
            self.vista.mostrar_error(f"Error inesperado: {e}")


    def listar_personas(self):
        personas = self.modelo.obtener_personas()
        if not personas:
            self.vista.mostrar_error("No hay personas registradas.")
        else:
            self.vista.mostrar_mensaje("\nLista de Personas:")
            for persona in personas:
                print(persona)
