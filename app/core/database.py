from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde el archivo .env
# Obtiene las credenciales de la base de datos desde las variables de entorno
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")          
    
# URL de la base de datos para MySQL.
# "mysql+mysqlconnector" es el dialecto para usar con la librería que instalaste.
# This is a better way to format the string
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Crea el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)

# Crea una sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# La clase base para nuestros modelos ORM
Base = declarative_base()

Base.metadata.create_all(bind=engine);

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()