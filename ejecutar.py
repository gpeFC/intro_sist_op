

import os


#Abre una 'shell' del sistema y ejecuta el comando.
os.system("date")

#dpipe = os.popen("algun comando")
#Ejecuta el comando y nos regresa un pipe para leer su salida.
p = os.popen("date")

#Para leer la salida.
tiempo = p.read()
print "Hoy es: ", tiempo


#Una mejor forma de ejecutar comandos de Unix.
import subprocess

#Llamada basica.
subprocess.call("date")


#Si queremos algo mas complejos como ls -l /home/<file>
subprocess.call(["ls", "-l", "/home/emanuel"])



#Llamamos al mis comando pero con un Pipe.
pip = subprocess.Popen(["ls", "-l", "/home/emanuel"], stdout = subprocess.PIPE, shell = True)

#Otro ejemplo.
ping = subprocess.Popen(["ping", "-c", "10", "google.com"], stdout = subprocess.PIPE)
s, e = ping.communicate()
print "Salida: ", s
print "Errores: ", e



