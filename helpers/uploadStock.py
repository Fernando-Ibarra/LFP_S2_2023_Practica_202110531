import importlib

from db import products, errorMaganement
from models import Product
helpers = importlib.import_module("helpers")

# Database
def chargeDB( stock: {} ):
    product: Product = Product(name=stock['product_name'], amount=stock['product_amount'], price=stock['product_price'], location=stock['product_location'])
    products.append(product)
    
def changeDB( stock: {}, method: int ):
    
    if ( method == 1):
        productsFilterName = [product for product in products if product.name == stock['product_name'] ]
        productsFilterLocation = [product for product in productsFilterName if product.location == stock['product_location'] ]
        if( len(productsFilterLocation) > 0 ):
                productsFilterLocation[0].amount += stock['product_amount']
        else:
            error = f"{ stock['product_name'] } no existe en la ubicación { stock['product_location'] } - No se puede { stock['instruction'] }"
            errorMaganement.append( error )

    if ( method == 2):
        productsFilterName = [product for product in products if product.name == stock['product_name'] ]
        productsFilterLocation = [product for product in productsFilterName if product.location == stock['product_location'] ]
        if( len(productsFilterLocation) > 0 ):
            if( productsFilterLocation[0].amount >= stock['product_amount'] ):
                productsFilterLocation[0].amount -= stock['product_amount']
            else:
                error = f"La cantidad { stock['product_amount'] } de { stock['product_name'] } no se encuentra disponible"
                errorMaganement.append( error )
        else:
            error = f"{ stock['product_name'] } no existe en la ubicación { stock['product_location'] } - No se puede { stock['instruction'] }"
            errorMaganement.append( error )

def onStartChangeDB() -> None:
    stocks = helpers.read()
    for stock in stocks:
        if stock['instruction'] == helpers.optionInstruction[0]:
            chargeDB( stock )
        elif stock['instruction'] == helpers.optionInstruction[1]:
            changeDB( stock, 1 )
        else:
            changeDB( stock, 2 )
    else:
        stocks.clear()
        
    if( len(errorMaganement) > 0 ):
        for i, error in enumerate(errorMaganement):
            print(f"Error { i + 1 }: { error }")
    helpers.pause()
    helpers.initialMenu()