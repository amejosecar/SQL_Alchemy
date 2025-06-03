#gestor_de_bd.py
import time
from conecion import crear_bd, validar_conexion
from models import MaterialBiblioteca, Libro, Revista, DVD, Usuario, Prestamo
from borrar_esquema import borrar_esquema

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
