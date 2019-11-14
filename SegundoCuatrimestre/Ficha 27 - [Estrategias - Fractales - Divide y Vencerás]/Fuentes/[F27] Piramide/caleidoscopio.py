from tkinter import *
from random import *

__author__ = 'Cátedra de Algoritmos y Estructuras de Datos'


def kaleidoscope(canvas, x, y, r):
    if r > 0:
        # seleccionar dos colores en forma aleatoria...
        colors = ('blue', 'red', 'yellow', 'green', 'orange', 'purple', 'magenta', 'black', 'salmon')
        c1 = choice(colors)
        c2 = choice(colors)

        # dibujar en pre-orden el cuadrado y el rombo de ese nivel...
        square(canvas, c1, x, y, r)
        diamond(canvas, c2, x, y, r)

        # dibujar recursivamente el resto del caleidoscopio...
        kaleidoscope(canvas, x, y, r//2)


def square(canvas, c, x, y, r):
    left = x - r
    top = y - r

    right = x + r
    down = y + r

    canvas.create_polygon((left, top, right, top, right, down, left, down), width=2, outline=c, fill='')


def diamond(canvas, c, x, y, r):
    left = x - r
    top = y - r

    right = x + r
    down = y + r

    canvas.create_polygon((x, top, right, y, x, down, left, y), width=2, outline=c, fill='')


def render():
    # configuracion inicial de la ventana principal...
    root = Tk()
    root.title('Caleidoscopio Fractal Simple')

    # calculo de resolucion en pixels de la pantalla...
    maxw = root.winfo_screenwidth()
    maxh = root.winfo_screenheight()

    # ajuste de las dimensiones y coordenadas de arranque de la ventana...
    root.geometry("%dx%d+%d+%d" % (maxw, maxh, 0, 0))

    # un lienzo de dibujo dentro de la ventana...
    canvas = Canvas(root, bg='white', width=maxw, height=maxh)
    canvas.grid(column=0, row=0)

    # sea un lado inicial r igual a un octavo del ancho del area de dibujo...
    r = maxw // 8

    # coordenadas del centro del caleidoscopio a dibujar...
    cx = maxw // 2
    cy = maxh // 2 - maxh//12

    # dibujar piramide fractal centrada en (cx, cy) y con el cuadrado mayor con lado = r.
    kaleidoscope(canvas, cx, cy, r)

    # lanzar el ciclo principal de control de eventos de la ventana...
    root.mainloop()


if __name__ == '__main__':
    render()
