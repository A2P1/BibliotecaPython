#import numpy as np
#lista_nombre = [] # type: list
import json
diccionario = [] # Creo un diccionario vacio para almacenar libros
diccionario_aux = [] #Creo un diccinario auxiliar para almacenar los libros prestados
diccionario_usuario = [] #Diccionario vacío para guardar la informacion de los usuarios

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
            MandarFichero()
        elif opcion == 7:  
            Salir()
        
def Menu():
    print("Bienvenido a la Biblioteca de Practica")
    print("Elija una opcion")
    print("1. Agregar libro\n2. Prestar libro\n3. Devolver libro\n4. Mostrar libros disponibles\n5. Buscar libro\n6. Mandar datos a fichero\n7. Salir")
    opcion = int(input("Opcion: "))
    return opcion

def Agregar():
    while True:
        
        libros = {} #Creo el diccionario vacío para introducir los datos del libro
        
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año = int(input("Ingrese el año de publicación del libro: "))
        
        titulo_n = normalizar(titulo)
  
        libros["titulo"] = titulo_n
        libros["autor"] = autor
        libros["año"] = año
        
        diccionario.append(libros) #Añado el diccionario que contiene los datos del libro al diccionario principal
        '''with open("Libros.json","a") as file: #crea un fichero llamado Libros.json
            json.dump(libros, file) #Guarda la informacion creada en el fichero'''
        continuar = input("Desea agregar otro libro? (S/N): ").upper() #Pregunto si desea agregar otro libro
        if continuar != "S": # SI no quiere agregar otro libro, salgo del bucle
            break
    
    
def Prestar():
    
    buscar = input("Ingrese el título del libro que desea prestar: ")
    buscar_n = normalizar(buscar)
    for i in range(len(diccionario)):
        if diccionario[i]["titulo"] == buscar_n: #Busco en el diccionario si existe el libro que ha solicitado el usuario
            print(f"El libro {buscar} ha sido prestado con exito ")
            diccionario_aux.append(diccionario[i]) #Añado el libro al diccionario auxiliar
            diccionario.pop(i) #Elimino el libro prestado del diccionario
            break
        else:
            print(f"El libro {buscar} no existe") # Si no encuentra dicho libro, muestra un mensaje de error
            break
        
def Devolver():
    devolver = input("Ingrese el título del libro que desea devolver: ")
    devolver_n = normalizar(devolver)
    for i in range(len(diccionario_aux)):
        if diccionario_aux[i]["titulo"] == devolver_n: #Busco en el diccionario auxiliar si existe el libro que quiere devolver
            
            diccionario.append(diccionario_aux[i])#Muevo el libro del diccionario auxiliar al diccionario principal
            diccionario_aux.pop(i) #Elimino el libro del diccionario auxiliar
            print(f"El libro {devolver} ha sido devuelto con exito")
                
            break
        else:
            print(f"El libro {devolver} no existe")
            break   
   
def Mostrar():
    '''with open("Libros.json","r") as file:
        libros_cargados = json.load(file)
    print(libros_cargados)'''
    for i, libro in enumerate(diccionario, start=1):
        print(f"Libro {i}")
        for clave, valor in libro.items():
            print(f"{clave}: {valor}")
    
def Buscar():

    buscar = input("Ingrese el titulo del libro que quiere buscar: ")
    buscar_normalizado = normalizar(buscar)
    for i in range(len(diccionario)):
        if (diccionario[i]["titulo"] == buscar_normalizado):
            print(diccionario[i])
            break
        else:
            print("No se encontro el libro")
            break
        
def MandarFichero():
    with open("Libros.json", "w") as file: #Edito el archivo Libros.json para incluir el diccionario
        json.dump(diccionario, file, indent=3) #Guardo la información en el archivo poniendo que almacene en cada objeto 3 datos
        



def Registro(cont):
    lista = {} #Creo una lista vacía para alamcenar los datos de usuario y su contraseña
    usuario = input("Ingrese un nombre del usuario: ")
    contraseña = input("Ingrese una contrasena:")
    contraseña2 = input("Vuelva a ingresar la contrasena: ")
    
    if contraseña != contraseña2: #Compruebo que las contraseñas coinciden, si no, vuelvo a registrar
        print("Las contrasenas no coinciden")
        cont += 1
        print(cont)
        if cont == 3: #Si falla 3 veces, se sale del programa
            Salir()
        Registro(cont)
    else:
        lista["Usuario"] = usuario # Almaceno los datos en la lista
        lista["Contrasena"] = contraseña
        diccionario_usuario.append(lista) # Añado los datos al diccionario
        with open("Usuarios.json", "w") as file:
            json.dump(diccionario_usuario, file, indent=2) #Escribo el fichero Usuarios.json para añadir los datos del usuario
            
def Salir():
    exit()
def normalizar(texto):
    return texto.lower().strip()
    
main()