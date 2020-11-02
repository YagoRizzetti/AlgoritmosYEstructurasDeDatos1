class Tema():
    def __init__(self, titulo, genero, idioma):
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma

def write(musica):
    print("Titulo: ", musica.titulo, "-", end=" ")

    if musica.genero == "0":
        print("Genero: ", "Balada", "-", end=" ")
    elif musica.genero == "1":
        print("Genero: ", "Pop", "-", end=" ")
    elif musica.genero == "2":
        print("Genero: ", "Rock", "-", end=" ")
    elif musica.genero == "3":
        print("Genero: ", "Folclore", "-", end=" ")
    elif musica.genero == "4":
        print("Genero: ", "Electrónica", "-", end=" ")
    elif musica.genero == "5":
        print("Genero: ", "Otros", "-", end=" ")

    if musica.idioma == "0":
        print("Idioma: ", "Español", "-")
    elif musica.idioma == "1":
        print("Idioma: ", "Inglés", "-")
    elif musica.idioma == "2":
        print("Idioma: ", "Francés", "-")
    elif musica.idioma == "3":
        print("Idioma: ", "Portugués", "-")
    elif musica.idioma == "4":
        print("Idioma: ", "Otros", "-")
