from tkinter import *

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


def pyramid(canvas, x, y, side):
    if side > 10:
        triangle(canvas, x, y, side)
        pyramid(canvas, x, y, side//2)
        half_height = side/2 * (pow(3, 0.5)/2)
        pyramid(canvas, x + side/4, y + half_height, side/2)
        pyramid(canvas, x - side/4, y + half_height, side/2)


def triangle(canvas, x, y, r):
    # Dibujo del triángulo exterior
    height = r * (pow(3, 0.5)/2)
    base = y + height
    left = x - r/2
    right = x + r/2
    canvas.create_polygon(x, y, left, base, right, base, outline='red', fill='red')

    # Dibujo del triángulo interno invertido
    left = x - r/4
    right = x + r/4
    half_height = y + height / 2
    canvas.create_polygon(x, base, left, half_height, right, half_height, outline='white', fill='white')


def render():
    # configuracion inicial de la ventana principal...
    root = Tk()
    root.title('Sierpinski triangle')

    # calculo de resolucion en pixels de la pantalla...
    maxw = root.winfo_screenwidth()
    maxh = root.winfo_screenheight()

    # ajuste de las dimensiones y coordenadas de arranque de la ventana...
    root.geometry("%dx%d+%d+%d" % (maxw, maxh, 0, 0))

    # un lienzo de dibujo dentro de la ventana...
    canvas = Canvas(root, width=maxw, height=maxh)
    canvas.grid(column=0, row=0)

    # sea un lado inicial side...
    side = maxh - 20

    # coordenadas del punto superior del triángulo...
    cx = maxw / 2
    cy = (maxh - side) / 2

    # dibujar piramide fractal
    pyramid(canvas, cx, cy, side)

    # lanzar el ciclo principal de control de eventos de la ventana...
    root.mainloop()

if __name__ == '__main__':
    render()
