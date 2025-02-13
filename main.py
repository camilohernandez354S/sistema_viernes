from Controllers.ClienteController import ClienteController
from Controllers.PersonaController import PersonaController
from conexion import Conexion

# Crear la conexión a la base de datos
conexion = Conexion()
conexion.conectar()

# Inicializar los controladores con la conexión
cliente_controlador = ClienteController()
persona_controlador = PersonaController(conexion)

if __name__ == "__main__":
    while True:
        print("\nMenú CRUD")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Agregar persona")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cliente_controlador.listar_clientes()
        elif opcion == "2":
            id_cliente = int(input("Ingrese el ID del cliente: "))
            cliente_controlador.agregar_cliente(id_cliente)
        elif opcion == "3":
            id = int(input("Ingrese el ID del cliente a actualizar: "))
            id_cliente = int(input("Ingrese el nuevo ID del cliente: "))
            cliente_controlador.actualizar_cliente(id, id_cliente)
        elif opcion == "4":
            id = int(input("Ingrese el ID del cliente a eliminar: "))
            cliente_controlador.eliminar_cliente(id)
        elif opcion == "5":
            pri_nombre = input("Ingrese el primer nombre: ")
            seg_nombre = input("Ingrese el segundo nombre: ")
            pri_apellido = input("Ingrese el primer apellido: ")
            seg_apellido = input("Ingrese el segundo apellido: ")
            documento = input("Ingrese el documento: ")
            telefono = input("Ingrese el teléfono: ")
            correo_electronico = input("Ingrese el correo electrónico: ")
            direccion_residencia = input("Ingrese la dirección de residencia: ")
            fecha_registro = input("Ingrese la fecha de registro (YYYY-MM-DD): ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
            genero = input("Ingrese el género (F/M): ").upper()

            if genero not in ["F", "M"]:
                print("Error: Género inválido, debe ser 'F' o 'M'.")
            else:
                persona_controlador.agregar_persona(
                    pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, 
                    telefono, correo_electronico, direccion_residencia, fecha_registro, 
                    fecha_nacimiento, genero
                )
        elif opcion == "6":
            print("Saliendo...")
            conexion.cerrar_conexion()
            break
        else:
            print("Opción no válida, intente nuevamente.")
