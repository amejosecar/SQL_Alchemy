# SiGesBi.py
# Sistema de Gestión de Biblioteca
# -*- coding: utf-8 -*-
#
# Descripción:
#
# Crea un sistema para gestionar una biblioteca. El sistema debe permitir la gestión de diferentes
# tipos de materiales (libros, revistas, DVDs) mediante inserciones en la base de datos.
# Se reemplaza el manejo de archivo PKL por operaciones directas a la BD.

import time
import os

# Importamos las clases que representan los materiales
import time
from datetime import datetime
from biblioteca import MaterialBiblioteca, Libro, Revista, DVD  # Tus modelos ORM
from validar_campo import validate_string, validate_date, validate_integer, validate_float
from conecion import get_engine  # Esta función retorna el engine ya configurado
from sqlalchemy.orm import sessionmaker
from borrar_esquema import borrar_esquema
from conecion import crear_bd, validar_conexion
from crear_esquema import crear_esquema 

# Función auxiliar para solicitar y validar datos.
def input_validated(prompt: str, validation_function, field_name: str, **kwargs):
    while True:
        value = input(prompt)
        try:
            return validation_function(value, field_name, **kwargs)
        except ValueError as e:
            print(e)

def agregar_material():
    # Crear una sesión
    Session = sessionmaker(bind=get_engine())
    session = Session()
    
    print("\nSeleccione el tipo de material a agregar:")
    print("1. Libro")
    print("2. Revista")
    print("3. DVD")
    print("4. Volver al menú principal")
    opcion = input("Ingrese la opción (1/2/3/4): ")

    if opcion == "1":
        # Recoger datos generales
        codigo = input_validated("Ingrese el código de inventario: ", validate_integer, "Código de inventario", max_digits=6)
        titulo = input_validated("Ingrese el título: ", validate_string, "Título")
        autor = input_validated("Ingrese el autor: ", validate_string, "Autor", allow_digits=False)
        ubicacion = input_validated("Ingrese la ubicación: ", validate_string, "Ubicación")
        disponible = True  # Siempre true al agregar
        # Datos específicos para Libro
        numero_paginas = input_validated("Ingrese el número de páginas: ", validate_integer, "Número de páginas")
        isbn = input_validated("Ingrese el ISBN: ", validate_string, "ISBN")
        editorial = input_validated("Ingrese la editorial: ", validate_string, "Editorial", allow_digits=False)
        fecha_input = input_validated("Ingrese la fecha de publicación (dd/mm/aaaa): ",
                                      validate_date, "Fecha de publicación", date_format="%d/%m/%Y")
        try:
            fecha_publicacion = datetime.strptime(fecha_input, "%d/%m/%Y").strftime("%Y-%m-%d")
        except Exception as e:
            print(f"Error al convertir la fecha: {e}")
            session.close()
            return
        edicion = input_validated("Ingrese la edición: ", validate_integer, "Edición")
        idioma = input_validated("Ingrese el idioma: ", validate_string, "Idioma", allow_digits=False)
        peso_libro = input_validated("Ingrese el peso del libro (grs): ", validate_float, "Peso del libro")
        formato_libro = input_validated("Ingrese el formato del libro (Tapa blanda, Digital, Audiolibro, Tapa dura): ",
                                        validate_string, "Formato del libro", allow_digits=False)
        tipo_literatura = input_validated("Ingrese el tipo de literatura (Novela, Poesía, Teatro, etc.): ",
                                          validate_string, "Tipo de literatura", allow_digits=False)
        resena = input_validated("Ingrese la reseña: ", validate_string, "Reseña")
        
        # Crear el registro del libro pasando todos los parámetros requeridos
        nuevo_libro = Libro(
            titulo=titulo,
            autor=autor,
            codigo_inventario=int(codigo),
            ubicacion=ubicacion,
            disponible=disponible,
            isbn=isbn,
            numero_paginas=numero_paginas,
            editorial=editorial,
            fecha_publicacion=fecha_publicacion,
            edicion=str(edicion),
            idioma=idioma,
            peso_libro=peso_libro,
            formato_libro=formato_libro,
            tipo_literatura=tipo_literatura,
            resena=resena
        )
        
        session.add(nuevo_libro)
        session.commit()
        print(f"Material '{nuevo_libro.titulo}' insertado correctamente en la base de datos.")
        session.close()


    elif opcion == "2":
        # Datos generales para MaterialBiblioteca (Revista)
        codigo = input_validated("Ingrese el código de inventario: ", validate_string, "Código de inventario")
        titulo = input_validated("Ingrese el título: ", validate_string, "Título")
        autor = input_validated("Ingrese el autor: ", validate_string, "Autor", allow_digits=False)
        ubicacion = ""  # Suponemos que no interesa la ubicación para la revista
        tipo_material = "Revista"
        material_base = MaterialBiblioteca(
            codigo_inventario=codigo,
            titulo=titulo,
            autor=autor,
            ubicacion=ubicacion,
            disponible=True,
            tipo_material=tipo_material
        )
        
        # Datos específicos para Revista
        isbn = input_validated("Ingrese el ISBN: ", validate_string, "ISBN")
        numero_edicion = input_validated("Ingrese el número de edición: ", validate_integer, "Número de edición")
        fecha_input = input_validated("Ingrese la fecha de publicación (dd/mm/aaaa): ",
                                      validate_date, "Fecha de publicación", date_format="%d/%m/%Y")
        try:
            fecha_publicacion = datetime.strptime(fecha_input, "%d/%m/%Y").strftime("%Y-%m-%d")
        except Exception as e:
            print(f"Error al convertir la fecha: {e}")
            session.close()
            return
        
        nuevo_revista = Revista(
            codigo_inventario=material_base.codigo_inventario,
            isbn=isbn,
            numero_edicion=numero_edicion,
            fecha_publicacion=fecha_publicacion
        )
        
        session.add(material_base)
        session.add(nuevo_revista)
        session.commit()
        print(f"Material '{titulo}' (Revista) insertado correctamente en la base de datos.")

    elif opcion == "3":
        # Datos generales para MaterialBiblioteca (DVD)
        codigo = input_validated("Ingrese el código de inventario: ", validate_string, "Código de inventario")
        titulo = input_validated("Ingrese el título: ", validate_string, "Título")
        autor = input_validated("Ingrese el autor: ", validate_string, "Autor", allow_digits=False)
        ubicacion = ""  # No es necesaria para DVD en este ejemplo
        tipo_material = "DVD"
        material_base = MaterialBiblioteca(
            codigo_inventario=codigo,
            titulo=titulo,
            autor=autor,
            ubicacion=ubicacion,
            disponible=True,
            tipo_material=tipo_material
        )
        
        # Datos específicos para DVD
        isbn = input_validated("Ingrese el ISBN: ", validate_string, "ISBN")
        duracion = input_validated("Ingrese la duración en minutos: ", validate_integer, "Duración")
        formato = input_validated("Ingrese el formato (por ejemplo, DVD, Blu-ray): ", validate_string, "Formato", allow_digits=False)
        
        nuevo_dvd = DVD(
            codigo_inventario=material_base.codigo_inventario,
            isbn=isbn,
            duracion=duracion,
            formato=formato
        )
        
        session.add(material_base)
        session.add(nuevo_dvd)
        session.commit()
        print(f"Material '{titulo}' (DVD) insertado correctamente en la base de datos.")
    else:
        print("Regresando al menú principal.")
        session.close()
        time.sleep(5)
        return
    
    session.close()

