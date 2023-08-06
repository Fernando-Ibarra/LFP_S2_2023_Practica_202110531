import importlib

from db import products, stocks
from models import Product
helpers = importlib.import_module("helpers")


# Database
def chargeDB( stock: {} ):
    product: Product = Product(name=stock['product_name'], amount=stock['product_amount'], price=stock['product_price'], location=stock['product_location'])
    products.append(product)

def onStartChangeDB() -> None:
    stocksOut = helpers.read()
    print(stocksOut)
    for stock in stocksOut:
        if stock['instruction'] == helpers.optionInstruction[0]:
            chargeDB( stock )
        elif stock['instruction'] == helpers.optionInstruction[1]:
            pass
        else:
            pass
    stocksOut.clear()
    stocks.clear()
    helpers.initialMenu()