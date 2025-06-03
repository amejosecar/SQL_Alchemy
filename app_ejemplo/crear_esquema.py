#crear_esquema.py
import environ
from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    DateTime,
    Boolean,
    ForeignKey,
    func
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# 1. Importaciones y Configuración del Entorno
env = environ.Env()
env.read_env(".env")
db_url = env("db_url")  # Ejemplo: sqlite:///app_ejemplo/BD_SiGesBi.db
print("Conectando a la base de datos usando:", db_url)

# 2. Creación del Motor (Engine)
engine = create_engine(db_url)

# 3. Definición del Modelo de Datos con Declarative Base
Base = declarative_base()

class MaterialBiblioteca(Base):
    __tablename__ = 'material_biblioteca'
    
    codigo_inventario = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    ubicacion = Column(String)
    disponible = Column(Boolean, nullable=False, default=True)
    tipo_material = Column(String, nullable=False)
    
    # Relaciones uno a uno con las tablas específicas y uno a muchos con préstamos
    libro = relationship("Libro", uselist=False, back_populates="material")
    revista = relationship("Revista", uselist=False, back_populates="material")
    dvd = relationship("DVD", uselist=False, back_populates="material")
    prestamos = relationship("Prestamo", back_populates="material", cascade="all, delete-orphan")

class Libro(Base):
    __tablename__ = 'libro'
    
    codigo_inventario = Column(Integer, ForeignKey('material_biblioteca.codigo_inventario'), primary_key=True)
    isbn = Column(String)
    numero_paginas = Column(Integer)
    editorial = Column(String)
    fecha_publicacion = Column(String)
    edicion = Column(String)
    idioma = Column(String)
    peso_libro = Column(Integer)  # Se puede usar Float si se prefiere
    formato_libro = Column(String)
    tipo_literatura = Column(String)
    resena = Column(String)
    
    # Relación inversa con la tabla material
    material = relationship("MaterialBiblioteca", back_populates="libro")

class Revista(Base):
    __tablename__ = 'revista'
    
    codigo_inventario = Column(Integer, ForeignKey('material_biblioteca.codigo_inventario'), primary_key=True)
    isbn = Column(String)
    numero_edicion = Column(Integer)
    fecha_publicacion = Column(String)
    
    material = relationship("MaterialBiblioteca", back_populates="revista")

class DVD(Base):
    __tablename__ = 'dvd'
    
    codigo_inventario = Column(Integer, ForeignKey('material_biblioteca.codigo_inventario'), primary_key=True)
    isbn = Column(String)
    duracion = Column(Integer)
    formato = Column(String)
    
    material = relationship("MaterialBiblioteca", back_populates="dvd")

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    usuario_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    # Se usa el valor por defecto de la función current_date() de SQLite
    fecha_registro = Column(DateTime, server_default=func.current_date())
    
    prestamos = relationship("Prestamo", back_populates="usuario", cascade="all, delete-orphan")

class Prestamo(Base):
    __tablename__ = 'prestamos'
    
    prestamo_id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_inventario = Column(String, ForeignKey('material_biblioteca.codigo_inventario'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.usuario_id'), nullable=False)
    fecha_prestamo = Column(DateTime, default=datetime.now)
    fecha_devolucion = Column(DateTime)
    devuelto = Column(Boolean, default=False)
    
    usuario = relationship("Usuario", back_populates="prestamos")
    material = relationship("MaterialBiblioteca", back_populates="prestamos")

# 6. Creación Real de la Tabla en la Base de Datos
def crear_esquema():
    # Opcional: eliminar las tablas existentes para reiniciar el esquema
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Esquema creado con éxito.")

# Crear las tablas en la base de datos
    
if __name__ == "__main__":
    crear_esquema()
