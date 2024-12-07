def agregarLibro():
    titulo=input("Ingrese el título del libro: ")
    autor=input("Ingrese el autor del libro: ")
    publi=int(input("Ingrese el año de publicación: "))
    estrellas=int(input("¿Cuántas estrellas le da?: "))
    personaje=input("Ingrese su personaje favorito: ")
    nota=input("Añadir nota: ")

    libro={"Título" : titulo,
           "Autor" : autor,
           "Año de publicación" : publi,
           "Estrellas" : estrellas,
           "Personaje favorito" : personaje,
           "Nota" : nota}
    lista_libros.append(libro)
    print(libro)

def modificarDato():
    if operacion=="1":
        nuevo_autor=input("Ingrese el nuevo autor: ")
        lista_libros[libro]["Autor"]=nuevo_autor
        print(lista_libros[libro])
    elif operacion=="2":
        nueva_publi=int(input("Ingrese el nuevo año de publicación: "))
        lista_libros[libro]["Año de publicación"]=nueva_publi
        print(lista_libros[libro])
    elif operacion=="3":
        nuevas_estrellas=int(input("Ingrese cuántas estrellas le da: "))
        lista_libros[libro]["Estrellas"]=nuevas_estrellas
        print(lista_libros[libro])
    elif operacion=="4":
        nuevo_personaje=input("Ingrese el nuevo personaje favorito: ")
        lista_libros[libro]["Personaje favorito"]=nuevo_personaje
        print(lista_libros[libro])
    elif operacion=="5":
        nueva_nota=input("Ingrese la nueva anotación: ")
        lista_libros[libro]["Nota"]=nueva_nota
    else:
        print("Por favor, ingrese un número de operación válido.")

lista_libros=[]

print("BIENVENIDO. Ingrese el primer libro.")
agregarLibro()

while True:
    print("BIENVENIDO AL MENÚ\n1-Mostrar libros.\n2-Modificar libro.\n3-Eliminar libro.\n4-Agregar libro.\n5-Salir del programa.")
    operacion=input("Qué operación desea realizar?: ")
    if operacion=="1":
        for i in range(0,len(lista_libros)):
            print(lista_libros[i])
    elif operacion=="2":
        for i in range(0,len(lista_libros)):
            print(lista_libros[i])
        
        libro=input("Qué libro desea modificar? Ingrese el título del libro, respetando mayúsculas y minúsculas: ")
        for i in range(0,len(lista_libros)):
            if libro in lista_libros:
                print(lista_libros[libro])
            else:
                print("No se encontró el libro. Por favor, intentelo de nuevo respetando mayúsculas y minúsculas.")
    
        print("Autor: 1\nAño de publicación: 2\nEstrellas: 3\nPersonaje favorito: 4\nNota: 5")
        dato=input("Qué dato desea modificar?: ")
        modificarDato(dato)
    elif operacion=="3":
        break