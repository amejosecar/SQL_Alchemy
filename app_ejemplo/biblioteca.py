# biblioteca.py
from models import MaterialBiblioteca, Libro, Revista, DVD

class MaterialBiblioteca(Base):
    __tablename__ = "material_biblioteca"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Esta columna es esencial
    codigo_inventario = Column(Integer, unique=True, nullable=False)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    ubicacion = Column(String, nullable=True)
    tipo_material = Column(String, nullable=False)
    disponible = Column(Boolean, default=True)

    __mapper_args__ = {
         'polymorphic_on': tipo_material,
         'polymorphic_identity': 'material'
    }

class Libro(MaterialBiblioteca):
    __tablename__ = "libros"

    id = Column(Integer, ForeignKey("material_biblioteca.id"), primary_key=True)
    isbn = Column(String, nullable=False)
    numero_paginas = Column(Integer, nullable=False)
    editorial = Column(String, nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    edicion = Column(String, nullable=False)
    idioma = Column(String, nullable=False)
    peso_libro = Column(Float, nullable=False)
    formato_libro = Column(String, nullable=False)
    tipo_literatura = Column(String, nullable=False)
    resena = Column(Text, nullable=True)

    __mapper_args__ = {
         'polymorphic_identity': 'libro'
    }

class Revista(MaterialBiblioteca):
    __tablename__ = "revistas"

    id = Column(Integer, ForeignKey("material_biblioteca.id"), primary_key=True)
    isbn = Column(String, nullable=False)
    numero_edicion = Column(Integer, nullable=False)
    fecha_publicacion = Column(Date, nullable=False)

    __mapper_args__ = {
         'polymorphic_identity': 'revista'
    }

class DVD(MaterialBiblioteca):
    __tablename__ = "dvds"

    id = Column(Integer, ForeignKey("material_biblioteca.id"), primary_key=True)
    isbn = Column(String, nullable=False)
    duracion = Column(Integer, nullable=False)
    formato = Column(String, nullable=False)

    __mapper_args__ = {
         'polymorphic_identity': 'dvd'
    }
