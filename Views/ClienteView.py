class ClienteView:
    def mostrar_clientes(self, clientes):
        for cliente in clientes:
            print(f"ID: {cliente[0]}, ID Cliente: {cliente[1]}")
