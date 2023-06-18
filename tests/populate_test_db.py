from pony.orm import db_session, count

from models import Product


@db_session
def load_data_for_test():
    products = [
        ('Product_A', 1_000),
        ('Product_B', 1_000_000),
    ]

    with db_session:
        if count(Product.select()) == 0:
            for name, price in products:
                Product(name=name, price=price)


if __name__ == '__main__':
    load_data_for_test()
