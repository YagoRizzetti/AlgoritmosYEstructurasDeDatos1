hora=3600
cantidadDeSegundos=int(input("ingrese la cantidad de segundos:"))
tiempoTranscurridoEnHoras=cantidadDeSegundos/hora
print("el tiempo transcurrido en horas fue de:", tiempoTranscurridoEnHoras)
minuto=60
tiempoTranscurridoMinutos=cantidadDeSegundos%hora/minuto
print("el tiempo transcurrido en minutos fue de:", tiempoTranscurridoMinutos)
tiempoTranscurridoEnSegundos=((cantidadDeSegundos)-((tiempoTranscurridoEnHoras*hora)+(tiempoTranscurridoMinutos*minuto)))
print("El tiempo transcurrido en segundos fue de:",tiempoTranscurridoEnSegundos)