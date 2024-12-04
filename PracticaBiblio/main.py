#import numpy as np
#lista_nombre = [] # type: list
diccionario = [] # Creo un diccionario vacio para almacenar libros
#diccionario_aux = [] #Creo un diccinario auxiliar para almacenar los libros prestados
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
    
    buscar = input("Ingrese el título del libro que desea prestar: ")
    for i in range(len(diccionario)):
        if diccionario[i]["titulo"] == buscar: #Busco en el diccionario si existe el libro que ha solicitado el usuario
            print(f"El libro {buscar} ha sido prestado con exito ")
           # diccionario_aux.append(diccionario[i]) #Añado el libro al diccionario auxiliar
            diccionario.pop(i) #Elimino el libro prestado del diccionario
            break
        else:
            print(f"El libro {buscar} no existe") # Si no encuentra dicho libro, muestra un mensaje de error
            break
        
def Devolver():
    return
def Mostrar():
   for i, libro in enumerate(diccionario, start=1):
        print(f"Libro {i}")
        for clave, valor in libro.items():
            print(f"{clave}: {valor}")
    
def Buscar():

    buscar = input("Ingrese el titulo del libro que quiere buscar: ")
    for i in range(len(diccionario)):
        if (diccionario[i]["titulo"] == buscar):
            print(diccionario[i])
            break
        else:
            print("No se encontro el libro")
            break

def Salir():
    exit()
    
main()