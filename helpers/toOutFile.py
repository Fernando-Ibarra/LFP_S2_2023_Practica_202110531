import os
import datetime
import importlib
from tabulate import tabulate
helpers = importlib.import_module("helpers")

def outTxtFIle(filename: str, products = []):
    path = os.path.join(os.getcwd(), filename)
    now = datetime.datetime.now()
    producWithStock = [product for product in products if product.amount > 0 ]
    producWithStock.sort(key=lambda product: product.location)
    productTablePrint = [["Producto","Cantidad", "Precio Unitario", "Valor Total", "Ubicación"]]
    for product in producWithStock:
        productRow = [ product.name, product.amount, f'Q { product.price }', f'Q { product.price * product.amount }', product.location]
        productTablePrint.append(productRow)
    tabulate(productTablePrint,headers="firstrow")
    with open(path, "w+", encoding="utf-8") as f:
        f.write('                       Informe de Inventario:\n')
        f.write(tabulate(productTablePrint, headers="firstrow", showindex="always", tablefmt="simple_grid", numalign="center"))
        f.write('\n')
        f.write(F'  Generado el { now.strftime("%m-%d-%Y %H:%M:%S") }')
        f.close()
    helpers.pause()
    helpers.initialMenu()
        