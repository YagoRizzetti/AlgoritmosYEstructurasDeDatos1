print("-"+100)
print("Censo")
print("-"+100)

sexo=()
edad=()
cantidadMayor=0
cantidadDeMujeresEscolar=0
hombreMayor80=False

np=raw_input("desea ingresar una nueva persona al la lista del censo? s/n :")

while(np=="s"):
    e=input("Ingrese la edad de la persona: ")
    edad.append(e)
    s=raw_input("ingrese el sexo de la persona m/f: ")
    sexo.append(s)
    np=raw_input("desea ingresar una nueva persona? s/n: ")

if(np=="n"):
    cm=sexo.count("m")    
    cf=sexo.count("f")
    if(cm==cf):
        cantidadMayor="Hay la misma cantidad de hombre que de mujeres."
    if(cm>cf):
        cantidadMayor="Hay mayor cantidad de Hombres."
    else:
        cantidadMayor="Hay mayor cantidad de Mujeres." 

for a in range(len(sexo)):
    for b in range(len(edad)):
        if(a=="f" and b >= 4 and b <= 18):
             cantidadDeMujeresEscolar += 1

for a in range(len(sexo)):
    for b in range(len(edad)):
        if(a=="m" and b >80):
            hombreMayor80=True
            if(hombreMayor80 == True):
                hombreMayor80="Existe al menos un hombre mayor a 80 años."

print(cantidadMayor)
print(cantidadDeMujeresEscolar)
print(hombreMayor80)        