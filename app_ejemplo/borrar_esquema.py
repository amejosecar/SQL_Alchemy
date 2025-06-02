# borrar_esquema.py

from crear_esquema import Base, engine

def borrar_esquema():
    """
    Elimina (drop) todas las tablas definidas en el modelo.
    """
    Base.metadata.drop_all(engine)
    print("Esquema borrado con éxito.")

if __name__ == '__main__':
    borrar_esquema()