import time

tiempo_en_segundos = time.time()
tiempo_entrada = time.ctime(tiempo_en_segundos)
print("El programa inicio en: ", tiempo_entrada)

tiempo_en_segundos +=5
tiempo_salida = time.ctime(tiempo_en_segundos)
print("El programa se cortara en: ", tiempo_salida)

tiempo_actual = time.process_time()
print("El tiempo actual es de: ", tiempo_actual)




print (time.localtime( time.time() ))
print (time.asctime( time.localtime(time.time()) ))
print ("time.time(): %f " %  time.clock())