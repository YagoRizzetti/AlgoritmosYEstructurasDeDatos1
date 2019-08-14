#-1 Determinar la cantidad de palabras que no tenían ninguna vocal. Por ejemplo, en el texto: “Si no
#le ganamos a Nigeria, entonces stms fr.”, tiene 2 palabras sin vocales ("stms" y "fr").

#2- El promedio de consonantes por palabra en todo el texto (tener en cuenta que puede haber otros
#caracteres). Por ejemplo, en el texto: “La universidad es una etapa más de la vida entre los 18 y
#los 25 años.” contiene 27 consonantes en 16 palabras, por lo que el promedio pedido es 27 / 16 =
#1.687 consonantes por palabra.

#3- Determinar cuántas palabras tenían una "p" o una "r", y al mismo tiempo comenzaban con la letra
#"a". Por ejemplo, en el texto: “Sabemos Python y apenas aparece Java.”, hay dos palabras que
#cumplen la condición pedida ("apenas" y "aparece").

#4- Determinar la cantidad de palabras que incluyeron la expresión “ar” pero de forma que comience
#después de la segunda letra de esas palabras. Por ejemplo, en el texto: “Los argentinos estaremos
#mirando el partido con ansiedad.”, hay una palabra que cumple la condición (“estaremos”). La
#palabra "argentino" no cumple (ya que "ar" se forma comenzando en la primera letra) y "partido"
#tampoco (ya que "ar" se forma comenzando en la segunda letra).

def controlAr(x):
    ar = False
    countl = 0
    ul = ""
    countpAr = 0
    for i in x:
        if i == " " or i == ".":
            if ar:
                countpAr += 1
                ar = False
            countl = 0
        else:
            countl += 1
            if countl > 2:
                if ul == "a" and i == "r":
                    ar = True
                ul = i
    return countpAr


def controltpra(x):
    pl = ""
    tienepor = False
    countl = 0
    countpcc = 0
    for i in x:
        if i == " " or i == ".":
            if pl == "a" and tienepor:
                countpcc += 1
            tienepor = False 
            countl = 0
        else:
            countl += 1
            if countl == 1:
                pl = i
            if i == "p" or i == "r":
                tienepor = True
    return countpcc


def esConsonante(x):
    consonantes = "qwrtypsdfghjklñzxcvbnm"
    ec = False
    if x in consonantes:
        ec = True
    return ec

def controlcpp(x):
    countc = 0
    countp = 0
    for i in x:
        if i == " " or i == ".":
            countp += 1            
        else:
            esC = esConsonante(i)
            if esC:
                countc +=1
    if countc != 0:
        promcpp = countp / countc
    else:
        promcpp = 0
    return promcpp

def esVocal(x):
    v = "aeiou"
    esvocal = False
    if x in v:
        esvocal = True
    return esvocal


def controlpsv(x):
    countpsv = 0
    tienev = False
    for i in x:
        if i == " " or i == ".":
            if tienev == False:
                countpsv += 1
            tienev = False
        else:
            ev = esVocal(i)
            if ev:
                tienev = True
    return countpsv            

def main():
    texto = input("Ingrese un texto que termine con un punto: ")
    tex = texto.lower()
    cpsv = controlpsv(tex)
    pcpp = controlcpp(tex)
    tporycca = controltpra(tex)
    par = controlAr(tex)

    print("El texto tiene una cantidad de " + str(cpsv) + " palabras sin vocales.")
    print("El promedio de conconantes por palabras es de: " + str(pcpp))
    print("La cantidad de palabras que comienzan con a y contienen p o r es de: " +str(tporycca))
    print("La cantidad de palabras que tienen 'ar' despues de la segunda letra es de: " + str(par))
    
main()