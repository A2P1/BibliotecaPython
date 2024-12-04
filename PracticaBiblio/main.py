#import numpy as np
#lista_nombre = [] # type: list
diccionario = {}
def main():
    opcion = 0
    while opcion != 6:
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
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año de publicación del libro: "))
    
    diccionario["titulo"] = titulo
    diccionario["autor"] = autor
    diccionario["año"] = año
    
def Prestar():
    print("Ha elegido la opcion 2")
    return
def Devolver():
    print("Ha elegido la opcion 3")
    return
def Mostrar():
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    return
    
def Buscar():
    
    print("Ha elegido la opcion 5")
    return
def Salir():
    exit()
    
main()