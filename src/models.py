from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DATABASE_FILENAME

# Configuración de la base de datos
engine = create_engine(f'sqlite:///{DATABASE_FILENAME}', echo=True)
Base = declarative_base()


# Define la entidad Product
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)


# Crea las tablas en la base de datos
Base.metadata.create_all(engine)

# Crea una sesión
Session = sessionmaker(bind=engine)
session = Session()
