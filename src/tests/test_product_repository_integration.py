import pytest
from sqlalchemy.orm import sessionmaker
from product_repository import ProductRepository
from models import Product, engine

# Configuración de la sesión
Session = sessionmaker(bind=engine)

@pytest.fixture
def product_repository():
    return ProductRepository()

@pytest.mark.integration_test
def test_get_products(product_repository: ProductRepository):
    session = Session()
    try:
        list_of_products = product_repository.get_products()
        N_products = session.query(Product).count()
        assert len(list_of_products) == N_products
    finally:
        session.close()

@pytest.mark.integration_test
def test_create_product(product_repository: ProductRepository):
    session = Session()
    try:
        N_products = session.query(Product).count()
    finally:
        session.close()

    product_repository.create_product('some_name', 1)

    session = Session()
    try:
        assert session.query(Product).count() == N_products + 1
    finally:
        session.close()
