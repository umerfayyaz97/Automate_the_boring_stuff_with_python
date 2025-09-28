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
 