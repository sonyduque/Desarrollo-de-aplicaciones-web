# Nombre: Julio Cesar Gonzalez Duque
# Carrera: Informatica
# Materia: Desarrollo de aplicaciones web con Python
# Practica 2.1 Votos

print("Elige un candidato entre A, B, C")
Candidato=input("Candidato elegido: ")
if Candidato.upper()=="A":
    print("Voto por el candidato amarillo")
elif Candidato.upper()=="B":
    print("Voto por el candidato morado")
elif Candidato.upper()=="C":
    print("Voto por el candidato rojo")
else:
    print("Dato erroneo")
print("De 2,000,000 votos")

import random
candidatos=[1,2,3]
cand1=0
cand2=0
cand3=0
for i in range(2000000):
    voto=random.choice(candidatos)
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    else:
        cand3 += 1
if cand1 > cand2 and cand1 > cand3:
    print("El ganador es el candidato Amarillo con:",cand1, "votos")
elif cand2 > cand1 and cand2 > cand3:
    print("El ganador es el candidato Morado con:",cand2, "votos")
else:
    print("El ganador es el candidato Rojo con:",cand3, "votos")

