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

registry = []

def register(func):
    print(f'Running register({func})')
    registry.append(func)
    return func

@register
def f1():
    print('Running f1()')

@register
def f2():
    print('Running f2()')

def f3():
    print('Running f3()')

def main():
    print('Running main()')
    print('Registry ->', registry)
    f1()
    f2()
    f3()

main()

