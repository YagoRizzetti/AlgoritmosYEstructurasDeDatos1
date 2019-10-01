__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

class Cuota:
    def __init__(self, socio, deporte, dia, valor):
        self.socio = socio
        self.deporte = deporte
        self.dia = dia
        self.valor = valor

def to_string(reg):
    return '{:<6}{:<10}{:>4}  ${:>5}'.format(reg.socio, describir_deporte(reg.deporte), reg.dia,reg.valor)

def to_string_titulos():
    return '{:<6}{:<10}{:>4}{:>8}'.format('Socio', 'Deporte', 'Dia','Valor')

def describir_deporte(cod):
    deportes = ['Natacion','Basquet','Karate','Futbol','Patin']
    return str(cod) + '-' + deportes[cod]