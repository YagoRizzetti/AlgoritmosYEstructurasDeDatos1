#1 Cantidad de palabras que tienen 'x' o 'X' en la primera mitad de la palabra
#2 Cantidad de palabras que comienzan con la ultima letra de la palabra anterior.
#3 Indicar con un mensaje si en el texto hay mas vocales que digitos (esVocal(car), esDigito(car), porcentaje(x,total))
#4 Porcentaje de palabras que comienzan y terminan con el mismo caracter.
from funcionesPracticaParcial import * 

def main():
    text = input("Ingrese un texto que termine con un punto: ")

    palx = palabrasx(text)
    ultl = ultimaL(text)
    vocales = controlar(text) 
    porplpu = porcentajepl(text)

    print("Cantidad de palabras que tienen x/X en su primera mitad: " + str(palx))
    print("Cantidad de palabras que comienzan con la ultima letra de la palabra anteriror: " + str(ultl))
    print(vocales)
    print("El porcentaje de palabras que comienzan y terminan con el mismo caracter es: " + str(porplpu))

main()