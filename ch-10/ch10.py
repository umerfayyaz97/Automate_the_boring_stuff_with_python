from pathlib import Path

#joining paths
# path = Path('spam' , 'eggs' ,'bacon')
# print(path)

#current path
# import os

# print("CWD")
# print(Path.cwd())

#home directory
# print(Path.home())


file = open('test1.txt', 'w', encoding='UTF-8')
file.write('Hello')
file.close()

opening = open('test1.txt', encoding='UTF-8')
content = opening.read()
print(content)
opening.close()