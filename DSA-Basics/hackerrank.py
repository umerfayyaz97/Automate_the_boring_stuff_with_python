# # Prompt the user to enter a number and convert it to an integer
# num = int(input("Enter a number: "))

# # Check if the number is even using the modulo operator
# if (num % 2) == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")

# n = int(input())
# list= []
    
# for i in range(n):
#     list.append(i)

# print(list)
        
# for i  in range(n):
#         print(i**2)
              
from itertools import permutations

# print(list(permutations(range(3),2)))

s,k = input().split()

print(sorted(s))
per = permutations(sorted(s), int(k))

for p in per:
    print(p)
    print("".join(p))