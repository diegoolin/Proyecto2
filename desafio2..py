import random
n=int(input("ingrese la cantidad maxima de pilas que se pueden hacer: "))
m=int(input("ingrese la cantidad maxima de contenedores que se pueden apilar: "))
lista=[]
Palabra = ""
for i in range(n):
	lista.append([])
	for j in range(m):
		lista[i].append(0)

for i in range(n):
    for j in range (m):
        print("|",lista[i][j], "|", end=" ")
    print()

menu = int(input("1 para ubicar un contenedor \n2 para ingresar el contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada laboral \nIngrese opción:"))
while menu !=4:
    if menu == 1:
        numerocontenedor= input("ingrese el numero del contenedor para ubicarlo: ")    
        nombreempresa = input("ingrese el nombre de la empresa:")
        ubicacion=numerocontenedor+"/"+nombreempresa
        for i in range(n):
            for j in range(m):
                if lista[i][j]==ubicacion:
                    print("el contenedor",lista[i][j],"se encuentra en la pila",[i],"en la posición",[j])           

        seguir = input("¿desea continuar?:")
        while seguir== "si":
            numerocontenedor= int(input("ingrese el numero del contenedor: "))
            nombreempresa= input("ingrese el nombre de la empresa propietaria: ")
            seguir = input("¿desea continuar?:")
           
        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

    if menu == 2:
        
        numerocontenedor=input("Ingrese numero del contenedor a añadir:")
        nombreempresa = input("Ingrese nombre de la empresa:")
        ubicacionf= int(input("Ingrese a que fila desea ingresar el contenedor:"))
        ubicacionc= int(input("Ingrese a que columna desea ingresar el contenedor:"))

        lista[ubicacionf][ubicacionc]= numerocontenedor+"/"+nombreempresa

        for i in range(n):
            for j in range (m):
                print("|",lista[i][j],"|",end=" ")
            print()
        
        seguir= input("¿desea continuar?: ")
        while seguir== "si":
            numerocontenedor=input("Ingrese numero del contenedor a añadir:")
            nombreempresa = input("Ingrese nombre de la empresa:")
            ubicacionf= int(input("Ingrese a que fila desea ingresar el contenedor:"))
            ubicacionc= int(input("Ingrese a que columna desea ingresar el contenedor:"))

            lista[ubicacionf][ubicacionc]= numerocontenedor+"/"+nombreempresa

        
            for i in range(n):
                for j in range (m):
                    print("|",lista[i][j],"|",end=" ")
                print()
            seguir = input("¿desea continuar?:")

        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada laboral \nIngrese opción:"))

    if menu == 3:
        numerocontenedor=int(input("Ingrese numero del contenedor a retirar:"))
        nombreempresa = input("Ingrese nombre de empresa:")
        ubicacionf=int(input("Ingrese a que fila desea retirar el contenedor:"))
        ubicacionc=int(input("Ingrese a que columna desea retirar el contenedor:"))

        if lista[ubicacionf-1][ubicacionc] == 0:
            lista[ubicacionf][ubicacionc] = 0
        else:
            print("hay un contenedor arriba por lo que el contenedor no se puede retirar")

       
        for i in range(n):
            for j in range (m):
                print("|", lista[i][j], "|", end=" ")
            print()
        seguir = input("¿desea continuar?:")

        while seguir == "si":
            numerocontenedor=int(input("Ingrese numero del contenedor a retirar:"))
            empresa = input("Ingrese nombre de empresa:")

            if lista[ubicacionf-1][ubicacionc] == 0:
                lista[ubicacionf][ubicacionc] = 0
            else:
                print("hay un contenedor arriba por lo que el contenedor no se puede retirar")

        
            for i in range(n):
                for j in range (m):
                    print("|", lista[i][j], "|", end=" ")
                print()
                seguir= input("¿desea continuar?:")
            seguir = input("¿desea continuar?:")
        
        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))
        
print("Gracias termino el periodo laboral")