from conecion import ejecutor_sql

sql_statements = [
    """
    CREATE TABLE IF NOT EXISTS material_biblioteca (
        codigo_inventario TEXT PRIMARY KEY,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ubicacion TEXT,
        disponible INTEGER NOT NULL DEFAULT 1,
        tipo_material TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS libro (
        codigo_inventario TEXT PRIMARY KEY,
        isbn TEXT,
        numero_paginas INTEGER,
        editorial TEXT,
        fecha_publicacion TEXT,
        edicion TEXT,
        idioma TEXT,
        peso_libro REAL,
        formato_libro TEXT,
        tipo_literatura TEXT,
        resena TEXT,
        FOREIGN KEY (codigo_inventario) REFERENCES material_biblioteca(codigo_inventario)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS revista (
        codigo_inventario TEXT PRIMARY KEY,
        isbn TEXT,
        numero_edicion INTEGER,
        fecha_publicacion TEXT,
        FOREIGN KEY (codigo_inventario) REFERENCES material_biblioteca(codigo_inventario)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS dvd (
        codigo_inventario TEXT PRIMARY KEY,
        isbn TEXT,
        duracion INTEGER,
        formato TEXT,
        FOREIGN KEY (codigo_inventario) REFERENCES material_biblioteca(codigo_inventario)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        fecha_registro TEXT DEFAULT (date('now'))
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS prestamos (
        prestamo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_inventario TEXT NOT NULL,
        usuario_id INTEGER NOT NULL,
        fecha_prestamo TEXT NOT NULL,
        fecha_devolucion TEXT,
        devuelto INTEGER DEFAULT 0,
        FOREIGN KEY (codigo_inventario) REFERENCES material_biblioteca(codigo_inventario),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
    );
    """
]

def crear_esquema():
    for statement in sql_statements:
        print("Ejecutando sentencia SQL:")
        print(statement)
        ejecutor_sql(statement)
        print("-" * 60)

if __name__ == '__main__':
    crear_esquema()
    print("Esquema creado con éxito.")
