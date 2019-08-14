#1- Determinar cuántas palabras del texto tienen más de cuatro letras, y contienen la letra 't'. Por
#ejemplo, el texto: "Estamos listos para adelantar la fase tres." tiene 3 palabras que cumplen la
#condición: "Estamos", "listos" y "adelantar".
#2- El promedio de letras por palabra entre las palabras que tienen hasta dos vocales. Por ejemplo, en
#el texto: "El mundo se volvió loco." hay 4 palabras que tienen hasta dos vocales ("El", "mundo",
#"se", "loco") y entre ellas suman 13 letras, por lo que el promedio pedido es pr = 13 / 4 = 3.25
#letras.
#3- Determinar la cantidad de palabras que contenían una "n" y comenzaban con vocal. Por ejemplo,
#el texto: “Algunos alumnos no saben que eso es correcto.” contiene 2 palabras que cumplen la
#condición: "Algunos" y "alumnos".
#4- Determinar cuántas palabras contuvieron la expresión "ro" pero de forma que comience después
#de la segunda letra de la palabra. Por ejemplo, en el texto: “Espero que el rotor funcione pero
#podemos seguir.”, contiene 2 palabras que cumplen la condición: "Espero" y "pero".

from funciones import *

def main():
    texto = input("Ingrese un texto que termine con un punto: ")
    tex = texto.lower()
    cpt = controlt(tex)
    plphdv = controltex(tex)
    pcnyv = controln(tex)
    ptro = controlro(tex)

    print("La cantidad de palabras que tienen 't' y su cantidad de letras es mayor a 4 son: " + str(cpt))
    print("El promedio de letras de las palabras que tiene una o 2 vocales es de: " + str(plphdv))
    print("La cantidad de palabras que comienzan con vocal y contienen 'n' es de: " + str(pcnyv))
    print("La cantidad de palabras que contienen 'ro' despues de la segunda letra es de: " + str(ptro))
main()
