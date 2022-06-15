from shapes import *

def user_menu():
    print("1- Esfera")
    print("2- Cubo")
    print("3- Prisma Rectangular")
    seleccion = input("Por favor, seleccione qué figura geométrica desea imprimir: ")

    if seleccion == "1":
        nombre_esfera = input("Introduzca el nombre de su esfera: ")
        radio_esfera = input("Introduzca el radio de su esfera: ")

        esfera_creada = esfera(nombre_esfera, radio_esfera)
        print("Imprimiento…", nombre_esfera)

    if seleccion == "2":
        nombre_cubo = input("Introduzca el nombre de su cubo: ")
        lado_cubo = input("Introduzca el lado de su cubo: ")

        cubo_creado = cubo(nombre_cubo, lado_cubo)
        print("Imprimiento…", nombre_cubo)
        print("Preview:")
        print(cubo_creado.shape_preview())

    if seleccion == "3":
        nombre_prisma = input("Introduzca el nombre de su prisma: ")
        base_prisma = input("Introduzca la base de su prisma: ")
        altura_prisma = input("Introduzca la altura de su prisma: ")
        profundidad_prisma = input("Introduzca la profundidad de su prisma: ")

        prisma_creado = prisma_rectangular(nombre_prisma, base_prisma, altura_prisma, profundidad_prisma)
        print("Imprimiento…", nombre_prisma)
        print("Preview:")
        print(prisma_creado.shape_preview())


user_menu()