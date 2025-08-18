statement = 'It is a bright day to go outside'
count= {}

for character in statement:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)