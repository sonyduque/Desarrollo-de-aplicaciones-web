#nombre: Juio Cesar Gonzalez Duque
#Carrera: Informatica
#Materia: Desarrollo de aplicaciones web
#Ejercicio: 2.2
fecha= input("fecha(formato 'dia, DD/MM');")
"""especifica el formato en como se pondran los datos"""
fecha= fecha.lower()
"""convierte la fecha en minusculas """
diasemana=fecha[0:fecha.find(',')]
"""define el fin hasta la coma del formato de fecha """
dianro=int(fecha[fecha.find(' ')+1:fecha.find('/')])
"""toma el espacio y le suma lo que sigue para acabar antes de la barra. y es entero """
mesnro=int(fecha[fecha.find('/')+1:])
"""sigue la continuacion despues de la barra del formato. es entero """
if dianro >31 or mesnro >12:
    print("Fecha incorrecta")
else:
    if diasemana in "lunes, martes, miercoles":
        respuesta=input("¿se tomaron examenes? S/N")
        if respuesta.lower()=="s":
            aprobados=int(input("Cantidad de aprobados: "))
            """toma la respuesta como entero """
            reprobados=int(input("Cantidad de reprobados: "))
            print("porcentaje de aprobados: ", (aprobados*100)/(aprobados+reprobados), "%")
            """imprime la respuesta y hace las operaciones en la misma linea """
    elif diasemana == "jueves":
        asistencia=int(input("porcentaje de asistencias: "))
        if asistencia >50:
            print("Asistio a la mayoria")
        else:
            print("NO asistio a la mayoria")
    elif diasemana == "viernes":
        if dianro ==1 and (mesnro==1 or mesnro==7):
            print("Comeinzo de nuevo ciclo")
            alumnos=int(input("Cantidad de alumnos: "))
            alcance1=float(input("alcance1:$"))
            print("ingreso total:$", alumnos*alcance1)
        else:
            print("Fecha incorrecta")

print("Fin del programa")