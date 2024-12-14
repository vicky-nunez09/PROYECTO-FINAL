import datetime

def mostrar_libros():
    archivo=open(r"libros.txt","r",encoding="utf-8")

    contenido=archivo.readlines()
    listaLibros=[]
    
    for libro in contenido:
        contLibro=libro.split(",")
        dicc={}
        dicc["ISBN"]=contLibro[0]
        dicc["Título"]=contLibro[1]
        dicc["Autor"]=contLibro[2]
        dicc["Publicación"]=contLibro[3]
        dicc["Estrellas"]=contLibro[4]
        dicc["Personaje favorito"]=contLibro[5]
        dicc["Comentario"]=contLibro[6]
        listaLibros.append(dicc)

    for libro in listaLibros:
        print(libro)

    archivo.close()

def agregar_libro():

    print("Añadir libro: ")
    
    libro=[]    
    archivo=open(r"libros.txt","a",encoding="utf-8")
    
    while True:
        try:
            ISBN=int(input("Ingrese el ISBN de su libro (escrito en el código de barra): "))
            break
        except ValueError:
            print("Número no válido. Inténtelo nuevamente...")
    
    libro.append(str(ISBN))
    
    titulo=input("Ingrese el título del libro: ")
    libro.append(titulo)
    autor=input("Ingrese el autor del libro: ")
    libro.append(autor)

    while True:
        try:
            publicacion=int(input("Ingrese el año de publicación (negativo para a.C): "))
            if publicacion>datetime.datetime.now().year:
                print("Número no válido. Inténtelo nuevamente...")
            else:
                break
        except ValueError:
            print("Número no válido. Inténtelo nuevamente...")

    libro.append(str(publicacion))

    while True:
        try:
            estrellas=int(input("¿Cuántas estrellas le da? (1-5): "))
            if estrellas>5:
                print("Número no válido. Inténtelo nuevamente...")
            elif estrellas==0:
                print("Número no válido. Inténtelo nuevamente...")
            elif estrellas<0:
                print("Número no válido. Inténtelo nuevamente...")
            else:
                break
        except ValueError:
             print("Número no válido. Inténtelo nuevamente...")
    libro.append(str(estrellas))
    personaje_fav=input("Ingrese su personaje favorito: ")
    libro.append(personaje_fav)
    comentario=input("Ingrese un comentario: ")
    libro.append(comentario)

    for i in libro:
        archivo.write(i)
        archivo.write(",")

    archivo.write("\n")

    print(libro)
    archivo.close()

def eliminar_libro():
    while True:
        try:
            isbn_eliminar=int(input("Ingrese el ISBN del libro a eliminar: "))
            break
        except ValueError:
            print("Número no válido. Inténtelo nuevamente...")
    

while True:
    print("BIENVENIDO AL DIARIO DE LECTURAS.\n1-Mostrar libros.\n2-Agregar libro.\n3-Modificar libro.\n4-Eliminar libro.\n5-Salir del programa.")
    actividad=input("Qué actividad desea realizar?: ")
    if actividad=="1":
        mostrar_libros()
    elif actividad=="2":
        agregar_libro()
    elif actividad=="4":
        eliminar_libro()

