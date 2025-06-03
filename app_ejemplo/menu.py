#menu.py
from gestion_material import agregar_material, listar_materiales, mostrar_detalle_material, eliminar_material
from gestion_prestamos import registrar_prestamo, listar_prestamos, devolver_material
import time
from conecion import crear_bd, validar_conexion
from crear_esquema import crear_esquema
from borrar_esquema import borrar_esquema
from models import Usuario


def menu_gestion_biblioteca():
    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Agregar nuevo material")
        print("2. Listar todos los materiales")
        print("3. Mostrar información detallada de un material")
        print("4. Borrar un material")        
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_material()
        elif opcion == "2":
            listar_materiales()
        elif opcion == "3":
            mostrar_detalle_material() 
        elif opcion == "4":
            eliminar_material()
        elif opcion == "5":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

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
        print("4. Eliminar un usuario")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            consultar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def gestor_de_bd():
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