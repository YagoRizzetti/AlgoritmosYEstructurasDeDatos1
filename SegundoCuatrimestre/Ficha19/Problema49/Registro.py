class Socio:
    def __init__(self,id,nombre,arancel,deporte):
        self.id = id
        self.nombre = nombre
        self.arancel = arancel
        self.deporte = deporte

def write(socio):
    print("ID: ", socio.id, "-", end=" ")
    print("Nombre: ", socio.nombre, "-", end=" ")
    print("Arancel: ", socio.arancel, "-", end=" ")
    print("Deporte: ", socio.deporte)
