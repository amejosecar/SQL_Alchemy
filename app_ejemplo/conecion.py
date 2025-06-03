# connection.py
import os
import environ
from sqlalchemy import create_engine, text
from modelo_base import Base

env = environ.Env()
env.read_env(".env")
db_url = env("db_url")  # Ejemplo: 'sqlite:///app_ejemplo/BD_SiGesBi.db'
print("Conectando a la base de datos desde:", db_url)

# Crear el motor de conexión sin forzar la creación del esquema
engine = create_engine(db_url, echo=False, future=True)

def get_engine():
    return engine

def crear_bd():
    """
    Crea la base de datos y el esquema (todas las tablas definidas en los modelos)
    """
    try:
        # Opcionalmente, para asegurarte una limpieza en desarrollo:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        print("La base de datos y el esquema se han creado correctamente.")
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

def validar_conexion():
    prefix = "sqlite:///"
    file_path = db_url[len(prefix):] if db_url.startswith(prefix) else db_url
    if os.path.exists(file_path):
        print("OK: El archivo de la BD existe.")
    else:
        print(f"Error: El archivo {os.path.basename(file_path)} no existe.")

if __name__ == "__main__":
    validar_conexion()
    crear_bd()
    validar_conexion()