def listar_materiales():
    from conecion import leer_tabla
    df = leer_tabla("material_biblioteca")
    if df is not None and not df.empty:
        print("\nMateriales registrados en la base de datos:")
        print(df)
    else:
        print("No se encontraron materiales registrados.")

def mostrar_detalle_material():
    codigo = input_validated("Ingrese el código de inventario: ", validate_integer, "Código de inventario")
    from conecion import leer_tabla
    df = leer_tabla("material_biblioteca")
    if df is not None and not df.empty:
        filtro = df[df["codigo_inventario"] == str(codigo)]
        if not filtro.empty:
            print("\nInformación detallada:")
            print(filtro)
        else:
            print("No se encontró ningún material con ese código.")
    else:
        print("No se encontraron materiales en la base de datos.")

# Placeholders para funciones de préstamos y usuarios
def registrar_prestamo():
    print("Función 'registrar_prestamo' no implementada.")
    
def listar_prestamos():
    print("Función 'listar_prestamos' no implementada.")
    
def devolver_material():
    print("Función 'devolver_material' no implementada.")
    
def registrar_usuario():
    print("Función 'registrar_usuario' no implementada.")
    
def listar_usuarios():
    print("Función 'listar_usuarios' no implementada.")
    
def consultar_usuario():
    print("Función 'consultar_usuario' no implementada.")

def menu_gestion_biblioteca():
    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Agregar nuevo material")
        print("2. Listar todos los materiales")
        print("3. Mostrar información detallada de un material")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_material()
        elif opcion == "2":
            print("Cargando materiales...")
            time.sleep(5)
            listar_materiales()
        elif opcion == "3":
            mostrar_detalle_material()
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        time.sleep(5)

def menu_prestamos():
    while True:
        print("\n--- Menú de Préstamos ---")
        print("1. Registrar nuevo préstamo")
        print("2. Listar préstamos activos")
        print("3. Devolver material")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            listar_prestamos()
        elif opcion == "3":
            devolver_material()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_usuarios():
    while True:
        print("\n--- Menú de Usuarios ---")
        print("1. Registrar nuevo usuario")
        print("2. Listar usuarios")
        print("3. Consultar información de un usuario")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            consultar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def gestor_de_bd_menu():
    while True:
        print("\n--- Gestor de BD ---")
        print("1. Crear base de datos")
        print("2. Validar conexión a la base de datos")
        print("3. Crear esquema de BD")
        print("4. Borrar esquema de BD")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_bd()
        elif opcion == "2":
            validar_conexion()
        elif opcion == "3":
            crear_esquema()
        elif opcion == "4":
            borrar_esquema()
        elif opcion == "5":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        time.sleep(5)

def menu():
    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Menú de Préstamos")
        print("2. Menú de Gestión de Biblioteca")
        print("3. Menú de Usuarios")
        print("4. Gestor de BD")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_prestamos()
        elif opcion == "2":
            menu_gestion_biblioteca()
        elif opcion == "3":
            menu_usuarios()
        elif opcion == "4":
            gestor_de_bd_menu()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        time.sleep(5)

if __name__ == '__main__':
    menu_gestion_biblioteca()
    #gestor_de_bd_menu()
    print("Gracias por usar el Sistema de Gestión de Biblioteca. ¡Hasta pronto!")

