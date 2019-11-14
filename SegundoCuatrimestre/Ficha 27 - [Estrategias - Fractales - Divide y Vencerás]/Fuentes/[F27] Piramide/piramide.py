from tkinter import *

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def pyramid(canvas, x, y, r):
    if r > 0:
        # dibujar recursivamente el soporte inferior izquierdo...
        pyramid(canvas, x-r, y+r, r//2)

        # dibujar recursivamente el soporte inferior derecho...
        pyramid(canvas, x+r, y+r, r//2)

        # dibujar recursivamente el soporte superior izquierdo...
        pyramid(canvas, x-r, y-r, r//2)

        # dibujar recursivamente el soporte superior derecho...
        pyramid(canvas, x+r, y-r, r//2)

        # dibujar en (post-orden) la tapa o cima de la pirámide...
        square(canvas, x, y, r)


def square(canvas, x, y, r):
    left = x - r
    top = y - r

    right = x + r
    down = y + r

    canvas.create_rectangle((left, top, right, down), outline='black', fill='', width=1)


def render():
    # configuracion inicial de la ventana principal...
    root = Tk()
    root.title('Pirámide Fractal')

    # calculo de resolucion en pixels de la pantalla...
    maxw = root.winfo_screenwidth()
    maxh = root.winfo_screenheight()

    # ajuste de las dimensiones y coordenadas de arranque de la ventana...
    root.geometry("%dx%d+%d+%d" % (maxw, maxh, 0, 0))

    # un lienzo de dibujo dentro de la ventana...
    canvas = Canvas(root, width=maxw, height=maxh)
    canvas.grid(column=0, row=0)

    # sea un lado inicial r igual a un duodécimo del ancho del area de dibujo...
    r = maxw // 12

    # coordenadas del centro de la pantalla...
    cx = maxw // 2
    cy = maxh // 2

    # dibujar piramide fractal centrada en (cx, cy) y con el cuadrado mayor con lado = r.
    pyramid(canvas, cx, cy, r)

    # lanzar el ciclo principal de control de eventos de la ventana...
    root.mainloop()


if __name__ == '__main__':
    render()