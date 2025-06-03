# gestion_material.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from conecion import get_engine
from models import MaterialBiblioteca, Libro, Revista, DVD  # Ahora se importan desde models.py
from validar_campo import validate_string, validate_date, validate_integer, validate_float
from datetime import datetime


def input_validated(prompt: str, validation_function, field_name: str, **kwargs):
    while True:
        value = input(prompt)
        try:
            return validation_function(value, field_name, **kwargs)
        except ValueError as e:
            print(e)

def agregar_material():
    # Inicializa la sesión solo cuando se requiere
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("\nSeleccione el tipo de material a agregar:")
    print("1. Libro")
    print("2. Revista")
    print("3. DVD")
    print("4. Volver al menú principal")
    opcion = input("Ingrese la opción (1/2/3/4): ")

    if opcion == "1":
        # Rama para Libro
        print("\n--- Agregar Libro ---")
        titulo = input_validated("Ingrese el título: ", validate_string, "Título")
        autor = input_validated("Ingrese el autor: ", validate_string, "Autor", allow_digits=False)
        codigo = input_validated("Ingrese el código de inventario: ", validate_integer, "Código de inventario")
        isbn = input_validated("Ingrese el ISBN: ", validate_string, "ISBN")
        numero_paginas = input_validated("Ingrese el número de páginas: ", validate_integer, "Número de páginas")
        editorial = input_validated("Ingrese la editorial: ", validate_string, "Editorial", allow_digits=False)
        fecha_publicacion = input_validated("Ingrese la fecha de publicación (dd/mm/aaaa): ", 
                                            validate_date, "Fecha de publicación", date_format="%d/%m/%Y")
        edicion = input_validated("Ingrese la edición: ", validate_integer, "Edición")
        idioma = input_validated("Ingrese el idioma: ", validate_string, "Idioma", allow_digits=False)
        peso_libro = input_validated("Ingrese el peso del libro (grs): ", validate_float, "Peso del libro")
        formato_libro = input_validated("Ingrese el formato del libro: ", validate_string, "Formato del libro", allow_digits=False)
        tipo_literatura = input_validated("Ingrese el tipo de literatura: ", validate_string, "Tipo de literatura", allow_digits=False)
        resena = input_validated("Ingrese la reseña: ", validate_string, "Reseña")

        # Validación: verificar si ya existe un material con el mismo código
        existente = session.query(MaterialBiblioteca).filter_by(codigo_inventario=codigo).first()
        if existente:
            
            print(f"\nError: El código de inventario {codigo} ya está registrado para el material '{existente.titulo}'.")
            session.close()
            return  # Se detiene la inserción sin continuar

        try:
            nuevo_libro = Libro(
                titulo=titulo,
                autor=autor,
                codigo_inventario=codigo,
                isbn=isbn,
                numero_paginas=numero_paginas,
                editorial=editorial,
                fecha_publicacion=datetime.strptime(fecha_publicacion, "%d/%m/%Y"),
                edicion=edicion,
                idioma=idioma,
                peso_libro=peso_libro,
                formato_libro=formato_libro,
                tipo_literatura=tipo_literatura,
                resena=resena
            )
            session.add(nuevo_libro)
            session.commit()
            
            print(f"\nMaterial '{nuevo_libro.titulo}' insertado correctamente.")
        except IntegrityError as e:
            session.rollback()
            
            print(f"\nError al insertar el material: {e}")
        finally:
            session.close()

    elif opcion == "2":
        # Rama para Revista
        print("\n--- Agregar Revista ---")
        titulo = input_validated("Ingrese el título: ", validate_string, "Título")
        autor = input_validated("Ingrese el autor: ", validate_string, "Autor", allow_digits=False)
        codigo = input_validated("Ingrese el código de inventario: ", validate_integer, "Código de inventario")
        isbn = input_validated("Ingrese el ISBN: ", validate_string, "ISBN")
        numero_edicion = input_validated("Ingrese el número de edición: ", validate_integer, "Número de edición")
        fecha_publicacion = input_validated("Ingrese la fecha de publicación (dd/mm/aaaa): ", 
                                            validate_date, "Fecha de publicación", date_format="%d/%m/%Y")
        
        # Validación: verificar si ya existe un material con el mismo código
        existente = session.query(MaterialBiblioteca).filter_by(codigo_inventario=codigo).first()
        if existente:
            print(f"\nError: El código de inventario {codigo} ya está registrado para el material '{existente.titulo}'.")
            session.close()
            return

        try:
            nuevo_revista = Revista(
                titulo=titulo,
                autor=autor,
                codigo_inventario=codigo,
                isbn=isbn,
                numero_edicion=numero_edicion,
                fecha_publicacion=datetime.strptime(fecha_publicacion, "%d/%m/%Y")
            )
            session.add(nuevo_revista)
            session.commit()
            print(f"\nMaterial '{nuevo_revista.titulo}' (Revista) insertado correctamente.")
        except IntegrityError as e:
            session.rollback()
            print(f"\nError al insertar el material: {e}")
        finally:
            session.close()

    elif opcion == "3":
        # Rama para DVD
        print("\n--- Agregar DVD ---")
        titulo = input_validated("Ingrese el título: ", validate_string, "Título")
        autor = input_validated("Ingrese el autor: ", validate_string, "Autor", allow_digits=False)
        codigo = input_validated("Ingrese el código de inventario: ", validate_integer, "Código de inventario")
        isbn = input_validated("Ingrese el ISBN: ", validate_string, "ISBN")
        duracion = input_validated("Ingrese la duración en minutos: ", validate_integer, "Duración")
        formato_input = input_validated("Ingrese el formato (por ejemplo, DVD, Blu-ray): ", 
                                        validate_string, "Formato", allow_digits=False)
        
        # Validación a nivel de código de inventario
        existente = session.query(MaterialBiblioteca).filter_by(codigo_inventario=codigo).first()
        if existente:
            print(f"\nError: El código de inventario {codigo} ya está registrado para el material '{existente.titulo}'.")
            session.close()
            return

        try:
            nuevo_dvd = DVD(
                titulo=titulo,
                autor=autor,
                codigo_inventario=codigo,
                isbn=isbn,
                duracion=duracion,
                formato=formato_input
            )
            session.add(nuevo_dvd)
            session.commit()
            print(f"\nMaterial '{nuevo_dvd.titulo}' (DVD) insertado correctamente.")
        except IntegrityError as e:
            session.rollback()
            print(f"\nError al insertar el material: {e}")
        finally:
            session.close()

    else:
        print("\nRegresando al menú principal.")
        session.close()


