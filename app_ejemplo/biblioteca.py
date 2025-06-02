# biblioteca.py
from datetime import datetime, time
import sys
sys.path.append(r"C:\americo\BackEnd\clase_aitor\docu\B-POO")  # Ajusta la ruta según tu ubicación
from validar_campo import validate_string, validate_date, validate_integer, validate_float

# Clase base que representa un material de biblioteca (ahora NO abstracta)
class MaterialBiblioteca:
    def __init__(self, codigo_inventario, titulo, autor, ubicacion, tipo_material, disponible=True):
        self.__codigo_inventario = codigo_inventario
        self.__titulo = titulo
        self.__autor = autor
        self.__ubicacion = ubicacion
        self.__disponible = disponible
        self.__tipo_material = tipo_material

    # Propiedad para Título
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    # Propiedad para Autor
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        self.__autor = value

    # Propiedad para Código de Inventario
    @property
    def codigo_inventario(self):
        return self.__codigo_inventario

    @codigo_inventario.setter
    def codigo_inventario(self, value):
        self.__codigo_inventario = value

    # Propiedad para Ubicación
    @property
    def ubicacion(self):
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, value):
        self.__ubicacion = value

    # Propiedad para Disponible
    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, value):
        self.__disponible = value

    # Propiedad para Tipo de Material
    @property
    def tipo_material(self):
        return self.__tipo_material

    @tipo_material.setter
    def tipo_material(self, value):
        self.__tipo_material = value

    # Métodos de gestión
    def trasladar(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f"El item '{self.titulo}' ha sido trasladado a '{nueva_ubicacion}'.")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El item '{self.titulo}' ha sido prestado.")
        else:
            print(f"El item '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El item '{self.titulo}' ha sido devuelto.")

    def mostrar_info(self):
        # Implementación base para mostrar información común
        info = (
            f"Tipo: {self.tipo_material}\n"
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Código de Inventario: {self.codigo_inventario}\n"
            f"Ubicación: {self.ubicacion}\n"
            f"Disponible: {self.disponible}\n"
        )
        print(info)

# Subclase para Libro
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo_inventario, ubicacion, disponible,
                 isbn, numero_paginas, editorial, fecha_publicacion, edicion, 
                 idioma, peso_libro, formato_libro, tipo_literatura, resena):
        # Asignar los atributos comunes a través de la clase base y fijar el tipo a "Libro"
        super().__init__(codigo_inventario, titulo, autor, ubicacion, "Libro", disponible)
        self.__ISBN = isbn
        self.__numero_paginas = numero_paginas
        self.__editorial = editorial
        self.__fecha_publicacion = fecha_publicacion
        self.__edicion = edicion
        self.__idioma = idioma
        self.__peso_libro = peso_libro
        self.__formato_libro = formato_libro
        self.__tipo_literatura = tipo_literatura
        self.__resena = resena

    @property
    def ISBN(self):
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, value):
        self.__ISBN = value

    @property
    def numero_paginas(self):
        return self.__numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, value):
        self.__numero_paginas = value

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, value):
        self.__editorial = value

    @property
    def fecha_publicacion(self):
        return self.__fecha_publicacion

    @fecha_publicacion.setter
    def fecha_publicacion(self, value):
        self.__fecha_publicacion = value

    @property
    def edicion(self):
        return self.__edicion

    @edicion.setter
    def edicion(self, value):
        self.__edicion = value

    @property
    def idioma(self):
        return self.__idioma

    @idioma.setter
    def idioma(self, value):
        self.__idioma = value

    @property
    def peso_libro(self):
        return self.__peso_libro

    @peso_libro.setter
    def peso_libro(self, value):
        self.__peso_libro = value

    @property
    def formato_libro(self):
        return self.__formato_libro

    @formato_libro.setter
    def formato_libro(self, value):
        self.__formato_libro = value

    @property
    def tipo_literatura(self):
        return self.__tipo_literatura

    @tipo_literatura.setter
    def tipo_literatura(self, value):
        self.__tipo_literatura = value

    @property
    def resena(self):
        return self.__resena

    @resena.setter
    def resena(self, value):
        self.__resena = value

    def mostrar_info(self):
        # Mostrar información común
        super().mostrar_info()
        # Mostrar la información específica de Libro
        print(f"ISBN: {self.__ISBN}")
        print(f"Número de páginas: {self.__numero_paginas}")
        print(f"Editorial: {self.__editorial}")
        print(f"Fecha de publicación: {self.__fecha_publicacion}")
        print(f"Edición: {self.__edicion}")
        print(f"Idioma: {self.__idioma}")
        print(f"Peso del libro: {self.__peso_libro}")
        print(f"Formato del libro: {self.__formato_libro}")
        print(f"Tipo de literatura: {self.__tipo_literatura}")
        print(f"Reseña: {self.__resena}")

# Subclase para Revista
class Revista(MaterialBiblioteca):
    def __init__(self, codigo_inventario, titulo, autor, ISBN, numero_edicion, fecha_publicacion):
        # Aquí fijamos el tipo de material a "Revista"
        super().__init__(codigo_inventario, titulo, autor, "", "Revista")
        self.__ISBN = ISBN
        self.__numero_edicion = numero_edicion
        self.__fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        # Información específica para Revista
        super().mostrar_info()
        print(f"ISBN: {self.__ISBN}")
        print(f"Número de edición: {self.__numero_edicion}")
        print(f"Fecha de publicación: {self.__fecha_publicacion}")

# Subclase para DVD
class DVD(MaterialBiblioteca):
    def __init__(self, codigo_inventario, titulo, autor, ISBN, duracion, formato):
        # Aquí fijamos el tipo de material a "DVD"
        super().__init__(codigo_inventario, titulo, autor, "", "DVD")
        self.__ISBN = ISBN
        self.__duracion = duracion
        self.__formato = formato

    def mostrar_info(self):
        # Información específica para DVD
        super().mostrar_info()
        print(f"ISBN: {self.__ISBN}")
        print(f"Duración: {self.__duracion} minutos")
        print(f"Formato: {self.__formato}")
