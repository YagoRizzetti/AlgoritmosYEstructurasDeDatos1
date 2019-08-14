def esVocal(v):
    vocales = 'aeiou'
    tienevocal = False
    if v in vocales:
        tienevocal = True
    return tienevocal

def esDigito(d):
    digito = '1234567890'
    esdigito = False
    if d in digito:
        esdigito = True
    return esdigito

def porcentaje(x,total):
    porcen = (x*100)/total
    return porcen

def porcentajepl(t):
    prim = ""
    ult = ""
    countppyu = 0
    countlpal = 0
    countpal = 0
    for i in t:
        if i == " " or i == ".":
            countpal += 1 
            if prim == ult:
                countppyu += 1
            countlpal = 0
        else:
            countlpal += 1 
            if countlpal == 1:
                prim = i
            ult = i
    
    porc = porcentaje(countppyu, countpal)

    return porc

def controlar(b):
    countV = 0
    countD = 0
    countL = 0
    for i in b:
        if i != " " and i != ".":
            countL += 1
            v = esVocal(i)
            d = esDigito(i)
            if v:
                countV += 1
            elif d:
                countD += 1
    porcV = porcentaje(countV,countL)
    porcD = porcentaje(countD,countL)
    if porcV > porcD:
        haymasV = "Hay mas vocales que digitos"
    else:
        haymasV = "Hay mas digitos que vocales"

    return haymasV

def ultimaL(a):
    newp = False
    ultima = ""
    countpla = 0

    for i in a:
        if i == " " or i == ".":
            newp = True
        else:
            if newp and ultima == i:
                countpla += 1
            ultima = i
            newp = False
    return countpla

def palabrasx(x):
    cp = 0
    cl = 0
    countpalx = 0
    tienex = False
    for i in x:
        if i == " " or i == ".":
            cp +=1
            if tienex:
                mit = cl / 2
                if x <= mit:
                    countpalx += 1
                    tienex = False
            cl = 0
        else:
            cl +=1
            if tienex == False and (i == "x" or i == "X"):
                x = cl
                tienex = True

    return countpalx
