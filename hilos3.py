import threading, time 

def imprime_tiempo(nombre_thread, retraso, contador):
    for i in range(contador):
        time.sleep(retraso)
        print "%s: %s" % (nombre_thread, time.ctime(time.time()))

class MiHilo(threading.Thread):
    def __init__(self, threadID, nombre, contador, retraso):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.contador = contador
        self.retraso = retraso
    
    def run(self):
        print "Iniciando hilo - > ", self.nombre
        threadLock.acquire()
        imprime_tiempo(self.nombre, self.retraso, self.contador)
        print "Terminando hilo -> ", self.nombre
        threadLock.release()

hilo1 = MiHilo(1, "Alfa", 5, 4)
hilo2 = MiHilo(2, "Beta", 10, 2)

hilo1.start()
hilo2.start()

#En este caso quiero esperar a los hilos.

threadLock = threading.Lock()
threads = []

threads.append(hilo1)
threads.append(hilo2)

for t in threads:
    t.join()

print "Programa principal completado"
