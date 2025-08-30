import re

# # paranthesis makes groups, acces them by 1 & 2
# phone_re = re.compile(r'(\d{3})-(\d{3}-\d{4})')
# mo = phone_re.search("My number is 455-444-1234")

# print(mo.group(2))


# no paranthesis makes them non group
phone_re = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_re.search("My number is 455-444-1234")

print(mo.group())
