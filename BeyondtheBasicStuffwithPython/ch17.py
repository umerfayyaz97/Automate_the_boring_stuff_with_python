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

    #class attribute
    book_count = 0

    def __init__(self, title:str, author:str, page:int):
        self.title = title
        self.author = author
        self.page = page

        Book.book_count +=1

        self.id  = Book.book_count
    
    def __str__(self):
        """Returns a user friendly string representation"""
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        """Returns length of book"""
        return self.page

    def __repr__(self):
        return f"Object of Book with id {self.id}"

    
my_book = Book('ATBSWP', 'Umer', 100)
my_book_2 = Book('ATBSWP', 'Umer', 100)

# print(repr(my_book))
# print(repr(my_book_2))

# print(my_book)
# print(f'{len(my_book)} ')

class MesssageList:
    def __init__(self, message_data):
        self._messages = message_data

    def __getitem__(self, position):
        return self._messages[position]
    
    def __iter__(self):
        for msg in self._messages:
            yield msg
    
api_response_data = [
    {'role': 'assistant', 'content': 'Hello! How can I help?'},
    {'role': 'user', 'content': 'What is the capital of Pakistan?'}
]

messages_list = MesssageList(api_response_data)

first_message = messages_list[0]
print(f"First message is from {first_message['role']}")

for message in messages_list:
    print(f" Role :{message['role']}, content : {message['content']} ")
