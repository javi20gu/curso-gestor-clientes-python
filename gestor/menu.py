""" Menú del programa """

import helpers
import manager


class Menu(manager.Manager):

    def __init__(self):
        super().__init__()
        while True:

            helpers.clear()
    
            print("========================")
            print("  BIENVENIDO AL GESTOR  ")
            print("========================")
            print("[1] Listar clientes     ")
            print("[2] Mostrar cliente     ")
            print("[3] Añadir cliente      ")
            print("[4] Modificar cliente   ")
            print("[5] Borrar cliente      ")
            print("[6] Salir               ")
            print("========================")
    
            option = input("> ")
    
            helpers.clear()
    
            if option == '1':
                print("Listando los clientes...\n")
                self.show_clients()
            if option == '2':
                print("Mostrando un cliente...\n")
                self.find()
            if option == '3':
                print("Añadiendo un cliente...\n")
                self.add()
                print("Cliente añadido correctamente\n")
            if option == '4':
                print("Modificando un cliente...\n")
                if self.edit():
                    print("Cliente modificado correctamente\n")
            if option == '5':
                print("Borrando un cliente...\n")
                if self.delete():
                    print("Cliente borrado correctamente\n")
            if option == '6':
                print("Saliendo...\n")
                break
    
            input("\nPresiona ENTER para continuar...")


menu = Menu()