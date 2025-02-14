class PersonaView:
    def obtener_datos_persona(self):
        pri_nombre = input("Ingrese el primer nombre: ").strip()
        seg_nombre = input("Ingrese el segundo nombre (opcional): ").strip()
        pri_apellido = input("Ingrese el primer apellido: ").strip()
        seg_apellido = input("Ingrese el segundo apellido (opcional): ").strip()
        documento = input("Ingrese el número de documento: ").strip()
        telefono = input("Ingrese el número de teléfono: ").strip()
        correo_electronico = input("Ingrese el correo electrónico: ").strip()
        direccion_residencia = input("Ingrese la dirección de residencia: ").strip()
        fecha_registro = input("Ingrese la fecha de registro (YYYY-MM-DD): ").strip()
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ").strip()
        genero = input("Ingrese el género (M/F): ").strip().upper()

        return pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_registro, fecha_nacimiento, genero

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_error(self, error):
        print(f" Error: {error}") #mensaje de error
