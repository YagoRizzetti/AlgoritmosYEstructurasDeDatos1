def esVocal(x):
    vocales = "aeiou"
    ev = False
    if x in vocales:
        ev = True
    return ev

def controlro(x):
    ul = ""
    countl = 0
    tienero = False
    countpcro = 0
    for i in x:
        if i == " " or i == ".":
            if tienero:
                countpcro += 1
            tienero = False
            countl = 0
            ul = ""
        else:
            countl += 1
            if countl > 2:
                if ul == "r" and i == "o":
                    tienero = True
                ul = i
    return countpcro

def controln(x):
    countpvyn = 0
    plv = False
    tienen = False
    countl = 0
    for i in x:
        if i == " " or i == ".":
            if plv and tienen:
                countpvyn += 1
            tienen = False
            plv = False
            countl = 0
        else:
            countl += 1
            if countl == 1:
                ev = esVocal(i)
                if ev:
                    plv = True
            else:
                if i == "n":
                    tienen = True
    return countpvyn

def controltex(x):
    countv = 0
    countl = 0
    suml = 0
    countpcv = 0
    for i in x:
        if i == " " or i == ".":
            if countv <= 2:
                countpcv += 1
                suml += countl
            countv = 0
            countl = 0
        else:
            countl += 1
            ev = esVocal(i)
            if ev:
                countv += 1
    prom = suml / countpcv
    return prom

def controlt(x):
    tienet = False
    countl = 0
    countptt = 0
    for i in x:
        if i == " " or i == ".":
            if countl > 4 and tienet:
                countptt += 1
            countl = 0
            tienet = False
        else:
            countl +=1
            if i == "t":
                tienet = True
    return countptt
