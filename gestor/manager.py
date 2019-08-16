import re
import helpers
from os import remove
from os.path import join

from gestor_ficheros import GestorFicheros
from config import Cliente, DataPath

class Manager:

    __clientes: list = []

    def __init__(self):
        self.__clientes = GestorFicheros.loadClient()
        print(self.__clientes)

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
                GestorFicheros.writeCliente(dni, nombre, apellidos)
                self.__clientes.append(Cliente(nombre, apellidos, dni))
                break
            else:
                print("DNI incorrecto o en uso")
                dni = None            

    def is_valid(self, dni: str):
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
            remove(join(DataPath, '{}.json'.format(client.dni)))
            return True

        return False

    def edit(self):
        """ Modifica el nombre y apellido de un cliente a partir del dni """
    
        i, client = self.find()
        if client:
    
            print(f"Introduce nuevo nombre ({client.nombre})")
            nombre = helpers.input_text(2, 30)
            self.__clientes[i].nombre = nombre

            print(f"Introduce nuevo apellido ({client.apellidos})")
            apellidos = helpers.input_text(2, 30)
            self.__clientes[i].apellidos = apellidos

            GestorFicheros.writeCliente(client.dni, nombre, apellidos)

            return True
