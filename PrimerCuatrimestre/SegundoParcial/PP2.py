#1 Cantidad de palabras que tienen 'x' o 'X' en la primera mitad de la palabra
#2 Cantidad de palabras que comienzan con la ultima letra de la palabra anterior.
#3 Indicar con un mensaje si en el texto hay mas vocales que digitos (esVocal(car), esDigito(car), porcentaje(x,total))
#4 Porcentaje de palabras que comienzan y terminan con el mismo caracter.

def porcentaje(x,t):
    porc = t/100*x
    return porc

def comyterm(x):
    ul = ""
    pl = ""
    countlp = 0 
    countpyu = 0
    totalp = 0
    a = x.lower()
    for i in a:
        if i == " " or i == ".":
            totalp += 1
            if ul == pl:
                countpyu += 1
            countlp = 0
        else:
            countlp +=1
            if countlp == 1:
                pl = i       
            ul = i

    porc = porcentaje(countpyu,totalp)

    return porc

def esDigito(x):
    digitos = "1234567890"
    d = False
    if x in digitos:
        d = True
    return d

def esVocal(x):
    vocales = "aeiou"
    v = False
    if x in vocales:
        v = True
    return v

def controlv(x):
    countv = 0
    countd = 0
    totalc = 0 
    for i in x:
        if i != " " or i != ".":
            totalc += 1
            v = esVocal(i)
            d = esDigito(i)
            if v:
                countv +=1
            else:
                if d:
                    countd +=1
    porcv = porcentaje(countv,totalc)
    porcd = porcentaje(countd,totalc)
    if porcv > porcd:
        res = "Hay mas vocales que digitos"
    else:
        if porcd >= porcv:
            res = "No hay mas vocales que digitos"

    return res

def controlul(x):
    ul = ""
    countpul = 0
    countp = 0
    for i in x:
        if i == " " or i == ".":
            countp += 1
        else:
            if countp != 0:
                if i == ul:
                    countpul += 1 
            ul = i

    return countpul

def controlx(x):
    countlp = 0
    countpx = 0
    lugx = 0
    tienex = False
    a = x.lower()
    for i in a:
        if i == " " or i == ".":
            if tienex:
                mitp = countlp / 2
                if lugx <= mitp:
                    countpx += 1
                tienex = False
            countlp = 0
        else:
            countlp += 1
            if i == "x" and tienex == False:
                lugx = countlp
                tienex = True

    return countpx

def main():
    texto = input("Ingrese un texto que termine con un punto: ")
    palx = controlx(texto)
    palulap = controlul(texto)
    vod = controlv(texto)
    cyt = comyterm(texto)

    print(palx)
    print(palulap)
    print(vod)
    print(cyt)

main()