import inquirer
import importlib

from db import initialStock, products
from models import Product
helpers = importlib.import_module("helpers")

# Path
def pathRequired( mess ) -> str:
    questions = [
    inquirer.Path(
        name='path',
        message=mess,
        path_type=inquirer.Path.FILE,
        ),
    ]
    
    answers: dict = inquirer.prompt(questions)
    path: str = answers["path"]
    return path

# Database
def chargeDB( initialStockProp = [] ):
    for stock in initialStockProp:
        product: Product = Product(name=stock['product_name'], amount=stock['product_amount'], price=stock['product_price'], location=stock['product_location'])
        products.append(product)

# Read lines
def read() -> None:
    path: str = pathRequired('Ingresa la ruta del archivo')
    file1 = open(path, 'r')
    count = 0
 
    while True:
        count += 1
    
        line = file1.readline()
        
        # Cleanning lines
        auxline = line.strip()
        
        if not auxline:
            break
        
        arrayWords = auxline.split()
        instruction = arrayWords[0]
        produc = arrayWords[1].split(";")
        
        product_dict = {
            "instruction":instruction,
            "product_name": produc[0],
            "product_amount": int(produc[1]),
            "product_price": float(produc[2]),
            "product_location": produc[3],
        }
        
        initialStock.append(product_dict)
    
    file1.close()
    chargeDB( initialStock )
    helpers.initialMenu()