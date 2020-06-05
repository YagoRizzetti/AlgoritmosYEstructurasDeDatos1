import random

#--------------------------------------------------------------------------------------------------------------------------------------

def porcentaje(x,n):

    p=(x*100)/n

    return(p)

#--------------------------------------------------------------------------------------------------------------------------------------

def casoAutoctono(e,res,reg,c,p,s):
    esAutoctono = False
    if res == "Positivo" and c == "No" and p == "No" and s == "No":
        esAutoctono = True
    return(esAutoctono)

#--------------------------------------------------------------------------------------------------------------------------------------

def validarUser(u, v):
    tA = False
    tP = False
    for i in range(len(u)):
        if u[i] == "@" or u[i] == ".":
            if i == 0 or i == len(u)-1:
                v = False
                tA = False
                tP = False
                break
            if u[i] == "@":
                if tA:
                    v = False
                    tA = False
                    tP = False
                    break
                tA = True
            else:
                if u[i] == u[i - 1]:
                    v = False
                    tA = False
                    tP = False
                    break
            v = True
                     
    return(u, v)            

#--------------------------------------------------------------------------------------------------------------------------------------

def regSinCasos(a,b):
    for i in range(len(a)):
        if a[i] == 0:
            for l in range(len(b)):
                if i == l:
                    print("En la region: ", b[l], " hay una cantidad de: " + str(a[i]) + " casos")
                    break
            

#--------------------------------------------------------------------------------------------------------------------------------------

def cargarDatos(x):
    estados = ("Positivo", "Negativo")
    sn = ("Si", "No")
    reg = ["Capital", "Cordoba", "Norte", "Sur"]
    cantCP = 0
    cantPS = 0
    countPGR = 0
    cantCPExterior = 0
    cantCS = 0
    cantCAP = 0
    acumEPGR = 0
    acumE = 0
    mE = 100
    mECA = 100
    casosPR = [0,0,0,0]
    for i in range(x):
        edad = random.randint(1,100)
        resultado = random.choice(estados)
        region = random.choice(reg)
        contacto = random.choice(sn)
        personal = random.choice(sn)
        salio = random.choice(sn)

        cA = casoAutoctono(edad,resultado,region,contacto,personal,salio)

        if resultado == "Positivo":
            cantCP += 1
            acumE += edad
            if region == "Capital":
                casosPR[0] += 1
            elif region == "Cordoba":
                casosPR[1] += 1
            elif region == "Norte":
                casosPR[2] += 1
            else:
                casosPR[3] += 1
            if salio == "Si":
                cantCPExterior += 1
        else:
            if contacto == "Si":
                cantCS += 1

        if edad >= 60:
            countPGR += 1
            acumEPGR += edad

        if personal == "Si":
            cantPS += 1

        if edad < mE:
            mE = edad

        if cA:
            if edad < mECA:
                mECA = edad
            if resultado == "Positivo":
                cantCAP += 1

        print("edad: " + str(edad) + "\n"
              "Resultado: " + resultado + "\n"
              "Región: " + region + "\n"
              "estuvo en contacto con casos confirmados: " + contacto + "\n"
              "Es personal de salud: " + personal + "\n"
              "Salio al exterior: " , salio , "\n")

    porcCP = porcentaje(cantCP,x)

    eppgr = acumEPGR/countPGR

    porcPS = porcentaje(cantPS,x)

    epcc = acumE/cantCP

    pccap = porcentaje(casosPR[0],cantCP)

    pccor = porcentaje(casosPR[1],cantCP)
    
    pcnort = porcentaje(casosPR[2],cantCP)

    pcsur = porcentaje(casosPR[3],cantCP)

    pcap = porcentaje(cantCAP,cantCP)
    
    return (cantCP, porcCP, eppgr, cantPS, porcPS, epcc, mECA, casosPR[0], casosPR[1], casosPR[2], casosPR[3], pccap, pccor, pcnort, pcsur, cantCPExterior, cantCS, casosPR, reg, pcap)

#--------------------------------------------------------------------------------------------------------------------------------------

