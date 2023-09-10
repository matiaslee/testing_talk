from typing import List

from product_repository import ProductRepository
from connector import DolarBlueConnector


class ProductWithDollarBluePrices:
    def __init__(
        self, product_repo: ProductRepository,
        dollar_blue_connector: DolarBlueConnector
    ):
        self.product_repo = product_repo
        self.dollar_blue_connector = dollar_blue_connector

    def get_product(self, product_id: int) -> dict:
        product = self.product_repo.get_product(product_id)
        dollar_blue_price = self.dollar_blue_connector.get_price()
        product['usd_price'] = product['price'] / dollar_blue_price
        return product

    def get_products(self) -> List[dict]:
        products = self.product_repo.get_products()
        dollar_blue_price = self.dollar_blue_connector.get_price()
        for product in products:
            product['usd_price'] = product['price'] / dollar_blue_price

        return products
