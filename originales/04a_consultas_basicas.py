from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

import environ
env = environ.Env()
env.read_env(".env")
db_url = env("db_url")

# URL de conexión a la base de datos SQLite (puedes cambiarlo a tu configuración PostgreSQL)
db_url = 'sqlite:///ejemplo.db'

# Crear una instancia de motor (engine)
engine = create_engine(db_url)

# Crear una instancia de MetaData
# metadata = MetaData()

# Crear la clase de modelo utilizando Declarative Base
# Base = declarative_base(metadata=metadata)

# Definir la clase de modelo para la tabla 'tabla_personas'
from modelos import Tabla_Personas

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Insertar un nuevo registro
nuevo_registro = Tabla_Personas(nombre='Ejemplo', apellido1='Primero', dni='123456789')
session.add(nuevo_registro)
session.commit()

session.query(Tabla_Personas).count()
# Consulta: Obtener todos los registros
registros = session.query(Tabla_Personas).all()
print("Todos los registros:")
for registro in registros:
    print(registro.id, registro.nombre, registro.apellido1, registro.dni, registro.date_created)

# Consulta: Filtrar por el valor de un campo
    # Con filter
filtro_nombre = session.query(Tabla_Personas).filter(Tabla_Personas.nombre=='Ejemplo').first()
print("\nRegistro con nombre 'Ejemplo':", filtro_nombre.id, filtro_nombre.nombre, filtro_nombre.apellido1, filtro_nombre.dni, filtro_nombre.date_created)
session.commit()
    # Con filter_by
filtro_nombre = session.query(Tabla_Personas).filter_by(nombre='Ejemplo').first()
print("\nRegistro con nombre 'Ejemplo':", filtro_nombre.id, filtro_nombre.nombre, filtro_nombre.apellido1, filtro_nombre.dni, filtro_nombre.date_created)


# Actualizar un registro
registro_a_actualizar = session.query(Tabla_Personas).filter_by(nombre='Ejemplo').first()
registro_a_actualizar.nombre = 'NuevoNombre'
session.commit()

# Consulta: Verificar la actualización
registro_actualizado = session.query(Tabla_Personas).filter_by(nombre='NuevoNombre').first()
print("\nRegistro con nombre 'NuevoNombre':", registro_actualizado.id, registro_actualizado.nombre, registro_actualizado.apellido1, registro_actualizado.dni, registro_actualizado.date_created)

# Eliminar un registro
registro_a_eliminar = session.query(Tabla_Personas).filter_by(nombre='NuevoNombre').first()
session.delete(registro_a_eliminar)
session.commit()

# Consulta: Verificar la eliminación
registro_eliminado = session.query(Tabla_Personas).filter_by(nombre='NuevoNombre').first()
print("\nRegistro eliminado:", registro_eliminado)

# Cerrar la sesión
session.close()
