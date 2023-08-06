import os
import sys
import inquirer
import importlib

helpers = importlib.import_module("helpers")
from db import products


# Main Menu
options = [
    "Cargar inventario inicial",
    "Cargar instrucciones de movimientos",
    "Crear informe de inventario",
    "Salir"
]

def validMenu( optionSelected: str ):
    if ( optionSelected == "Cargar inventario inicial" ):
        helpers.onStartChangeDB()
    elif ( optionSelected == "Cargar instrucciones de movimientos" ):
        print('2')
    elif ( optionSelected == "Crear informe de inventario" ):
        helpers.outTxtFIle(filename="stock.txt", products=products)
    else:
        sys.exit()

def initialMenu():
    os.system('cls')
    
    menuOptions = [
        inquirer.List(
            name="menu",
            message="¿Qué desea hacer?",
            choices=options,
            carousel=True
        )
    ]
        
    answers: list = inquirer.prompt(menuOptions)
    optionSelected: int = answers["menu"]
    validMenu( optionSelected )