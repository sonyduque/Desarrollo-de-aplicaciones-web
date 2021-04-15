#Nombre: Julio Cesar Gonzalez Duque
#Carrera: Informatica
#Materia: Desarrollo de aplicaciones web
#Practica 2.3

from random import randint
#se toma otro codigo de un archivo aparte
from funcionesteatro import *

#se definen algunas variables 
precio=100
capacidad=10000
monto= capacidad*precio
suma_des=0
suma_percibida=0

categoria={"primera":0, "segunda":0, "tercera":0, "cuarta":0, "quinta":0,}
descuentos={
    "1":(precio*.30),
    "2":(precio*.10),
    "3":(precio*.15),
    "4":(precio*.25),
    "5":(precio*.35)
    }
#se agregan listas
suma_descuentos=[0, 0, 0, 0, 0]
suma_entradas={"1":0, "2":0, "3":0, "4":0, "5":0}

#se le da un rango de personas admitidas
for i in range(10000):
    #se toma la edad de forma aleratoria de 5 a 120
    edad=randint(5, 120)
    if edad >5 and edad <14:
        categoria["primera"]+=1
        suma_descuentos[0]+= descuentos["1"]
        suma_entradas["1"]+= precio - descuentos["1"]
    elif edad >15 and edad <19:
        categoria["segunda"]+=1
        suma_descuentos[1]+= descuentos["2"]
        suma_entradas["2"]+= precio - descuentos["2"]
    elif edad >20 and edad <45:
        categoria["tercera"]+=1
        suma_descuentos[2]+= descuentos["3"]
        suma_entradas["3"]+= precio - descuentos["3"]
    elif edad >46 and edad <65:
        categoria["cuarta"]+=1
        suma_descuentos[3]+= descuentos["4"]
        suma_entradas["4"]+= precio - descuentos["4"]
    else:
        categoria["quinta"]+=1
        suma_descuentos[4]+= descuentos["5"]
        suma_entradas["5"]+= precio - descuentos["5"]
        
#funcion que saca el total que obtuvo por el evento
suma_percibida=obtenersumasentradas(suma_entradas)
print(f"la suma total percibida es $ {suma_percibida:0.2f}")

#lo que no cobro el evento
suma_des=obtenersumasdescuentos(suma_descuentos)
print(f"el descuento es $ {suma_des:0.2f}")

#monto anterior en forma de porcentaje
porcentaje=(suma_des/monto)*100
print(f"equivale a {porcentaje:0.2f}%")

#lo que recibiria si no aplicara los descuentos
print(f"se pudo haber obtenido {monto:0.2f}")

#cuantas personas de cierta edad entraron 
por1=(categoria['primera']/ capacidad)*100
por2=(categoria['segunda']/ capacidad)*100
por3=(categoria['tercera']/ capacidad)*100
por4=(categoria['cuarta']/ capacidad)*100
por5=(categoria['quinta']/ capacidad)*100

bar1=int(por1)
bar2=int(por2)
bar3=int(por3)
bar4=int(por4)
bar5=int(por5)

#grafica de el porcentaje de personas que asistieron segun la edad
print("entraron por rango de edad")
print(f"5-14: {categoria['primera']:7.2f}: {por1:5.2f}%: {('>' * bar1)}")
print(f"15-19: {categoria['segunda']:7.2f}: {por2:5.2f}%: {('>' * bar2)}")
print(f"20-45: {categoria['tercera']:7.2f}: {por3:5.2f}%: {('>' * bar3)}")
print(f"46-65: {categoria['cuarta']:7.2f}: {por4:5.2f}%: {('>' * bar4)}")
print(f"65->: {categoria['quinta']:7.2f}: {por5:5.2f}%: {('>' * bar5)}")