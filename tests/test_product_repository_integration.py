import pytest
from pony.orm import count, db_session

from product_repository import ProductRepository
from models import Product


@pytest.fixture
def product_repository():
    return ProductRepository()


@pytest.mark.integration_test
@db_session
def test_get_products(product_repository: ProductRepository):
    list_of_products = product_repository.get_products()
    assert len(list_of_products) == count(Product.select())


@pytest.mark.integration_test
def test_create_product(product_repository: ProductRepository):

    with db_session:
        N_products = count(Product.select())

    product_repository.create_product('some_name', 1)

    with db_session:
        assert count(Product.select()) == N_products + 1
