#Finding duplicate using set (hashing)

def has_duplicate(nums):

    #creates a set of unique values (set)
    seen = set()   

    for num in nums:
        if num in seen:
            print(f"Found {num} ")
            return True
        seen.add(num)
    return False

#lists
# print(f"Fast way with [1, 2, 3, 1]: {has_duplicate([1, 2, 3, 1])}")
# print(f"Fast way with [1, 2, 3, 4]: {has_duplicate([1, 2, 3, 4])}")

#string
# print(has_duplicate("SSTRINGsss"))

#dictionaries
print(has_duplicate({'key1': 'value1', 'key2': 'value2', 'key3': 'value1'}.values()))