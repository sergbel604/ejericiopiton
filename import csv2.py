import csv
lista=[]
def menu():
    print("")
    print("-"*150)
    print(".-.-.-.-.-.- J U G A D O R E S     D E L    N I U P I    Q U E    H A N    A N O T A D O    G O L E S -.-.-.-.-.-.")
    print("-"*150)
    print("")
    print("1.- Agregar jugador")
    print("2.- Listar jugadores")
    print("3.- Imprimir datos del jugador")
    print("4.- Eliminar jugador")
    print("5.- Estadisticas")
    print("6.- Generar bbdd")
    print("7.- cargar datos desde archivo")
    print("0.- Salir")
def eliminar(list):
    for x in list:
        if num==x[0]:
            lista.remove(x)
            print("Se ha eliminado correctamente")
def promedio(list):
    acumula=0
    elementos=len(list)
    for x in lista:
        acumula=int(x[2])+acumula
        prom=acumula/elementos
    print("Promedio: ",prom)
def maxim(list):
    for y in list:
        maximos=max(int(y[2]) for y in list)
    print("Maximo de goles: ",maximos)
def bdd():
    with open('jugadorcitos.csv','w',newline='')as jugadorcitos:
            escritor_csv=csv.writer(jugadorcitos)
            escritor_csv.writerows(lista)
            print("Se genero base de datos")
def cargar():
    with open('jugadorcitos.csv','r',newline='')as jugadorcitos:
            lector_csv=csv.reader(jugadorcitos)
            for i in lector_csv:
                lista.append(i)
            print("Base de datos cargada")
while True:
    menu()
    op=int(input("Ingrese una opcion: "))
    if op==1:
        print("---- Agregar Jugador ----")
        num=int(input("Ingrese numero de  camiseta: "))
        nombre=input("Ingrese su nombre: ")
        goles=int(input("Ingrese cantidad de goles: "))
        if goles>0 and goles<6:
            print("Clasificacion: Amateur")
            clasificacion="amateur"
        if goles>5 and goles<16:
            print("Clasificacion: Semi")
            clasificacion="semi"
        if goles>15:
            print("Clasificacion: Pro")
            clasificacion="pro"
        jugadores=[num,nombre,int(goles),clasificacion]
        lista.append(jugadores)
        print("Se ha añadido un jugador")
    elif op==2:
        print("---- Listar jugadores ----")
        for i in lista:
            print("Numero: ",i[0]," Nombre: ",i[1]," Goles: ",i[2]," Clasificacion: ",i[3])
            
    elif op==3:
        encontrado=False
        print("---- Buscar Jugador ----")
        num=int(input("Ingrese numero q esta buscando: "))
        for i in lista:
            if num==i[0]:
                print("Numero: ",i[0]," Nombre: ",i[1]," Goles: ",i[2]," Clasificacion: ",i[3])
                encontrado=True
        if encontrado==False:
            print("No encontrado")
    elif op==4:
        encontrado=False
        print("---- Elimar jugador ----")
        num=int(input("Ingrese numero q esta buscando: "))
        for i in lista:
            if num==i[0]:
                print("Numero: ",i[0]," Nombre: ",i[1]," Goles: ",i[2]," Clasificacion: ",i[3])
                encontrado=True
                while True: 
                    print("1.- Eliminar")
                    print("0.- Volver al menu principal")
                    op2=int(input("Ingrese opcion: "))
                    if op2==1:
                        eliminar(lista)
                        break
                    elif op2==0:
                        print("volviendo")
                        break
                    else:
                        print("opcion invalida")
    elif op==5:
        print("---- Estadisticas ----")
        promedio(lista)
        maxim(lista)
    elif op==6:
        print("---- Generar bbdd ----")
        bdd()
    elif op==7:
        print("---- Cargar bbdd ----")
        cargar()
    elif op==0:
        print("Adios")
        break
    else:
        print("Opcion invalida")