# BibliotecaPython

#Práctica sencilla personal para aprender a programar en python
#El git podría ser mejor, tengo una rama suelta que dejé abandonada, y por errores en el código tuve que volver a ramas ya terminadas para arreglar problemas
#La práctica consiste en la gestión de una biblioteca con las siguientes opciones:
  - Opcion1: Agregar libros a un diccionario
  - Opcion2: Prestar libros
  - Opcion3: Devolver libros prestados
  - Opcion4: Mostrar todos los libros que tengo en la biblioteca
  - Opción5: Buscar un libro en concreto
  - Opcion6: Salir del sistema
    
#Opcion1:
  - Almaceno los datos de: título, autor y año y los guardo en una lista vacía que se crea cada vez que se accede a la opción. A continuación, hago un append para guardar dicha lista en un diccionario principal vacío       creado fuera del main. Por último, pregunto si quiere continuar introduciendo libros, y si quiere seguir introduciéndolos, se vuelve a crear una lista vacía para almacenar más datos.
  - NOTA: He creado una función para "normalizar" el título para que no existan errores cuando se escriban nombres compuestos por varias palabras. ej: Don Quijote de la Mancha.
    
#Opcion2:
  - Guardo en una variable el libro que quiere pedir el usuario y a continuación lo normalizo (ver NOTA opcion1). Después, hago un loop para buscar en todos los títulos que hay almacenados en el diccionario, uno que tenga el mismo título que el que pide el usuario. Si lo encuentra, guardo dicho libro en un diccionario vacío auxiliar (para darle uso más tarde) y lo elimino del diccionario principal. Si no encuentra el libro sale del loop
    
#Opcion3:
  - Guardo en una variable el libro que quiere devolver el usuario y a continuación lo normalizo (ver NOTA opcion1). Después, hago un loop para buscar todos los títulos que hay almacenados en el diccionario auxiliar, uno que tenga el mismo título que el que pide el usuario. Si lo encuentra, guarda el libro en el diccionario principal y lo elimina del diccionario auxiliar. Si no encuentra el libro sale del loop.
    
#Opcion4:
  - Hago un loop recorriendo todo el diccionario, imprimendo en orden los libros introducidos con un número y a continuación la información de los libros
    
#Opcion5:
  - Guardo en una variable el libro que quiere buscar el usuario y a continuación lo normalizo (ver NOTA opcion1). Después, hago un loop para buscar en todos los títulos que hay almacenados en el diccionario, uno que tenga el mismo título que el que pide el usuario. Si lo encuentra, imprime toda la información referente a ese libro. Si no encuentra el libro sale del loop.
    
#Opcion6:
  - Hago un exit() y salgo del programa

========MEJORAS========
- Utilizar la rama abandonada para imprimir correctamente el mensaje de "No se encontró ningún libro" cuando el diccionario esté vacío. Por ahora solo se sale del loop y no lo imprime

========POSIBLES EXTENSIONES DEL PROGRAMA========
Guardar y cargar datos en un archivo:

  Permite guardar el catálogo en un archivo de texto o JSON para que no se pierdan los datos al cerrar el programa.
    Usa las funciones open() y el módulo json.
    - Guardando los datos directamente no me ha funcionado. Probaré guardar todos los datos en el diccionario y posteriormente guardaré toda esa información en el fichero para guardarlo

Gestión de usuarios:

  Permite agregar un sistema de usuarios con nombres y contraseñas.
    Registra qué usuario tomó prestado cada libro.

Historial de préstamos:

  Lleva un registro de qué libros han sido prestados y devueltos, y cuándo ocurrió.
    Usa listas adicionales o un archivo para guardar este historial.

Ordenamiento y filtrado:

  Agrega una opción para ordenar los libros por título, autor o año.
    Permite filtrar libros por autor o año.

Interfaz gráfica:

  Usa una librería como tkinter para crear una interfaz gráfica para tu programa.
