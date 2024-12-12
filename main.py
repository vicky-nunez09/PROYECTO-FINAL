import datetime

def mostrar_libros():
    file=open(r"libros.txt","r",encoding="utf-8")

    contenido=file.readlines()
    listaLibros=[]

    for libro in contenido:
        contLibro=libro.split(",")
        dicc={}
        dicc["Título"]=contLibro[0]
        dicc["Autor"]=contLibro[1]
        dicc["Publicación"]=contLibro[2]
        dicc["Estrellas"]=contLibro[3]
        dicc["Personaje favorito"]=contLibro[4]
        dicc["Comentario"]=contLibro[5]

    listaLibros.append(dicc)

    for i in range(len(contenido)):
        print(contenido[i])

    file.close()

def agregar_libro():

    archivo=open(r"libros.txt","a",encoding="utf-8")
    print("Añadir libro: ")

    libro=[]
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

    str(publicacion)
    libro.append(publicacion)

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
    str(estrellas)
    libro.append(estrellas)
    personaje_fav=input("Ingrese su personaje favorito: ")
    libro.append(personaje_fav)
    comentario=input("Ingrese un comentario: ")
    libro.append(comentario)
    archivo.write("\n")

    for i in libro:
        archivo.write(i)
        archivo.write(",")

    print(libro)



# # while True:
# #     print("BIENVENIDO AL DIARIO DE LECTURAS.\n1-Mostrar libros.\n2-Agregar libro.\n3-Modificar libro.\n4-Eliminar libro.\n5-Salir del programa.")
# #     actividad=input("Qué actividad desea realizar?: ")
# #     if actividad=="1":
# #         mostrar_libros()
# #     elif actividad=="2":
# #         agregar_libro()
# #     elif actividad=="3":
# #         break
