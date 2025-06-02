from sqlalchemy import MetaData, Column, Integer, String, DateTime, event
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

# Definir el objeto MetaData y la clase base
metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Tabla_Personas(Base):
    __tablename__ = 'tabla_personas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)
    apellido1 = Column(String(30), nullable=False)
    apellido2 = Column(String(30), nullable=True)
    dni = Column(String(9), nullable=False, unique=True)
    date_created = Column(DateTime, default=datetime.now(timezone.utc))

# Configuración de eventos (before_insert) para establecer la fecha de creación
def set_date_created(mapper, connection, target):
    if target.date_created is None:
        target.date_created = datetime.now(timezone.utc)

event.listen(Tabla_Personas, 'before_insert', set_date_created)