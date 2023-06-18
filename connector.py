from settings import DOLAR_BLUE_URL
import requests


class DolarBlueConnector():
    def __init__(self, url=DOLAR_BLUE_URL):
        self.url = url

    def get_price(self) -> float:
        """function returns the current dolar blue price in Argentina
        """
        json_data = requests.get(self.url).json()
        price = json_data['blue']['value_avg']
        return price
