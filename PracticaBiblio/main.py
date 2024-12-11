#import numpy as np
#lista_nombre = [] # type: list
import json
fichero = "Usuarios.json"
fichero2 = "Libros.json"

#diccionario_aux = [] #Creo un diccinario auxiliar para almacenar los libros prestados
try:
    with open(fichero2, "r", encoding="utf-8") as file:
        contenido2 = json.load(file)
except FileNotFoundError:
    contenido2 = []
try:
    with open(fichero, "r", encoding="utf-8") as file:
        contenido = json.load(file)
except FileNotFoundError:
    contenido = []

def main():
    cont = 0
    Registro(cont)
    opcion = 0
    while opcion != 7:
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
        
        titulo_n = normalizar(titulo)
  
        libros[titulo_n] = 0
        libros["autor"] = autor
        libros["año"] = año
        

        if isinstance (contenido2, list): #Si es una lisa, lo agrega
            contenido2.append(libros)
        elif isinstance(contenido2, dict): #Si es un diccionario, lo actualiza
            contenido2.update(libros)
        else:
            raise TypeError("Contenido no reconocido") #Si no es un diccionario o lista, lanzo un error
            
        with open(fichero2, "w", encoding="utf-8") as file:
            json.dump(contenido2, file, indent=2)
        continuar = input("Desea agregar otro libro? (S/N): ").upper() #Pregunto si desea agregar otro libro
        if continuar != "S": # SI no quiere agregar otro libro, salgo del bucle
            break
    
    
def Prestar():
    
   ''' buscar = input("Ingrese el título del libro que desea prestar: ")
    buscar_n = normalizar(buscar)
    for i in range(len(diccionario)):
        if diccionario[i]["titulo"] == buscar_n: #Busco en el diccionario si existe el libro que ha solicitado el usuario
            print(f"El libro {buscar} ha sido prestado con exito ")
            diccionario_aux.append(diccionario[i]) #Añado el libro al diccionario auxiliar
            diccionario.pop(i) #Elimino el libro prestado del diccionario
            break
        else:
            print(f"El libro {buscar} no existe") # Si no encuentra dicho libro, muestra un mensaje de error
            break'''
        
def Devolver():
   ''' devolver = input("Ingrese el título del libro que desea devolver: ")
    devolver_n = normalizar(devolver)
    for i in range(len(diccionario_aux)):
        if diccionario_aux[i]["titulo"] == devolver_n: #Busco en el diccionario auxiliar si existe el libro que quiere devolver
            
            diccionario.append(diccionario_aux[i])#Muevo el libro del diccionario auxiliar al diccionario principal
            diccionario_aux.pop(i) #Elimino el libro del diccionario auxiliar
            print(f"El libro {devolver} ha sido devuelto con exito")
                
            break
        else:
            print(f"El libro {devolver} no existe")
            break   '''
   
def Mostrar():
 '''   with open("Libros.json","r") as file:
        libros_cargados = json.load(file)
    print(libros_cargados)
    for i, libro in enumerate(diccionario, start=1):
        print(f"Libro {i}")
        for clave, valor in libro.items():
            print(f"{clave}: {valor}")'''
    
def Buscar():

    '''buscar = input("Ingrese el titulo del libro que quiere buscar: ")
    buscar_normalizado = normalizar(buscar)
    for i in range(len(diccionario)):
        if (diccionario[i]["titulo"] == buscar_normalizado):
            print(diccionario[i])
            break
        else:
            print("No se encontro el libro")
            break'''
        
'''def InicioSesion():
    usuario = input("Introduzca su nombre de usuario: ")
    #contraseña = input("Introduzca su contraseña: ")
    
    
    if usuario in diccionario_usuario:
        Menu()
    else:
        print("Usuario o contraseña incorrectos o no existe la cuenta")
        InicioSesion()'''

def Registro(cont):

    lista = {} #Creo una lista vacía para alamcenar los datos de usuario y su contraseña
    usuario = input("Ingrese un nombre del usuario: ")
    contraseña = input("Ingrese una contrasena:")
    #contraseña2 = input("Vuelva a ingresar la contrasena: ")
            

    lista[usuario] = contraseña # Almaceno los datos en la lista
    if isinstance (contenido, list): #Si es una lisa, lo agrega
        contenido.append(lista)
    elif isinstance(contenido, dict): #Si es un diccionario, lo actualiza
        contenido.update(lista)
    else:
        raise TypeError("Contenido no reconocido") #Si no es un diccionario o lista, lanzo un error
        
    with open(fichero, "w", encoding="utf-8") as file:
        json.dump(contenido, file, indent=2)
            
def Salir():
    exit()
def normalizar(texto):
    return texto.lower().strip() #Funcion para normalizar el texto
    
main()