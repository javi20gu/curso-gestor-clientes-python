import re
import helpers


class Cliente:

    nombre: str
    apellidos: str
    dni: str

    def __init__(self, nombre: str, apellidos: str, dni: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

    def __str__(self):
        return f"{self.dni}: {self.nombre} {self.apellidos}"


class Manager:

    __clientes: list = []

    @staticmethod
    def show_client(client: Cliente):
        """ Muestra por pantalla un cliente de forma amigable """
        print(client)

    def show_clients(self):
        """ Recorre la lista de clientes y los muetra uno a uno """
        if self.__clientes == []:
            print("No hay clientes disponibles.")
        else:
            for cliente in self.__clientes:
                Manager.show_client(cliente)

    def add(self):
        """ Añade un cliente a la lista de clientes """

        print('Introduce nombre (De 2 a 30 caracteres)')
        nombre = helpers.input_text(2, 30)
        print('Introduce apellido (De 2 a 30 caracteres)')
        apellidos = helpers.input_text(2, 30)
        while True:
            print("Introduce DNI (2 números y 1 carácter en mayúscula)")
            dni = helpers.input_text(3, 3)
            if self.is_valid(dni):
                self.__clientes.append(Cliente(nombre, apellidos, dni))
                break
            else:
                print("DNI incorrecto o en uso")
                dni = None

            

    def is_valid(self, dni: str):
        """
        Hace diferentes validaciones en el campo dni
            >>> is_valid('48H')  # No válido, en uso
        False
            >>> is_valid('X82')  # No válido, incorrecto
        False
            >>> is_valid('21A')  # Válido
        True
        """
        if not re.match('[0-9]{2}[A-Z]', dni):
            return False

        for client in self.__clientes:
            if client.dni == dni:
                return False

        return True

    def find(self):
        """ Busca un cliente y lo devuelve junto a su índice """
        dni = input("Introduce el dni del cliente\n> ")
        for i, client in enumerate(self.__clientes):
            if client.dni == dni:
                Manager.show_client(client)
                return i, client
        print("No se ha encontrado ningún cliente con ese DNI")
        return None, None

    def delete(self):
        """ Borra un cliente de la lista a partir del dni """

        i, client = self.find()

        if client:
            client = self.__clientes.pop(i)
            return True

        return False

    def edit(self):
        """ Modifica el nombre y apellido de un cliente a partir del dni """
    
        i, client = self.find()
        if client:
    
            print(f"Introduce nuevo nombre ({client.nombre})")
            self.__clientes[i].nombre = helpers.input_text(2, 30)
    
            print(f"Introduce nuevo apellido ({client.apellidos})")
            self.__clientes[i].apellidos = helpers.input_text(2, 30)
    
            return True
