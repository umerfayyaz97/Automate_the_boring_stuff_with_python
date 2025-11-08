# def deco(func):
#     def inner():
#         print('Running inner()')
#     return inner

# @deco
# def target():
#     print('Running target()')

# target = deco(target)


# target()

# print(target)

# ------------------------------------

# registry = []

# def register(func):
#     print(f'Running register({func})')
#     registry.append(func)
#     return func

# @register
# def f1():
#     print('Running f1()')

# @register
# def f2():
#     print('Running f2()')

# def f3():
#     print('Running f3()')

# def main():
#     print('Running main()')
#     print('Registry ->', registry)
#     f1()
#     f2()
#     f3()

# main()

# ------------------------------------

def add_five(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 5
    return wrapper

@add_five
def sum_two_numbers(a,b):
    return a+b

result = sum_two_numbers(10,15)
print(result)

@add_five
def add_zero(num):
    return num

result2 = add_zero(10)
print(result2)