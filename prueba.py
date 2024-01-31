import requests
import random
lista_passwords=["admin","password","manager","letmein","cisco","default","root","apc","pass","security","user","system","sys"]
url=None
password_encontrada=False

inicio=0
final=len(lista_passwords)
while password_encontrada==False:
    login_aleatorio=random.randint(inicio,final)
    contraseña_aleatoria=random.randint(inicio,final)

    payload={lista_passwords[login_aleatorio]:lista_passwords[contraseña_aleatoria]}

    peticion=requests.post(url,data=payload)
    if peticion.status_code==200:
        print("contraseña encontrada",payload)
        password_encontrada==True
    else:
        print("/+/-/*//dame1seg//+/-/*/")
        pass
