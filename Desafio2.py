n= int(input("ingrese la cantidad maxima de contenedores que se pueden apilar: "))
m= int(input("ingrese la cantidad maxima de pilas que se pueden hacer: "))
print()
puerto= []
seguir = ""
for i in range(n):
    puerto.append([])
    for j in range (m):
        puerto[i].append(0) 

for i in range(n):
    for j in range (m):
        print("|", puerto[i][j], "|", end=" ")
    print()
print()
menu = int(input("1 para ubicar un contenedor \n2 para ingresar el contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada laboral \nIngrese opción:"))

while menu !=4:
    if menu == 1:
        numero = int(input("ingrese el numero del contenedor para ubicarlo: "))
        print("hay un total de", numero.count(numero), "contenedores con ese numero y las empresas con ese numero son", empresa)
        nombreempresa = input("ingrese el nombre de la empresa:")
        
        consulta = input("¿desea continuar?:")
        while consulta == "si":
            numero = int(input("ingrese el numero del contenedor: "))
            nombreempresa = input("ingrese el nombre de la empresa propietaria: ")
            consulta = input("¿desea continuar?:")
           
        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

    if menu == 2:
        
        numerocontenedora=int(input("Ingrese numero del contenedor a añadir:"))
        nombreempresa = input("Ingrese empresa:")
        ubicacionc= int(input("Ingrese a que fila desea ingresar el contenedor:"))
        ubicaciona= int(input("Ingrese a que columna desea ingresar el contenedor:"))

        puerto[ubicacionc][ubicaciona] = numerocontenedora, nombreempresa

       
        for i in range(n):
            for j in range (m):
                print("|",puerto[i][j],"|",end=" ")
            print()
        
        seguir= input("¿desea continuar?: ")
        while seguir== "si":
            numerocontenedora=int(input("Ingrese numero del contenedor a añadir:"))
            nombreempresa = input("Ingrese nombre de la empresa:")
            ubicacionc= int(input("Ingrese a que fila desea ingresar el contenedor:"))
            ubicaciona= int(input("Ingrese a que columna desea ingresar el contenedor:"))

            puerto[ubicacionc][ubicaciona] = numerocontenedora, nombreempresa

        
            for i in range(n):
                for j in range (m):
                    print("|",puerto[i][j],"|",end=" ")
                print()
            consulta = input("¿desea continuar?:")

        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada laboral \nIngrese opción:"))

    if menu == 3:
        numerocontenedora=int(input("Ingrese numero del contenedor a retirar:"))
        nombreempresa = input("Ingrese nombre de empresa:")

        if puerto[ubicacionc-1][ubicaciona] == None:
            puerto[ubicacionc][ubicaciona] = None
        else:
            print("hay un contenedor arriba por lo que el contenedor no se puede retirar")

       
        for i in range(n):
            for j in range (m):
                print("|", puerto[i][j], "|", end=" ")
            print()
        seguir = input("¿desea continuar?:")
        while seguir == "si":
            numerocontenedora=int(input("Ingrese numero del contenedor a retirar:"))
            empresa = input("Ingrese nombre de empresa:")

            if puerto[ubicacionc-1][ubicaciona] == None:
                puerto[ubicacionc][ubicaciona] = None
            else:
                print("hay un contenedor arriba por lo que el contenedor no se puede retirar")

        
            for i in range(n):
                for j in range (m):
                    print("|", puerto[i][j], "|", end=" ")
                print()
                seguir= input("¿desea continuar?:")
            seguir = input("¿desea continuar?:")

        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))