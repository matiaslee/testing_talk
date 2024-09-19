import requests


DOLAR_BLUE_URL = 'https://api.bluelytics.com.ar/v2/latest'


class DolarBlueConnector():
    def __init__(self, url=DOLAR_BLUE_URL):
        self.url = url

    def get_price(self) -> float:
        """function returns the current dolar blue price in Argentina
        """
        json_data = requests.get(self.url).json()
        price = json_data['blue']['value_avg']
        return price

    def get_price_with_ipdb(self) -> float:

        # How to play with ipdb and testing :)
        # 1 - uncomment two lines at the bottom
        # 2 - run the following command `pytest -k test_get_price_with_ipdb -s`
        # (-k) to run a particular test.
        # (-s) is needed to allow interaction
        # 3 - write the body of this function as you want
        # 4 - update test `test_get_price_with_ipdb` accordly

        # import ipdb
        # ipdb.set_trace()

        pass
