from Models.ClienteModel import ClienteModel

class ClienteController:
    def __init__(self, conexion):
        self.modelo = ClienteModel(conexion)

    def listar_clientes(self):
        clientes = self.modelo.obtener_clientes()
        for cliente in clientes:
            id_cliente, id_persona, documento, pri_nombre, pri_apellido = cliente
            print(f"ID Cliente: {id_cliente}, ID Persona: {id_persona}, Documento: {documento}, Nombre: {pri_nombre}, Apellido: {pri_apellido}")

    def agregar_cliente(self, id_cliente):
        if not isinstance(id_cliente, int):
            print("El ID del cliente debe ser un número entero válido.")
            return
        
        self.modelo.agregar_cliente(id_cliente)
        print("Cliente agregado correctamente.")
    def actualizar_cliente(self, id, nuevo_id=None, nuevo_nombre=None, nuevo_apellido=None):
        cliente_existente = self.modelo.obtener_cliente_por_id(id)
        if not cliente_existente:
            print("El cliente con el ID ingresado no existe.")
            return
        
        # Permitir que el usuario ingrese solo lo que quiere actualizar.
        if nuevo_id is None:
            nuevo_id = input("Ingrese el nuevo ID del cliente (o presione Enter para mantener el actual): ").strip() or None
            nuevo_id = int(nuevo_id) if nuevo_id else None
        if nuevo_nombre is None:
            nuevo_nombre = input("Ingrese el nuevo nombre del cliente (o presione Enter para mantener el actual): ").strip() or None
        if nuevo_apellido is None:
            nuevo_apellido = input("Ingrese el nuevo apellido del cliente (o presione Enter para mantener el actual): ").strip() or None

        resultado = self.modelo.actualizar_cliente(id, nuevo_id, nuevo_nombre, nuevo_apellido)
        if resultado:
            print("Cliente actualizado correctamente.")
        else:
            print("Error al actualizar cliente.")


    def eliminar_cliente(self, id):
        if not isinstance(id, int):
            print("El ID debe ser un número entero válido.")
            return

        cliente_existente = self.modelo.obtener_cliente_por_id(id)
        if not cliente_existente:
            print("Cliente no encontrado. No se puede eliminar.")
            return

        self.modelo.eliminar_cliente(id)
        print(" Cliente eliminado correctamente.")
