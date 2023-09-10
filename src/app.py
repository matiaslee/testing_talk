from fastapi import FastAPI, HTTPException
from product_repository import ProductRepository
from util import ProductWithDollarBluePrices
from connector import DolarBlueConnector
from requests import Timeout

app = FastAPI()


@app.post('/products')
def create_product(name: str, price: float):
    repo = ProductRepository()
    repo.create_product(name=name, price=price)
    return {'message': 'Product created'}


@app.get('/products')
def get_products():
    repo = ProductRepository()
    return repo.get_products()


@app.get('/products/{product_id}')
def get_product(product_id: int):
    repo = ProductRepository()
    try:
        return repo.get_product(product_id)
    except ValueError:
        raise HTTPException(status_code=404, detail='Product not found')


@app.put('/products/')
def update_products_price(factor: float):
    repo = ProductRepository()
    repo.update_all_prices(factor)
    return {'message': 'Prices updated'}


@app.get('/products_with_usd_prices/{product_id}')
def get_product_with_usd_price(product_id: int):
    repo = ProductWithDollarBluePrices(
        ProductRepository(), DolarBlueConnector()
    )
    try:
        return repo.get_product(product_id)
    except ValueError:
        raise HTTPException(status_code=404, detail='Product not found')
    except Timeout:
        HTTPException(status_code=504, detail='Timeout...')


@app.get('/products_with_usd_prices/')
def get_products_with_usd_price():
    repo = ProductWithDollarBluePrices(
        ProductRepository(), DolarBlueConnector()
    )
    try:
        return repo.get_products()
    except Timeout:
        HTTPException(status_code=504, detail='Timeout...')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
