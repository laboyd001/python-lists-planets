# using the 'random' module and the 'range' method, generate a list of 20 random numbers between 0 and 49

import random

random_numbers = []

# for num in range(21):
#     random.randrange(0,100)
#     random_numbers.append(num)

# print("#1")
# print("random numbers:",random_numbers)

for num in range (0, 21):
    random_numbers.append(random.randrange(0,49))

print("#1 Here's a list of random numbers:")
print(random_numbers)

# with the resulting list, use a list comprehension to build a new list that contains each number squared.  For example, if the original list is [2, 5], the final list will be [4,25]
print("\n#2 Here's the list of numbers with each number squared:")

rand_num_squared = [num**2 for num in random_numbers]
print(rand_num_squared)