##registro
class Trafico:
    def __init__(self,ipEnvia,ipRecibir,tamaño):
        self.ipEnvia = ipEnvia
        self.ipRecibir = ipRecibir
        self.tamaño = tamaño

def write(trafico):
    print('ip_enviar: ',trafico.ipEnvia,'-',end='')
    print('ip_recibir: ',trafico.ipRecibir,'-',end='')
    print('tamaño: ',trafico.tamaño)