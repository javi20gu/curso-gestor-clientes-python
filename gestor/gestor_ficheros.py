from json import dump, load
from os.path import join

from config import DataPath, Cliente


class GestorFicheros:

    @staticmethod
    def loadClient():
        #Cliente(data["nombre"], data["apellidos"], dni)
        return [
            GestorFicheros.readCliente(file.resolve().stem)
            for file in list(DataPath.glob('*'))
        ]
       
        #return [file.resolve().stem for file in )]

    @staticmethod
    def readCliente(dni):
        if DataPath.exists():
            with open('{}.json'.format(join(DataPath, dni))) as fichero:
                data = load(fichero)
                return Cliente(data["nombre"], data["apellidos"], dni)
        else:
            raise FileNotFoundError("Fichero No Existente: {}".format('{}.json'.format(join(DataPath, dni))))

    @staticmethod
    def writeCliente(dni: str, nombre: str, apellidos: str):
        if DataPath.exists():
            with open('{}.json'.format(join(DataPath, dni)), 'w') as fichero:
                dump({'nombre': nombre, 'apellidos': apellidos}, fichero, indent=4)
