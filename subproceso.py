
import subprocess, sys

comando = "ping -c 10 google.com"
proceso = subprocess.Popen(comando, shell = True, stderr = subprocess.PIPE)

while True:
    out = proceso.stderr.read(1)
    if not out and proceso.poll() != None:
        break 
    else:
        sys.stdout.write(out)
        sys.stdout.flush()
