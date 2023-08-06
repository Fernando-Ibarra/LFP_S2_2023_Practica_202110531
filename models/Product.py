class Product(object):
    name: str
    amount: int
    price: float
    location: str
    
    def __init__(self, name, amount, price, location) -> None:
        self.name = name
        self.amount = amount
        self.price = price
        self.location = location
        