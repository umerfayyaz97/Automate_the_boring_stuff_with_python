class Product:
    def __init__(self, price:float):
        self._price = price

    @property
    def price(self):
        print("Getter: Reading price")
        return self._price
    
    @price.setter
    def price(self, new_price: float):
        print("Setter: setting new value")
        if new_price >=0:
            self._price = new_price
        else:
            print("Price cannot be negative")

    @price.deleter
    def price(self):
        print("Deleter")
        self._price = 0

book = Product(15)

print(f"Current price: {book.price}")
book.price = 12
print(f"After Updating: {book.price}")
del book.price
print(f"After deleting: {book.price}")