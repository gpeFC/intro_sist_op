import threading, os, sys, subprocess


class MiHilo(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
    
    def run(self):
            os.system("date")
            subprocess.call(["ls", "-l", "/home/emanuel"])

hilo1 = MiHilo(1)
hilo2 = MiHilo(2)

hilo1.start()
hilo2.start()

print "Programa principal completado"
