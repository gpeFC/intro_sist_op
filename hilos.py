
import thread, time 

#Para utilizar hilos necesitamos una funcion que es la que se va a
#llamar para ser ejecutada por el hilo.


#Funcion para el hilo.
def imprime_tiempo(nombre_thread, retraso):
    for i in range(5):
        time.sleep(retraso)
        print "%s: %s" % (nombre_thread, time.ctime(time.time()))

#Ahora vamos a crear los hilos.
try:
    thread.start_new_thread(imprime_tiempo, ("Hilo Alfa", 2))
    thread.start_new_thread(imprime_tiempo, ("Hilo Beta", 3))
except:
    print "No se pudieron crear los hilos"

while 1:
    pass


