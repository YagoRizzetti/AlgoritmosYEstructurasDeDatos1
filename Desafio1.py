horas=0
minutos=0

print("ingrese la cantidad de segundos")
segundosTotal=input()
if(segundosTotal>=3600):
    horas=segundosTotal/3600
    segundosRestantes1=segundosTotal%3600
    if(segundosRestantes1<3600):
        minutos=segundosRestantes1/60
        segundosRestantes2=segundosRestantes1%60
        print(segundosTotal, "Es igual a: ", horas,"horas", minutos,"minutos", segundosRestantes2,"segundos")
if(60<segundosTotal<3600):
    minutos=segundosTotal/60
    segundosRestantes2=segundosTotal%60
    print(segundosTotal, "Es igual a: ", horas, "horas", minutos,"minutos", segundosRestantes2,"segundos")
if(segundosTotal<60):
    print(segundosTotal, "Es igual a: ", horas, "horas", minutos, "minutos", segundosTotal, "segundos")

print("ingrese una cantidad de horas:")
h=input()
print("ingrese una cantidad de minutos")
m=input()
print("ingrese una cantidad de segundos")
s=input()
print("La conversion de: ", h ,"horas", m ,"minutos", s ,"segundos", " es igual a: ", ((h*3600)+(m*60)+s))    
    