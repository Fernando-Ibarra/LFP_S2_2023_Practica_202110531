import inquirer

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
def read() -> []:
    stocksGroup = []
    path: str = pathRequired('Ingresa la ruta del archivo')
    file1 = open(path, mode = 'r', encoding='utf-8')
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
        product = arrayWords[1].split(";")
        
        if ( instruction == optionInstruction[0]):
            product_dict = {
                "instruction":instruction,
                "product_name": product[0],
                "product_amount": int(product[1]),
                "product_price": float(product[2]),
                "product_location": product[3],
            }
        
        if ( instruction == optionInstruction[1]):
            product_dict = {
                "instruction":instruction,
                "product_name": product[0],
                "product_amount": int(product[1]),
                "product_location": product[2],
            }
        
        if ( instruction == optionInstruction[2]):
            product_dict = {
                "instruction":instruction,
                "product_name": product[0],
                "product_amount": int(product[1]),
                "product_location": product[2],
            }
            
        stocksGroup.append(product_dict)
    file1.close()
    return stocksGroup