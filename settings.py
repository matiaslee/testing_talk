import os

TEST = 'test'
PROD = 'production'
DEV = 'development'
ENVIROMENT = os.getenv('ENVIROMENT', TEST)

DATABASE_FILENAME = f"database_{ENVIROMENT}.sqlite"

DOLAR_BLUE_URL = 'https://api.bluelytics.com.ar/v2/latest'