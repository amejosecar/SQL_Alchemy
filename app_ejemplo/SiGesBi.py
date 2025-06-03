# SiGesBi.py
from menu import menu_gestion_biblioteca, menu_prestamos, menu_usuarios, gestor_de_bd

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
            gestor_de_bd()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == '__main__':
    menu()
