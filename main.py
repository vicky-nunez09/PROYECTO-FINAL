import json

def cargar_datos():
    try:
        with open("libros.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    
def lector_datos():
    lista_datos=[]
    with open("libros.json", "r") as lector:
        lista_datos=json.load(lector)
    return lista_datos

def mostrar_libro():
    datos=lector_datos()
    print(datos)

def agregar_libro():
    try:
        with open("libros.json", "r") as archivo:
            libros = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        libros=[]        
    print("Añadir libro: ")
    ID = max([libro["id"] for libro in libros], default=0) + 1
    titulo=input("Ingrese el título del libro: ")
    autor=input("Ingrese el autor del libro: ")
    while True:
        try:
            publicacion=input("Ingrese el año de publicación: ")
            break
        except ValueError:
            print("Número no válido. Inténtelo nuevamente...")
   
    while True:
        try:
             estrellas=int(input("¿Cuántas estrellas le da? (Ingrese un número, por favor): "))
             break
        except ValueError:
             print("Número no válido. Inténtelo nuevamente...")
    
    personaje_fav=input("Ingrese su personaje favorito: ")
    reseña=input("Ingrese una reseña: ")

    nuevo_libro={
        "ID" : ID,
        "Titulo" : titulo,
        "Autor" : autor,
        "Publicacion" : publicacion,
        "Estrellas" : estrellas,
        "PersonajeFav" : personaje_fav,
        "Reseña" : reseña
    }
    libros.append(nuevo_libro)
    with open("libros.json","w") as archivo:
        json.dump(libros,archivo)

    print("El libro se ha añadido con éxito.")
    print(f"Libros registrados: \n{libros}")

    

# def modificar_libro():
#     print("Título: 1.\nAutor: 2\nAño de publicación: 3\nEstrellas: 4\nPersonaje favorito: 5\nReseña: 6")
#     dato=input("¿Qué dato desea modificar?")
#     if dato=="1":


libros=[]

while True:
    print("BIENVENIDO AL DIARIO DE LECTURAS.\n1-Mostrar libros.\n2-Agregar libro.\n3-Modificar libro.\n4-Eliminar libro.\n5-Salir del programa.")
    actividad=input("Qué actividad desea realizar?: ")
    if actividad=="1":
        mostrar_libro()
    elif actividad=="2":
        agregar_libro()
    elif actividad=="3":
        break
