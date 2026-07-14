from datetime import date
from dateutil.relativedelta import relativedelta

class Persona:
    'Clase que representa al tipo persona'
    contador = 0

    def __init__(self, nombre, ci, fechaNac, trabajos=None, sueldo=0.0):
        self.nombre = nombre
        self.ci = ci
        self.fechaNac = fechaNac
        self.trabajos = trabajos if trabajos is not None else []
        self.sueldo = sueldo
        Persona.contador += 1

    def dar_aumento_sueldo(self):
        self.sueldo += self.sueldo * 0.1

    def obtener_edad(self):
        return relativedelta(date.today(), self.fechaNac).years

    def agregar_trabajo(self, nuevo):
        self.trabajos.append(nuevo)
