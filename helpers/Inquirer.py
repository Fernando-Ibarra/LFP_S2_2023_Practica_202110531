import os
import sys
import inquirer
from .uploadStock import upload

# MENU INICIAL
options = [
    "Cargar inventario inicial",
    "Cargar instrucciones de movimientos",
    "Crear informe de inventario",
    "Salir"
]

def validMenu( optionSelected: str ):
    if ( optionSelected == "Cargar inventario inicial" ):
        upload()
    elif ( optionSelected == "Cargar instrucciones de movimientos" ):
        print('2')
    elif ( optionSelected == "Crear informe de inventario" ):
        print('3')
    else:
        sys.exit()

def initialMenu():
    os.system('cls')
    
    menuOptions = [
        inquirer.List(
            name="menu",
            message="¿Qué desea hacer?",
            choices=options
        )
    ]
        
    answers: list = inquirer.prompt(menuOptions)
    optionSelected: int = answers["menu"]
    validMenu( optionSelected )
    
