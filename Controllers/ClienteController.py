from Models.ClienteModel import ClienteModel
from Views.ClienteView import ClienteView

class ClienteController:
    def __init__(self):
        self.modelo = ClienteModel()
        self.vista = ClienteView()
    def listar_clientes(self):
        clientes = self.modelo.obtener_clientes()
        self.vista.mostrar_clientes(clientes)

    def agregar_cliente(self, id_cliente):
        self.modelo.agregar_cliente(id_cliente)
        print("Cliente agregado exitosamente.")

    def actualizar_cliente(self, id, id_cliente):
        self.modelo.actualizar_cliente(id, id_cliente)
        print("Cliente actualizado exitosamente.")

    def eliminar_cliente(self, id):
        self.modelo.eliminar_cliente(id)
        print("Cliente eliminado exitosamente.")
