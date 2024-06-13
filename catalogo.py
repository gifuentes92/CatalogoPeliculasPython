"""El objetivo consiste en desarrollar un programa que permita llevar un registro de películas 
aplicando conceptos de programación orientada a objetos.
 El funcionamiento esperado es el siguiente:
 Al ejecutar el programa se solicita ingresar el nombre del catálogo de películas:
 Si el catálogo de películas no existe se creará uno nuevo. Este catálogo se va a guardar en un 
archivo txt donde posteriormente se guardarán las películas. Si el catálogo existe se podrá 
seguir modificando el archivo.
 Se debe mostrar un menú de opciones, que permita realizar las siguientes operaciones:
    1. Agregar Película
    2. Listar Películas
    3. Eliminar catálogo películas
    4. Salir

    
    Funcionamiento de las opciones:
 ● Agregar Película: se va a solicitar el nombre de la película y esta película se va a guardar 
en el archivo txt.
 ● Listar Peliculas: va a mostrar todas las peliculas del catalogo y guardadas en el archivo 
txt.
 ● Eliminar catálogo: elimina el archivo txt que corresponde al catálogo de películas.
 ● Salir: debe finalizar el programa mostrando un mensaje al usuario.
 Implementación POO:
 El programa debe implementar programación orientada a objetos. Se solicita:
 ● Clase Pelicula. 
○ Uno de sus atributos debe ser privado
 ● Clase CatalogoPelicula
 ○ atributo nombre
 ○ atributo ruta_archivo
 ○ métodos: agregar, listar, eliminar

    """

import os 



def mostrar_menu():
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")
    print("Menú principal:")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo")
    print("4. Salir")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")

    def main():
        catalogo = CatalogoPeliculas("catalogo.txt")
        while True:
            mostrar_menu()
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                titulo= input("Ingrese el título de la película: ")
                director= input("Ingrese el director de la película: ")
                anio= input("Ingrese el año de la película: ")
                catalogo.agregar(titulo, director, anio)
                print("Película agregada con éxito :)")
            elif opcion == 2:
                listar_peliculas(catalogo)
            elif opcion == 3:
                eliminar_catalogo(catalogo)
            elif opcion == 4:
                print("Gracias por usar el programa")
                break
            else:
                print("Opción inválida")

