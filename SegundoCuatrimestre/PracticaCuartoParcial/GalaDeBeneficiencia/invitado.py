__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

class Invitado:
    def __init__(self,nombre, mesa, ong, monto):
        self.nombre = nombre
        self.mesa = mesa
        self.ong = ong
        self.monto = monto


def to_string(invitado):
    txt = '{:<30}'.format(invitado.nombre)
    txt += '{:<5}'.format(invitado.mesa)
    txt += '{:<30}'.format(describir_ong(invitado.ong))
    txt += '${:<8.2f}'.format(invitado.monto)
    return txt


def describir_ong(codigo):
    ongs = ['Missing Children','Caritas','PUPI','Médicos Sin Fronteras','Vida Silvestre',
            'Aldeas','Fundaleu','Cimientos','Uniendo Caminos','Adoptare']
    return ongs[codigo]



