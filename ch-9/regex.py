import re

# paranthesis makes groups, acces them by 1 & 2
phone_re = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_re.search("My number is 455-444-1234")

print(mo.group())

#if you want to nreceive all groups in the form of tuple
# print(mo.groups())


# no paranthesis makes them non group
# phone_re = re.compile(r'\d{3}-\d{3}-\d{4}')
# mo = phone_re.search("My number is 455-444-1234")

# print(mo.group())


#findall returns a list of strings if there are no groups, finds first occurance only and doesnt overlap
phone_re = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_re.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

