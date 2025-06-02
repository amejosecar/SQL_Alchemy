"""
Conexión a una base de datos postgres gratuita
creada en https://railway.com/
"""
from sqlalchemy import create_engine
import environ

env = environ.Env()
env.read_env(".env")

db_management_sys = "postgresql"
db_name = "railway"  # Si tu base de datos se llama 'railway' o ajusta según corresponda
db_user = "postgres"
db_password = "LAjXtwXMQUWbcqCVnFIPNJeBLcNsfqdS"  # Asegúrate de que la contraseña sea la correcta

# Usa el host público en lugar del interno
db_host = "centerbeam.proxy.rlwy.net"
db_port = "38291"  # Asegúrate de incluir el puerto que corresponde

# Reconstruimos el string de conexión. Si Railway requiere SSL, puedes agregar '?sslmode=require' al final.
db_url = f"{db_management_sys}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
#print("Conectando a la base de datos con:", db_url)

engine = create_engine(db_url)

try:
    with engine.connect() as connection:
        print("Conexión exitosa")
        # Aquí puedes realizar operaciones en la base de datos
except Exception as e:
    print(f"Error de conexión: {e}")

