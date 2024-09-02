from sqlalchemy.orm import sessionmaker
from models import Product, engine

# Configuración de la sesión
Session = sessionmaker(bind=engine)

def load_data_for_test():
    products = [
        ('Product_A', 1_000),
        ('Product_B', 1_000_000),
    ]

    session = Session()
    try:
        if session.query(Product).count() == 0:
            for name, price in products:
                product = Product(name=name, price=price)
                session.add(product)
            session.commit()
    finally:
        session.close()

if __name__ == '__main__':
    load_data_for_test()