### Función para listar todos los materiales
def listar_materiales():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    print("\n--- Listado de Materiales ---")
    materiales = session.query(MaterialBiblioteca).all()
    if materiales:
        for m in materiales:
            print(f"\nCódigo: {m.codigo_inventario}, Título: {m.titulo}, Autor: {m.autor}, Tipo: {m.tipo_material}")
    else:
        print("\nNo se encontraron materiales registrados.")

    session.close()


### Función para mostrar el detalle de un material (consulta por código)
def mostrar_detalle_material():
    from sqlalchemy.orm import with_polymorphic
    from conecion import get_engine
    from sqlalchemy.orm import sessionmaker
    from biblioteca import MaterialBiblioteca

    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    codigo_input = input("\nIngrese el código de inventario a consultar: ")
    try:
        codigo = int(codigo_input)
    except ValueError:
        print("\nEl código debe ser un número entero.")
        session.close()
        return

    # Creamos el alias polimórfico para MaterialBiblioteca y todas sus subclases
    mp = with_polymorphic(MaterialBiblioteca, "*")
    material = session.query(mp).filter(mp.codigo_inventario == codigo).first()

    if material:
        print("\n--- Detalle del Material ---")
        print(f"Código: {material.codigo_inventario}")
        print(f"Título: {material.titulo}")
        print(f"Autor: {material.autor}")
        print(f"Ubicación: {material.ubicacion}")
        print(f"Disponible: {material.disponible}")
        print(f"Tipo: {material.tipo_material}")
        # Según el tipo de material se muestran atributos específicos
        if material.tipo_material == 'libro':
            print(f"ISBN: {material.isbn}")
            print(f"Número de páginas: {material.numero_paginas}")
            print(f"Editorial: {material.editorial}")
            print(f"Fecha de publicación: {material.fecha_publicacion}")
            print(f"Edición: {material.edicion}")
            print(f"Idioma: {material.idioma}")
            print(f"Peso del libro: {material.peso_libro}")
            print(f"Formato del libro: {material.formato_libro}")
            print(f"Tipo de literatura: {material.tipo_literatura}")
            print(f"Reseña: {material.resena}")
        elif material.tipo_material == 'revista':
            print(f"ISBN: {material.isbn}")
            print(f"Número de edición: {material.numero_edicion}")
            print(f"Fecha de publicación: {material.fecha_publicacion}")
        elif material.tipo_material == 'dvd':
            print(f"ISBN: {material.isbn}")
            print(f"Duración: {material.duracion}")
            print(f"Formato: {material.formato}")
    else:
        print("\nNo se encontró material con ese código.")

    session.close()

def eliminar_material():
    """
    Elimina un material de la base de datos en función del código de inventario.
    Se solicita al usuario el código, se busca el registro y se pide confirmación para la eliminación.
    """
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    print()
    codigo_input = input("\nIngrese el código de inventario a eliminar: ")
    try:
        codigo = int(codigo_input)
    except ValueError:
        print("\nEl código debe ser un número entero.")
        session.close()
        return

    # Buscar el material según el código de inventario
    material = session.query(MaterialBiblioteca).filter_by(codigo_inventario=codigo).first()
    if not material:
        print(f"\nNo se encontró material con el código {codigo}.")
        session.close()
        return

    # Confirmar la eliminación
    confirm = input(f"\n¿Está seguro de eliminar el material '{material.titulo}' (Tipo: {material.tipo_material})? (s/n): ")
    if confirm.lower() == 's':
        try:
            session.delete(material)
            session.commit()
            print()
            print(f"\nMaterial '{material.titulo}' eliminado correctamente.")
        except Exception as e:
            session.rollback()
            print()
            print(f"\nError al eliminar el material: {e}")
        finally:
            session.close()
    else:
        print()
        print("Operación cancelada.")

        session.close()
