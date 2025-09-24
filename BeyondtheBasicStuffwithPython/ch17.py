# class Product:
#     def __init__(self, price:float):
#         self._price = price

#     @property
#     def price(self):
#         print("Getter: Reading price")
#         return self._price
    
#     @price.setter
#     def price(self, new_price: float):
#         print("Setter: setting new value")
#         if new_price >=0:
#             self._price = new_price
#         else:
#             print("Price cannot be negative")

#     @price.deleter
#     def price(self):
#         print("Deleter")
#         self._price = 0

# book = Product(15)

# print(f"Current price: {book.price}")
# book.price = 12
# print(f"After Updating: {book.price}")
# del book.price
# print(f"After deleting: {book.price}")

# --------------------------------------------------------

# import datetime

# newyear = datetime.date(2021,1,1)
# print(repr(newyear))
# print(type(repr(newyear)))


# print(str(newyear))
# print(type(str(newyear)))

# print(newyear)
# print(type(newyear))


# ----------------------------------------------------------
# Dunder methods

class Book:
    def __init__(self, title:str, author:str, page:int):
        self.title = title
        self.author = author
        self.page = page
    
    def __str__(self):
        """Returns a user friendly string representation"""
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        """Returns length of book"""
        return self.page

    
my_book = Book('ATBSWP', 'Umer', 100)

print(my_book)
print(f'{len(my_book)} ')

