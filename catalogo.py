

import os 

class Pelicula:
    def __init__(self, titulo, director, anio):
        self.__titulo = titulo  #atributo privado
        self.director = director
        self.anio = anio

#metodos property y setter para poder modificar el atributo privado "titulo"
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def __str__(self):
        return f"Película: {self.__titulo}, {self.director}, {self.anio}"


class catalogoPeliculas:

    ruta_archivo = "catalogo.txt"
    @classmethod
    def agregar_pelicula(cls,pelicula):
     with open(cls.ruta_archivo,"a",encoding= 'utf8') as archivo:
        archivo.write(f"{pelicula.titulo},{pelicula.director},{pelicula.anio}\n")

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo,"r",encoding= 'utf8') as archivo:
            for linea in archivo:
                titulo, director, anio = linea.split(",")
                print(f"Película: {titulo}, {director}, {anio}")

    @classmethod
    def eliminar_catalogo(cls):
        os.remove(cls.ruta_archivo)
        print("Catálogo eliminado con éxito")

def mostrar_menu():
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")
    print("Menú principal:")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo")
    print("4. Salir")
    print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                titulo = input("Ingrese el título de la película: ")
                director = input("Ingrese el director de la película: ")
                anio = input("Ingrese el año de la película: ")
                pelicula = Pelicula(titulo, director, anio)
                catalogoPeliculas.agregar_pelicula(pelicula)
                print("Película agregada con éxito :)")
            elif opcion == 2:
                catalogoPeliculas.listar_peliculas()
            elif opcion == 3:
                catalogoPeliculas.eliminar_catalogo()
            elif opcion == 4:
                print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")
                print("Gracias por usar el programa!")
                print("~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°~°")
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Ha ocurrido un error!: {e}")


main()