import os
import datetime

def outTxtFIle(filename: str, products = []):
    path = os.path.join(os.getcwd(), filename)
    now = datetime.datetime.now()
    with open(path, "w+", encoding="utf-8") as f:
        f.write('Informe de Inventario:\n')
        f.write('Producto   Cantidad   Precio Unitario   Valor Total   Ubicación\n')
        f.write('---------------------------------------------------------------\n')
        for product in products:
            f.write(f' { product.name }       { product.amount }            Q { product.price }       Q { product.price * product.amount }       { product.location }\n')
        f.write(F'Generado el { now.strftime("%Y-%m-%d") }')
        