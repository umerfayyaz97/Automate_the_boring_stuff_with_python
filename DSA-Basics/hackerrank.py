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

# s,k = input().split()

# print(sorted(s))
# per = permutations(sorted(s), int(k))

# for p in per:
#     print(p)
#     print("".join(p))

# per = permutations([1,2])

# for p in per:
#     s = map(str, p)
#     print("".join(s))
    

# x=1
# y=1
# z=2
# n=3
    
# print([ [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n ])

# n = int(input())

# arr = map(int, input().split())

# unique_list = sorted(set(arr))

# print(unique_list[-2])



# a = [[a,b] for a in range(3)  for b in range(3)]
# print(a)

records = [[5,'Harry'],[37.21,'Berry'],[37.21,'Tina'],[37.2,'Akriti'],[41,'Harsh']]

scores = [record[0] for record in records ]

# print(scores)
unique = set(scores)
sorted_values = sorted(unique)

second_lowest = sorted_values[1]
print(second_lowest)


runner_ups = []
for item in records:
    if item[0] == second_lowest:
        runner_ups.append(item[1])

runner_ups.sort()

for name in runner_ups:
    print(name)