from models import Product
from pony.orm import db_session
from typing import List


class ProductRepository:

    @db_session
    def create_product(self, name, price):
        Product(name=name, price=price)

    @db_session
    def get_product(self, product_id: int) -> dict:
        product = Product.get(id=product_id)
        if product is None:
            raise ValueError("Product does not exist")
        return {'id': product.id, 'name': product.name, 'price': product.price}

    @db_session
    def get_products(self) -> List[dict]:
        products = [
            {'id': product.id, 'name': product.name, 'price': product.price}
            for product in Product.select()
        ]
        return products

    @db_session
    def update_all_prices(self, factor):
        for p in Product.select():
            p.price = p.price * factor
