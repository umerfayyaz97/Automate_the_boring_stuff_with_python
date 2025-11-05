# def factorial(n):
#     """returns n!"""
#     return 1 if n <2 else n * factorial(n-1)

# print(factorial(8))
# print(factorial.__doc__)
# help(factorial)

# fact = factorial
# print(fact(5))

# m = map(factorial, range(11))
# print(list(m))
# print(m)
# -----------------------------------------

# sorting a lost of words by length

# fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
# fruits_sorted = sorted(fruits, key=len)
# print(fruits_sorted)

# def reverse(word):
#     return word[::-1]

# fruits_reversed = sorted(fruits, key=reverse)
# print(fruits_reversed)
# ---------------------------------------
# functools and operator

# from functools import partial

# def my_fn(base, exponent):
#     return base ** exponent

# #we freeze the exponent to two instead of passing everytime

# square = partial(my_fn, exponent = 2)

# print(f' using the original fn: {my_fn(10,2)}')
# print(f' using the partial fn: {square(10,3)}')

# -------------------------------------------
# metro_data = [
#  ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#  ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#  ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#  ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#  ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
#  ]

# from operator import itemgetter
# for city in sorted(metro_data, key = itemgetter(2)):
#     print(city)

# ------------------------------------------------
# named tuples
 
# from collections import namedtuple

# Student = namedtuple("Student", ['name', 'age', 'major'])

# s1 = Student('Ali', '21', 'Math')

# print(s1)

# -------------------------------------------------
# getattr (works on objects with named attr, named tuples and classes)

# from collections import namedtuple

# metro_data = [
#  ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#  ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#  ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#  ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#  ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
#  ]

# Metropolis = namedtuple('Metropolis',['name', 'cc', 'pop', 'coords'])

# metro_objects = [Metropolis(*data) for data in metro_data ]

# # print(metro_objects)
# # print(type(metro_objects))

# from operator import attrgetter

# for city in sorted(metro_objects, key=attrgetter('pop')):
#     print(city)

# -------------------------------------------------------------


# fluent python

