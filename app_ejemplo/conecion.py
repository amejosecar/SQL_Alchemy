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

def ejecutor_sql(codigo_sql):
    try:
        with engine.begin() as connection:
            connection.execute(text(codigo_sql))
        print("✅ Ejecución correcta de SQL")
        return True
    except Exception as e:
        print(f"❌ Error de SQLite: {e}")
        return False

def leer_tabla(tabla):
    import pandas as pd
    engine = get_engine()
    try:
        with engine.connect() as connection:
            query = text(f"SELECT * FROM {tabla}")
            df = pd.read_sql(query, connection)
        return df
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def validar_conexion_bd():
    engine = get_engine()
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ Conexión a la base de datos: OK")
    except Exception as e:
        print(f"❌ Error de conexión a la base de datos: {e}")
    finally:
        print("🔗 Conexión cerrada")