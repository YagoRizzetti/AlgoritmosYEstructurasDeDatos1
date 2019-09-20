class Serie:
    def __init__(self, titulo, genero, idioma, temporadas, duracion):
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.temporadas = temporadas
        self.duracion = duracion

def write(serie):
    print("Titulo: ", serie.titulo , "-", end=" ")
    print("Genero: ", serie.genero , "-", end=" ")
    print("idioma: ", serie.idioma , "-", end=" ")
    print("Temporadas: ", serie.temporadas , "-", end=" ")
    print("duracion: ", serie.duracion )
