# gestion_usuarios.py
from sqlalchemy.orm import sessionmaker
from conecion import get_engine
from models import Usuario

def registrar_usuario():
    """
    Permite registrar un nuevo usuario solicitando nombre, apellido y email.
    Valida que el email no esté registrado antes de insertar.
    """
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    print("\n--- Registrar Nuevo Usuario ---")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    email = input("Ingrese el email: ")

    # Validación: Verificar si ya existe usuario con ese email.
    existente = session.query(Usuario).filter_by(email=email).first()
    if existente:
        print(f"\nError: El email '{email}' ya está registrado para el usuario {existente.nombre} {existente.apellido}.")
        session.close()
        return

    try:
        nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, email=email)
        session.add(nuevo_usuario)
        session.commit()
        print(f"\nUsuario '{nombre} {apellido}' registrado exitosamente con ID: {nuevo_usuario.usuario_id}.")
    except Exception as e:
        session.rollback()
        print("\nError al registrar el usuario:", e)
    finally:
        session.close()


def listar_usuarios():
    """
    Lista todos los usuarios registrados mostrando el ID, nombre, apellido, email y fecha de registro.
    """
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    print("\n--- Listado de Usuarios ---")
    usuarios = session.query(Usuario).all()
    if usuarios:
        for u in usuarios:
            print(f"\nID: {u.usuario_id}, Nombre: {u.nombre} {u.apellido}, Email: {u.email}, Fecha de Registro: {u.fecha_registro}")
    else:
        print("\nNo hay usuarios registrados.")
    session.close()


def consultar_usuario():
    """
    Permite consultar la información de un usuario ingresando el ID o email.
    Muestra los datos del usuario.
    """
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    criterio = input("\nIngrese el ID del usuario o email a consultar: ").strip()
    usuario = None
    if criterio.isdigit():
        usuario = session.query(Usuario).filter_by(usuario_id=int(criterio)).first()
    else:
        usuario = session.query(Usuario).filter_by(email=criterio).first()

    if usuario:
        print("\n--- Detalle del Usuario ---")
        print(f"ID: {usuario.usuario_id}")
        print(f"Nombre: {usuario.nombre} {usuario.apellido}")
        print(f"Email: {usuario.email}")
        print(f"Fecha de Registro: {usuario.fecha_registro}")
    else:
        print("\nNo se encontró usuario con ese criterio.")

    session.close()


def eliminar_usuario():
    """
    Permite eliminar un usuario de la BD.
    Se solicita el ID o email del usuario a eliminar y se pide confirmación antes de borrarlo.
    """
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    criterio = input("\nIngrese el ID del usuario o email a eliminar: ").strip()
    usuario = None
    if criterio.isdigit():
        usuario = session.query(Usuario).filter_by(usuario_id=int(criterio)).first()
    else:
        usuario = session.query(Usuario).filter_by(email=criterio).first()

    if not usuario:
        print("\nNo se encontró usuario con ese criterio.")
        session.close()
        return

    confirm = input(f"\nEstá seguro de eliminar al usuario '{usuario.nombre} {usuario.apellido}' (ID: {usuario.usuario_id})? (s/n): ")
    if confirm.lower() == 's':
        try:
            session.delete(usuario)
            session.commit()
            print(f"\nUsuario '{usuario.nombre} {usuario.apellido}' eliminado correctamente.")
        except Exception as e:
            session.rollback()
            print("\nError al eliminar el usuario:", e)
        finally:
            session.close()
    else:
        print("\nOperación cancelada.")
        session.close()
