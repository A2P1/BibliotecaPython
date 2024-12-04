#import numpy as np
#lista_nombre = [] # type: list
diccionario = [] # Creo un diccionario vacio para almacenar libros
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
    while True:
        
        libros = {} #Creo el diccionario vacío para introducir los datos del libro
        
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año = int(input("Ingrese el año de publicación del libro: "))
        
        libros["titulo"] = titulo
        libros["autor"] = autor
        libros["año"] = año
        diccionario.append(libros) #Añado el diccionario que contie los datos del libro al diccionario principal
        continuar = input("Desea agregar otro libro? (S/N): ").upper() #Pregunto si desea agregar otro libro
        if continuar != "S": # SI no quiere agregar otro libro, salgo del bucle
            break
    
    
def Prestar():
    
    return
def Devolver():
    print("Ha elegido la opcion 3")
    return
def Mostrar():
   for i, libro in enumerate(diccionario, start=1):
        print(f"Libro {i}")
        for clave, valor in libro.items():
            print(f"{clave}: {valor}")
    
def Buscar():
    
    print("Ha elegido la opcion 5")
    return
def Salir():
    exit()
    
main()