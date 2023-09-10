import pytest
from unittest.mock import MagicMock
from util import ProductWithDollarBluePrices


@pytest.fixture
def product_a():
    return {
        "id": 1,
        "name": "Telefono",
        "price": 100_000
    }


@pytest.fixture
def product_wiht_dollar_blue_prices(product_a):
    mock_repository = MagicMock()
    mock_repository.get_product.return_value = product_a

    mock_dollar_blue_connector = MagicMock()
    mock_dollar_blue_connector.get_price.return_value = 500

    return ProductWithDollarBluePrices(
        product_repo=mock_repository,
        dollar_blue_connector=mock_dollar_blue_connector
    )


def test_get_product(product_wiht_dollar_blue_prices):
    product = product_wiht_dollar_blue_prices.get_product(1)
    expected_product = {
        "id": 1,
        "name": "Telefono",
        "price": 100_000,
        "usd_price": 200
    }

    assert product == expected_product
