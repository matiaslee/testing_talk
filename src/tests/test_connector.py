import pytest
from unittest.mock import MagicMock, patch
from requests.exceptions import Timeout


from connector import DolarBlueConnector


@pytest.fixture
def dolar_blue_connector():
    return DolarBlueConnector()


@pytest.fixture
def json_data():
    return {
        'oficial': {
            'value_avg': 256.0, 'value_sell': 261.0, 'value_buy': 251.0},
        'blue': {
            'value_avg': 489.5, 'value_sell': 492.0, 'value_buy': 487.0},
        'oficial_euro': {
            'value_avg': 278.5, 'value_sell': 284.0, 'value_buy': 273.0},
        'blue_euro': {
            'value_avg': 532.0, 'value_sell': 535.0, 'value_buy': 529.0},
        'last_update':
            '2023-06-16T14:40:32.069001-03:00'
    }


@patch('connector.requests')
def test_get_price(
    mock_requests, dolar_blue_connector: DolarBlueConnector, json_data: dict
):
    """ - Test shows how to mock get from module requests.
    - The test tests function get_price
    """

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = json_data

    # specify the return value of the get() method
    mock_requests.get.return_value = mock_response

    # mock the response
    price = dolar_blue_connector.get_price()

    assert price == 489.5


@patch('connector.requests')
def test_get_price_with_timeout(
    mock_requests, dolar_blue_connector: DolarBlueConnector
):
    """ - Test shows how to "assert" an exception.
    - The test tests that time out exception is not catched by
    the connector
    """
    mock_requests.get.side_effect = Timeout

    with pytest.raises(Timeout):
        dolar_blue_connector.get_price()


def test_get_price_with_ipdb(
    dolar_blue_connector: DolarBlueConnector
):
    """ auxiliar test to show how to use ipdb for developing """
    assert dolar_blue_connector.get_price_with_ipdb() is None
