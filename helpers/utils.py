import inquirer

stocksGroup = []

# instruction
optionInstruction = [
    "crear_producto",
    "agregar_stock",
    "vender_producto"
]

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

# Read lines
def read() -> bool:
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
        
        if ( instruction == optionInstruction[0]):
            product_dict = {
                "instruction":instruction,
                "product_name": produc[0],
                "product_amount": int(produc[1]),
                "product_price": float(produc[2]),
                "product_location": produc[3],
            }
        
        if ( instruction == optionInstruction[1]):
            product_dict = {
                "instruction":instruction,
                "product_name": produc[0],
                "product_amount": int(produc[1]),
                "product_location": produc[3],
            }
        
        if ( instruction == optionInstruction[2]):
            product_dict = {
                "instruction":instruction,
                "product_name": produc[0],
                "product_amount": int(produc[1]),
                "product_location": produc[3],
            }
            
        stocksGroup.append(product_dict)
    file1.close()
    return stocksGroup