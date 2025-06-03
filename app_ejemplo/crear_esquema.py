# crear_esquema.py
import environ
from sqlalchemy import create_engine
from modelo_base import Base
from models import MaterialBiblioteca, Libro, Revista, DVD, Usuario, Prestamo  # Importa todos los modelos
import os

env = environ.Env()
env.read_env(".env")
db_url = env("db_url")
print("Conectando a la base de datos usando:", db_url)

engine = create_engine(db_url)

def crear_esquema():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Esquema creado con éxito.")

if __name__ == "__main__":
    crear_esquema()
