from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound
from models import Product, engine
from typing import List

# Crea una sesión
Session = sessionmaker(bind=engine)


class ProductRepository:

    def create_product(self, name, price):
        session = Session()
        try:
            product = Product(name=name, price=price)
            session.add(product)
            session.commit()
        finally:
            session.close()

    def get_product(self, product_id: int) -> dict:
        session = Session()
        try:
            product = session.query(Product).filter(Product.id == product_id).one()
            return {'id': product.id, 'name': product.name, 'price': product.price}
        except NoResultFound:
            raise ValueError("Product does not exist")
        finally:
            session.close()

    def get_products(self) -> List[dict]:
        session = Session()
        try:
            products = session.query(Product).all()
            return [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
        finally:
            session.close()

    def update_all_prices(self, factor):
        session = Session()
        try:
            products = session.query(Product).all()
            for product in products:
                product.price *= factor
            session.commit()
        finally:
            session.close()
