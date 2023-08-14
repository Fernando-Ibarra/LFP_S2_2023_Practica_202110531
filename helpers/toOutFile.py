import os
import datetime

def outTxtFIle(filename: str, products = []):
    path = os.path.join(os.getcwd(), filename)
    now = datetime.datetime.now()
    producWithStock = [product for product in products if product.amount > 0 ]
    producWithStock.sort(key=lambda product: product.location)
    with open(path, "w+", encoding="utf-8") as f:
        f.write('Informe de Inventario:\n')
        f.write('Producto   Cantidad   Precio Unitario   Valor Total   Ubicación\n')
        f.write('---------------------------------------------------------------\n')
        for product in producWithStock:
            f.write(f' { product.name }       { product.amount }            Q { product.price }       Q { product.price * product.amount }       { product.location }\n')
        f.write(F'Generado el { now.strftime("%m-%d-%Y %H:%M:%S") }')
        