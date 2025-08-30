import re

# paranthesis makes groups, acces them by 1 & 2
# phone_re = re.compile(r'(\d{3})-(\d{3}-\d{4})')
# mo = phone_re.search("My number is 455-444-1234")

# print(mo.group())

#if you want to nreceive all groups in the form of tuple
# print(mo.groups())


# no paranthesis makes them non group
# phone_re = re.compile(r'\d{3}-\d{3}-\d{4}')
# mo = phone_re.search("My number is 455-444-1234")

# print(mo.group())


#findall returns a list of strings if there are no groups, finds first occurance only and doesnt overlap
# phone_re = re.compile(r'\d{3}-\d{3}-\d{4}')
# mo = phone_re.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo)


#use [] brackets to include all items to look for (similar to a|E|e), ^ for negative.
# vowel_pattern = re.compile(r'[aeiouAEIOU]')
# mo = vowel_pattern.findall('RoboCop eats BABY FOOD')
# print(mo)

#negative with ^ character
# consonant_pattern = re.compile(r'[^aeiouAEIOU]')
# mo = consonant_pattern.findall('RoboCop eats BABY FOOD')
# print(mo) 


#verify BNB/USDT or usdt/bnb
# pair = re.compile(r'[a-zA-Z]+\/[a-zA-Z]+')
# mo = pair.findall('BNB/USDT')
# print(mo)

def is_valid_pair(pair):
    pattern = re.compile(r'^[A-Z]+\/[A-Z]+$')

    if pattern.fullmatch(pair):
        return True
    else:
        return False
    
print(f"'BNB/USDT': {is_valid_pair('BNB/USDT')}")   # Output: 'BNB/USDT': True
print(f"'USDT/BNB': {is_valid_pair('USDT/BNB')}")   # Output: 'USDT/BNB': True
print(f"'usdt/bnb': {is_valid_pair('usdt/bnb')}")   # Output: 'usdt/bnb': false