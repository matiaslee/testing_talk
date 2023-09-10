import requests
import pytest

SERVICE_URL = "http://0.0.0.0:8000"


@pytest.fixture
def list_of_products():
    return [
        {'id': 1, 'name': 'Product_A', 'price': 1000.0},
        {'id': 2, 'name': 'Product_B', 'price': 1000000.0}
    ]


@pytest.mark.end2end_test
def test_get_products_end_point(list_of_products):
    data = requests.get(f"{SERVICE_URL}/products")
    assert data.json() == list_of_products


@pytest.mark.end2end_test
def test_get_product_with_usd_price_end_point(list_of_products):
    data = requests.get(f"{SERVICE_URL}/products_with_usd_prices/1")
    data = data.json()

    assert set(data.keys()) == {'id', 'name', 'price', 'usd_price'}
    assert data['price'] > data['usd_price']
