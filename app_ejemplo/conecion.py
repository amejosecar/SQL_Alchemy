#connection.py
import os
import environ
from sqlalchemy import create_engine, text

# Cargar las variables de entorno desde el archivo .env
env = environ.Env()
env.read_env(".env")
db_url = env("db_url")  # Se espera: 'sqlite:///app_ejemplo/BD_SiGesBi.db'
print("Conectando a la base de datos desde:", db_url)

# Creación del motor (Engine)
engine = create_engine(db_url, echo=False, future=True)

def get_engine():
    return engine

def crear_bd():
    """
    Crea la base de datos. En SQLite, el archivo se genera al establecer la primera conexión.
    """
    try:
        # Conexión trivial para forzar la creación de la base de datos
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("La base de datos se ha creado (o ya existe).")
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

def validar_conexion():
    """
    Valida la conexión comprobando la existencia del archivo SQLite.
    Si existe, se imprime: "OK: El archivo de la BD existe."
    De lo contrario, se muestra: "Error: El archivo BD_SiGesBi.db no existe."
    """
    # Extraer la ruta del archivo desde db_url (eliminando el prefijo "sqlite:///")
    prefix = "sqlite:///"
    if db_url.startswith(prefix):
        file_path = db_url[len(prefix):]
    else:
        file_path = db_url
    
    if os.path.exists(file_path):
        print("OK: El archivo de la BD existe.")
    else:
        print(f"Error: El archivo {os.path.basename(file_path)} no existe.")

if __name__ == "__main__":
    # Primero validamos (para saber si el archivo existe o no)
    validar_conexion()
    # Creamos la base de datos (esto forzará la creación del archivo si no existe)
    crear_bd()
    # Validamos de nuevo para comprobar que el archivo se ha generado
    validar_conexion()
