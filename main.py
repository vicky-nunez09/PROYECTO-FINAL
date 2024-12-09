import json

def cargar_datos():
    try:
        with open("libros.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    
def lector_datos():
    libros = []
    with open("libros.json", "r") as archivo:
        libros = json.load(archivo)
        print(libros)

def agregar_libro():
    libros=[]
    print("Añadir libro: ")
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

def buscar_libro():
    