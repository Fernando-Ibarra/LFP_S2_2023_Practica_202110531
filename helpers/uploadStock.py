import inquirer
from db import initialStock

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

def upload() -> None:
    path: str = pathRequired('Ingresa la ruta del archivo')
    file1 = open(path, 'r')
    count = 0
 
    while True:
        count += 1
    
        line = file1.readline()
        
        # Quitar salto de linea
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
    for stock in initialStock:
        print(f"Intrucción: { stock['instruction'] }")
        print(f"Nombre: { stock['product_name'] }")
        print(f"Cantidad: { stock['product_amount'] }")
        print(f"Precio: { stock['product_price'] }")
        print(f"Locación: { stock['product_location'] }", end="\n")