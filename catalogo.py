import os

class Pelicula:
    def __init__(self, titulo, director, anio):
        self.titulo = titulo
        self.director = director
        self.anio = anio

    def __str__(self):
        return f"Película: {self.titulo}, {self.director}, {self.anio}"

class catalogoPeliculas:
    ruta_archivo = "catalogo.txt"

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding='utf8') as archivo:
            archivo.write(f"{pelicula.titulo},{pelicula.director},{pelicula.anio}\n")

    @classmethod
    def listar_peliculas(cls):
        try:
            with open(cls.ruta_archivo, "r", encoding='utf8') as archivo:
                for linea in archivo:
                    titulo, director, anio = linea.strip().split(",")
                    print(f"Película: {titulo}, {director}, {anio}")
        except FileNotFoundError:
            print("El catálogo está vacío.")

    @classmethod
    def eliminar_catalogo(cls):
        if os.path.exists(cls.ruta_archivo):
            os.remove(cls.ruta_archivo)
            print(f"Catálogo {cls.ruta_archivo} eliminado con éxito.")
        else:
            print("El catálogo no existe.")

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