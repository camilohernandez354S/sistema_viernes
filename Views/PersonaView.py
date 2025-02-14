class PersonaView:
    def obtener_datos_persona(self):
        pri_nombre = self.validar_campo("Ingrese el primer nombre: ", minimo=4, es_numerico=False)
        seg_nombre = input("Ingrese el segundo nombre (opcional): ").strip()
        pri_apellido = self.validar_campo("Ingrese el primer apellido: ", minimo=4, es_numerico=False)
        seg_apellido = input("Ingrese el segundo apellido (opcional): ").strip()
        documento = self.validar_campo("Ingrese el número de documento: ", minimo=10, maximo=10, es_numerico=True)
        telefono = self.validar_campo("Ingrese el número de teléfono: ", minimo=10, maximo=10, es_numerico=True)
        correo_electronico = input("Ingrese el correo electrónico: ").strip()
        direccion_residencia = input("Ingrese la dirección de residencia: ").strip()
        fecha_registro = input("Ingrese la fecha de registro (YYYY-MM-DD): ").strip()
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ").strip()
        genero = self.validar_genero()

        return pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, telefono, correo_electronico, direccion_residencia, fecha_registro, fecha_nacimiento, genero

    def validar_campo(self, mensaje, minimo=0, maximo=None, es_numerico=False):
        while True:
            valor = input(mensaje).strip()

            if es_numerico:
                if not valor.isdigit():
                    self.mostrar_error("Solo se permiten números.")
                    continue
                if maximo and len(valor) != maximo:
                    self.mostrar_error(f"Debe tener exactamente {maximo} dígitos.")
                    continue
            else:
                if not valor.isalpha():
                    self.mostrar_error("Solo se permiten letras.")
                    continue
                if len(valor) < minimo:
                    self.mostrar_error(f"Debe tener al menos {minimo} caracteres.")
                    continue

            return valor

    def validar_genero(self):
        while True:
            genero = input("Ingrese el género (M/F): ").strip().upper()
            if genero in ["M", "F"]:
                return genero
            self.mostrar_error("El género debe ser 'M' o 'F'.")

    def mostrar_mensaje(self, mensaje):
        print(f"\033[32m{mensaje}")

    def mostrar_error(self, error):
        print(f"\033[31mError: {error}")
