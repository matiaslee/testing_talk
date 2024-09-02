import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch

from app import app

client = TestClient(app)


@pytest.fixture
def product_a():
    return {
        "id": 1,
        "name": "Telefono",
        "price": 100_000
    }


@pytest.fixture
def product_b():
    return {
        "id": 2,
        "name": "laptop",
        "price": 1_000_000
    }


@patch('app.ProductRepository')
def test_get_products_using_id(mock_ProductRepository, product_a):
    """Test shows how to mock:
    - First: mock a class (ProductRepository)
    - Second: mock an object of the class, particularly, we mock function
    `get_product`
    """
    mock_repository = MagicMock()
    mock_repository.get_product.return_value = product_a
    mock_ProductRepository.return_value = mock_repository

    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json() == product_a


@patch('app.ProductRepository')
def test_get_products_using_wrong_id(mock_ProductRepository):
    """ - test shows how to mock throwing an exception
    """
    mock_repository = MagicMock()
    mock_repository.get_product.side_effect = ValueError
    mock_ProductRepository.return_value = mock_repository

    response = client.get("/products/1234")

    assert response.status_code == 404
    assert response.json() == {"detail": 'Product not found'}


def test_get_products_using_wrong_type():
    """ This tests shows how fastapi checks types.
    Notice, mock is not necessary.
    """
    response = client.get("/products/i_am_not_a_number")

    assert response.status_code == 422

    expected_json = {
        'detail': [
            {
                'input': 'i_am_not_a_number',
                'loc': ['path', 'product_id'],
                'msg': 'Input should be a valid integer, unable to parse '
                'string as an integer',
                'type': 'int_parsing'
            }
        ]
    }
    assert response.json() == expected_json


@pytest.fixture
def list_of_products(product_a, product_b):
    return [product_a, product_b]


@patch('app.ProductRepository')
def test_get_products(mock_ProductRepository, list_of_products):
    """This test shows the usage of a fixture that is built using other
    features
    """
    mock_repository = MagicMock()
    mock_repository.get_products.return_value = list_of_products
    mock_ProductRepository.return_value = mock_repository

    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == list_of_products
