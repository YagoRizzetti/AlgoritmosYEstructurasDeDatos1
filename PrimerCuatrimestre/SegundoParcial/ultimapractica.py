def esDigito(x):
    digitos = "1234567890"
    esd = False
    if x in digitos:
        esd = True
    return esd
    
def controld(x):
    countd = 0
    countpcdp = 0
    for i in x:
        if i == " " or i == ".":
            if countd > 0: 
                if countd % 2 == 0 :
                    countpcdp += 1
                countd = 0
        else:
            esd = esDigito(i)
            if esd:
                countd += 1 

    return countpcdp

def main():
    texto = input("Ingrese un texto que termine con un punto: ")
    tex = texto.lower()

    cpcdp = controld(tex)

    print("Hay una cantidad de: " + str(cpcdp) + " palabras que contienen una cantidad de digitos par")

main()