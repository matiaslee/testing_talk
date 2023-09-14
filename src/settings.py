import os

TEST = 'test'
PROD = 'production'
DEV = 'development'
ENVIRONMENT = os.getenv('ENVIRONMENT', TEST)

DATABASE_FILENAME = f"database_{ENVIRONMENT}.sqlite"

DOLAR_BLUE_URL = 'https://api.bluelytics.com.ar/v2/latest'