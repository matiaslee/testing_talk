import os

TEST = 'test'
PROD = 'production'
DEV = 'development'
ENVIRONMENT = os.getenv('ENVIRONMENT', TEST)

DATABASE_FILENAME = f"database_{ENVIRONMENT}.sqlite"
