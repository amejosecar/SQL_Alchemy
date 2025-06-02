from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_esquema import MaterialBiblioteca, Libro, Revista, DVD, Prestamo
from datetime import datetime, timedelta

# Cambia esto si usas PostgreSQL:
# connection_string = "postgresql://dvm_owner:contrasena@ep-plain-wave-a5cnkp69-pooler.us-east-2.aws.neon.tech/dvm?sslmode=require"
connection_string = "sqlite:///app_ejemplo/BD_SiGesBi.db"

# Crear engine y sesión
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()


# Ejemplo: Insertar un registro en la tabla material_biblioteca
nuevo_material = MaterialBiblioteca(
    codigo_inventario='MAT001',
    titulo='Libro de Prueba',
    autor='Autor Ejemplo',
    ubicacion='Estantería A',
    tipo_material='Libro'
)
session.add(nuevo_material)
session.commit()

# Consulta de prueba
registros = session.query(MaterialBiblioteca).all()
for r in registros:
    print(r.codigo_inventario, r.titulo)
session.close()

Session = sessionmaker(bind=engine)
session = Session()

# Ejemplo: Insertar un registro en la tabla material_biblioteca
nuevo_material = MaterialBiblioteca(
    codigo_inventario='MAT001',
    titulo='Libro de Prueba',
    autor='Autor Ejemplo',
    ubicacion='Estantería A',
    tipo_material='Libro'
)
session.add(nuevo_material)
session.commit()

# Consulta de prueba
registros = session.query(MaterialBiblioteca).all()
for r in registros:
    print(r.codigo_inventario, r.titulo)
session.close()
