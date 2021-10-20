import csv
from os import read


class Item:

    pay_rate = 0.8  # The pay rate after 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the recived arguments
        assert price >= 0, f"Price {price} is not greater than or eaqual to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        # Asignar el self objeto
        self.name = name
        self.price = price
        self.quantity = quantity

    def calcular_precio_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the flaots taht are point
        # For i.e: 5.0 10.0
        if isinstance(num, float):
            # Count out the float that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()
print(Item.all)


''' 
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
'''
