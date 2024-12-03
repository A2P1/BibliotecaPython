
def main():
    opcion = Menu()
    if opcion == 1:
        Agregar()
    elif opcion == 2:
        Prestar()
    elif opcion == 3:
        Devolver()
    elif opcion == 4:
        Mostrar()
    elif opcion == 5:
        Buscar()
    elif opcion == 6:  
        Salir()
        
def Menu():
    print("Bienvenido a la Biblioteca de Practica")
    print("Elija una opcion")
    print("1. Agregar libro\n2. Prestar libro\n3. Devolver libro\n4. Mostrar libros disponibles\n5. Buscar libro\n6. Salir")
    opcion = int(input("Opcion: "))
    return opcion

def Agregar():
    print("Ha elegido la opcion 1")
    return
def Prestar():
    print("Ha elegido la opcion 2")
    return
def Devolver():
    print("Ha elegido la opcion 3")
    return
def Mostrar():
    print("Ha elegido la opcion 4")
    return
def Buscar():
    print("Ha elegido la opcion 5")
    return
def Salir():
    exit()
    
main()