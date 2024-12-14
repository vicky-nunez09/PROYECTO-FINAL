import datetime

def mostrar_libros():
    archivo=open(r"libros.txt", "r", encoding="utf-8")
    contenido=archivo.readlines()
    archivo.close()

    if not contenido:
        print("El archivo está vacío. No hay libros para mostrar.")
        return

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

def agregar_libro():
    print("Añadir libro: ")

    libro=[]
    archivo=open(r"libros.txt", "r", encoding="utf-8")
    contenido=archivo.readlines()
    archivo.close()

    while True:
        try:
            ISBN=int(input("Ingrese el ISBN de su libro (escrito en el código de barra): "))
            for libro_guardado in contenido:
                if str(ISBN)==libro_guardado.split(",")[0]:
                    print("¡Error! Ya existe un libro con ese ISBN.")
                    return
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
            elif estrellas<=0:
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

    archivo=open(r"libros.txt", "a", encoding="utf-8")
    for i in libro:
        archivo.write(i)
        archivo.write(",")
    archivo.write("\n")

    print(libro)
    archivo.close()


def eliminar_libro():
    archivo=open(r"libros.txt", "r", encoding="utf-8")
    contenido=archivo.readlines()
    archivo.close()

    if not contenido:
        print("No hay libros para eliminar.")
        return

    while True:
        mostrar_libros()

        while True:
            try:
                isbn_eliminar=int(input("Ingrese el ISBN del libro a eliminar: "))
                break
            except ValueError:
                print("Número no válido. Inténtelo nuevamente...")

        libros_actualizados=[]
        libro_encontrado=False

        for libro in contenido:
            contLibro=libro.strip().split(",")
            if contLibro[0]==str(isbn_eliminar):
                libro_encontrado=True
                print("Libro encontrado y eliminado:")
                print(contLibro)
            else:
                libros_actualizados.append(libro)

        if not libro_encontrado:
            print("No se encontró ningún libro con el ISBN ingresado.")
            continue

        archivo=open(r"libros.txt", "w", encoding="utf-8")
        archivo.writelines(libros_actualizados)
        archivo.close()

        print("El libro se eliminó con éxito.")
        break

def modificar_dato():
    archivo=open(r"libros.txt", "r", encoding="utf-8")
    contenido=archivo.readlines()
    archivo.close()

    if not contenido:
        print("No hay libros para modificar.")
        return

    mostrar_libros()

    while True:
        try:
            isbn_modificar=int(input("Ingrese el ISBN del libro a modificar: "))
            break
        except ValueError:
            print("Número no válido. Inténtelo nuevamente...")

    libros_actualizados=[]
    libro_encontrado=False

    for libro in contenido:
        contLibro=libro.strip().split(",")
        if contLibro[0]==str(isbn_modificar):
            libro_encontrado=True
            print("Libro encontrado:")
            print(contLibro)
            print("Título: 1\nAutor: 2\nAño de publicación: 3\nEstrellas: 4\nPersonaje favorito: 5\nComentario: 6")

            while True:
                try:
                    dato=int(input("¿Qué dato desea modificar? "))
                    if dato<=0:
                        print("Opción no válida, inténtelo nuevamente...")
                    elif dato>6:
                        print("Opción no válida, inténtelo nuevamente...")
                    else:
                        break
                except ValueError:
                    print("Número no válido. Inténtelo nuevamente...")

            nuevo_dato=input("Ingrese el nuevo dato: ")

            contLibro[dato]=nuevo_dato
            print("El dato ha sido modificado con éxito.")

        libros_actualizados.append(",".join(contLibro) + "\n")

    if not libro_encontrado:
        print("No se encontró ningún libro con el ISBN ingresado.")

    archivo=open(r"libros.txt", "w", encoding="utf-8")
    archivo.writelines(libros_actualizados)
    archivo.close()

    print("Archivo actualizado.")

while True:
    print("BIENVENIDO AL DIARIO DE LECTURAS.\n1-Mostrar libros.\n2-Agregar libro.\n3-Modificar libro.\n4-Eliminar libro.\n5-Salir del programa.")
    actividad=input("Qué actividad desea realizar?: ")
    if actividad=="1":
        mostrar_libros()
    elif actividad=="2":
        agregar_libro()
    elif actividad=="3":
        modificar_dato()
    elif actividad=="4":
        eliminar_libro()
    elif actividad=="5":
        print("Fin del programa.")
        break
    else:
        print("Ingrese una opción válida...")
