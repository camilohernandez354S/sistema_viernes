from Models.PersonaModel import PersonaModel

class PersonaController:
    def __init__(self, conexion):
        self.modelo = PersonaModel(conexion)

    def agregar_persona(self, pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_registro, fecha_nacimiento, genero):
        # Validar que el género sea 'M' o 'F'
        if genero not in ['M', 'F']:
            print(" Error: El género debe ser 'M' o 'F'.")
            return
        
        # Intentar agregar la persona
        if self.modelo.agregar_persona(pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_registro, fecha_nacimiento, genero):
            print(" Persona agregada correctamente.")
        else:
            print(" Error al agregar la persona.")

    def listar_personas(self):
        personas = self.modelo.obtener_personas()
        if not personas:
            print(" No hay personas registradas.")
        else:
            print("\n Lista de Personas:")
            for persona in personas:
                print(persona)
