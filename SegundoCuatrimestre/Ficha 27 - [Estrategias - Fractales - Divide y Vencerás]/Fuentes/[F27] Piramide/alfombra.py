from tkinter import *

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def pyramid(canvas, x, y, r):
    if r > 3:
        square(canvas, x, y, r)
        small_r = r / 3
        small_d = 2 * small_r
        pyramid(canvas, x - small_d, y - small_d, small_r)
        pyramid(canvas, x, y - small_d, small_r)
        pyramid(canvas, x + small_d, y - small_d, small_r)
        pyramid(canvas, x - small_d, y, small_r)
        pyramid(canvas, x + small_d, y, small_r)
        pyramid(canvas, x - small_d, y + small_d, small_r)
        pyramid(canvas, x, y + small_d, small_r)
        pyramid(canvas, x + small_d, y + small_d, small_r)


def square(canvas, x, y, r):
    small_r = r / 3

    left = x - r
    top = y - r

    right = x + r
    down = y + r

    canvas.create_rectangle((left, top, right, down), outline='blue', fill='blue', width=1)
    canvas.create_rectangle((x - small_r, y - small_r, x + small_r, y + small_r), fill="black")


def render():
    # configuracion inicial de la ventana principal...
    root = Tk()
    root.title('Sierpinsky carpet')

    # calculo de resolucion en pixels de la pantalla...
    maxw = root.winfo_screenwidth()
    maxh = root.winfo_screenheight()

    # ajuste de las dimensiones y coordenadas de arranque de la ventana...
    root.geometry("%dx%d+%d+%d" % (maxw, maxh, 0, 0))

    # un lienzo de dibujo dentro de la ventana...
    canvas = Canvas(root, width=maxw, height=maxh)
    canvas.grid(column=0, row=0)

    # sea un lado inicial r
    r = maxh // 2 - 30

    # coordenadas del centro de la pantalla...
    cx = maxw // 2
    cy = maxh // 2

    # dibujar piramide fractal centrada en (cx, cy) y con el cuadrado mayor con lado = r.
    pyramid(canvas, cx, cy, r)

    # lanzar el ciclo principal de control de eventos de la ventana...
    root.mainloop()


if __name__ == '__main__':
    render()
