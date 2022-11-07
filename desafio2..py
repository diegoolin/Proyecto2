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
            numerocontenedor=input("ingrese el numero del contenedor: ")
            nombreempresa= input("ingrese el nombre de la empresa propietaria: ")
            ubicacion=numerocontenedor+"/"+nombreempresa
            for i in range(n):
                for j in range(m):
                    if lista[i][j]==ubicacion:
                        print("el contenedor",lista[i][j],"se encuentra en la pila",[i],"en la posición",[j])  

            seguir = input("¿desea continuar?:")
           
        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

    if menu == 2:        
        numerocontenedor=input("Ingrese numero del contenedor a añadir:")
        nombreempresa = input("Ingrese nombre de la empresa:")
        salir=False
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if lista[i][j]==0:
                    lista[i][j]=numerocontenedor+"/"+nombreempresa
                    salir=True
                    break
            if salir:
                break
        for i in range(n):
            for j in range (m):
                print("|",lista[i][j], "|", end=" ")
            print()            

        seguir= input("¿desea continuar?: ")
        while seguir== "si":
            numerocontenedor=input("Ingrese numero del contenedor a añadir:")
            nombreempresa = input("Ingrese nombre de la empresa:")
            salir=False
            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    if lista[i][j]==0:
                        lista[i][j]=numerocontenedor+"/"+nombreempresa
                        salir=True
                        break
                if salir:
                    break               
            for i in range(n):
                for j in range (m):
                    print("|",lista[i][j], "|", end=" ")
                print()  
            seguir = input("¿desea continuar?:")

        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada laboral \nIngrese opción:"))

    if menu == 3:
        numerocontenedor=input("Ingrese numero del contenedor a retirar:")
        nombreempresa = input("Ingrese nombre de empresa:")
        if numerocontenedor==lista[i][j]:
            lista[i].remove(numerocontenedor)
            print(numerocontenedor)
            break    


        for i in range(n):
            for j in range (m):
                print("|", lista[i][j], "|", end=" ")
            print()
        seguir = input("¿desea continuar?:")

        while seguir == "si":
            numerocontenedor=input("Ingrese numero del contenedor a retirar:")
            empresa = input("Ingrese nombre de empresa:")


        
            for i in range(n):
                for j in range (m):
                    print("|", lista[i][j], "|", end=" ")
                print()
                seguir= input("¿desea continuar?:")
            seguir = input("¿desea continuar?:")
        
        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))
        
print("Gracias termino el periodo laboral")