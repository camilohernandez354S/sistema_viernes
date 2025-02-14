from Controllers.ClienteController import ClienteController
from Controllers.PersonaController import PersonaController
from Views.PersonaView import PersonaView
from conexion import Conexion

def main():
    conexion = Conexion()
    conexion.conectar()

    cliente_controlador = ClienteController(conexion)
    persona_controlador = PersonaController(conexion)
    persona_view = PersonaView()

    while True:
        print("\nMenú CRUD")
        print("1. Mostrar clientes")
        print("2. Agregar cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Agregar persona")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente_controlador.listar_clientes()

        elif opcion == "2":
            try:
                id_cliente = int(input("Ingrese el ID del cliente: "))
                cliente_controlador.agregar_cliente(id_cliente)
            except ValueError:
                print(" Debe ingresar un número entero.")

        elif opcion == "3":
            try:
                id = int(input("Ingrese el ID del cliente a actualizar: "))
                id_cliente = int(input("Ingrese el nuevo ID del cliente: "))
                cliente_controlador.actualizar_cliente(id, id_cliente)
            except ValueError:
                print(" Ambos valores deben ser números")

        elif opcion == "4":
            try:
                id = int(input("Ingrese el ID del cliente a eliminar: "))
                cliente_controlador.eliminar_cliente(id)
            except ValueError:
                print(" Debe ingresar un número entero.")

        elif opcion == "5":  
            persona_controlador.agregar_persona()

        elif opcion == "6":
            print("Saliendo...")
            conexion.cerrar_conexion()
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
