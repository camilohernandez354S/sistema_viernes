from Models.PersonaModel import PersonaModel

class PersonaController:
    def __init__(self, conexion):
        self.modelo = PersonaModel(conexion)  

    def agregar_persona(self):
        try:
            # Primero se ingresan los nombres y apellidos
            pri_nombre = input("Ingrese el primer nombre: ").strip()
            if not pri_nombre.replace(" ", "").isalpha():
                print("\033[33mError: El primer nombre solo puede contener letras.")
                return  

            seg_nombre = input("Ingrese el segundo nombre (opcional): ").strip()
            if seg_nombre and not seg_nombre.replace(" ", "").isalpha():
                print("\033[33mError: El segundo nombre solo puede contener letras.")
                return  

            pri_apellido = input("Ingrese el primer apellido: ").strip()
            if not pri_apellido.replace(" ", "").isalpha():
                print("\033[33mError: El primer apellido solo puede contener letras.")
                return  

            seg_apellido = input("Ingrese el segundo apellido (opcional): ").strip()
            if seg_apellido and not seg_apellido.replace(" ", "").isalpha():
                print("\033[33mError: El segundo apellido solo puede contener letras.")
                return  

            
            documento = input("Ingrese el documento: ").strip()
            if not documento.isdigit():
                print("\033[33mError: El documento debe contener solo números.")
                return  

            telefono = input("Ingrese el teléfono: ").strip()
            if not telefono.isdigit():
                print("\033[33mError: El teléfono debe contener solo números.")
                return  

            genero = input("Ingrese el género (M/F): ").strip().upper()
            if genero not in ["M", "F"]:
                print("\033[33mError: El género debe ser 'M' o 'F'.")
                return  

            self.modelo.agregar_persona(pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, "", "", "", "", genero)
            print("\033[32m Persona agregada correctamente.")

        except Exception as e:
            print(f"\033[31mError inesperado: {e}")




    def listar_personas(self):
        personas = self.modelo.obtener_personas()
        if not personas:
            print("\033[31mNo hay personas registradas.")
        else:
            print("\033[33m\nLista de Personas:")
            for persona in personas:
                print(persona)
