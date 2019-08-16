from pathlib import Path 


DataPath = Path(r".\clientes").absolute()


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
