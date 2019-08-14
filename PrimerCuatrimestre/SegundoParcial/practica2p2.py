#1- Determinar la cantidad de palabras que incluían al menos una "e" y tenían menos de 4 letras. Por
#ejemplo, en el texto: “Este es el segundo parcial a evaluar.”, tiene 2 palabras que cumplen la
#condición ("es" y "el"). La palabra "a" no cumple porque no tiene una "e" (aunque sí tiene menos
#de 4 letras).

#2- Determinar la longitud de la palabra más larga entre las que contenían al menos una "s". Por
#ejemplo, en el texto: “La universidad es una etapa más de la vida.” hay tres palabras que
#contienen al menos una "s" ("universidad", "es" y "más"), y la más larga ("universidad") tiene 11
#letras.

#3- Determinar cuántas palabras comenzaron con una vocal y tenían una consonante en la segunda
#letra. Por ejemplo, en el texto: “Estamos en el horno.” hay tres palabras que cumplen la condición
#("Estamos", "en", "el").

#4- Determinar cuántas palabras contienen la expresión "ta" más de una vez. Por ejemplo, en el
#texto: “El resultado del partido nos dejó tartamudos.”, encontramos una palabra que cumple la
#condición (“tartamudos”). La palabra "resultado" contiene la expresión "ta" pero sólo una vez, por
#lo que no debe ser contada.

def controlta(x):
    ul = ""
    countptta = 0
    ta = 0
    for i in x:
        if i == " " or i == ".":
            if ta >= 2:
                countptta += 1
            ta = 0
            ul = ""
        else:
            if ul == "t" and i == "a":
                ta += 1
            ul = i
    return countptta

def esConsonante(x):
    consonante = "qwrtypsdfghjklñxcvbnm"
    tienec = False
    if x in consonante:
        tienec = True
    return tienec

def esVocal(x):
    vocal = "aeiou"
    tienev = False
    if x in vocal:
        tienev = True
    return tienev

def controlpvyc(x):
    tienev = False
    tienec = False
    countl = 0
    countpcvyc = 0
    for i in x:
        if i == " " or i ==".":
            if tienev and tienec:
                countpcvyc += 1
            countl = 0
            tienev = False 
            tienec = False
        else:
            countl += 1
            if countl == 1:
                tienev = esVocal(i)
            if countl == 2:
                tienec = esConsonante(i)
    return countpcvyc

def controlpls(x):
    lpmlcs = 0
    countl = 0
    tienes = False
    for i in x:
        if i == " " or i == ".":
            if tienes:
                if countl > lpmlcs:
                    lpmlcs = countl
                tienes = False 
            countl = 0       
        else:
            countl += 1
            if i == "s":
                tienes = True

    return lpmlcs

def controle(x):
    tienee = False
    countl = 0
    countpce = 0
    for i in x:
        if i == " " or i == ".":
            if countl < 4 and tienee:
                countpce += 1
            tienee = False
            countl = 0
        else:
            countl += 1
            if i == "e":
                tienee = True
    return countpce

def main():
    texto = input("Ingrese un texto que termine con un punto: ")
    tex = texto.lower()
    ce = controle(tex)
    cpmls = controlpls(tex)
    cpvyc = controlpvyc(tex)
    cta = controlta(tex)

    print("La cantidad de palabras que tienen e y tienen menos de 4 letras son: " + str(ce))
    print("La palabra con la mayor cantidad de letras y que contiene s tiene una cantidad de: " + str(cpmls) + " letras.")
    print("La cantidad de palabras que empiezan con vocal y su segunda letra es una consonante es de: " + str(cpvyc))
    print("La cantidad de palabras que tienen 'ta' dos veces o mas es de: " + str(cta))

main()
