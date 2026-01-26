# i = 1 # initialize counter
# while i <= 10: # loop from 1 to 10
#     print(3*i) # prints the multiplication table of 3
#     i += 1 # increment counter

# number = int(input("Enter a number to print its multiplication table: "))
# i = 1
# while i <= 10:
#     print(number*i)
#     i += 1
# print("Multiplication table completed.")

# n = int(input("Enter a number to print its multiplication table: "))
# for _ in range(1, 11):
#     print(n*_) # prints the multiplication table of the given number


# t = 0 # initialize counter
# while t <= 5: # loop from 0 to 5
#     print ("Hello Rishabh")
#     t += 1 # increment counter
# print("Done")

# m = 5 # initialize counter
# while m >= 1: # loop from 5 to 1
#     print(2**m) # prints powers of 2 from 2^5 to 2^1
#     m -= 1 # decrement counter
# print("Finished")

# j = 1
# while j <= 10: # loop from 1 to 10
#     print(j*j) # prints squares of numbers from 1 to 10
#     j += 1
# print("Completed")

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(num): # loop through the list
#     print(num[i])
#     i += 1
# print("All numbers printed.")

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) # Finding a certain number in a tuple
# a = 64
# i = 0
# while i < len(num):
#     if num[i] == a: # check if the current element matches 'a'
#         print(f"Found the number {a} at index {i}.")
#         break
#     i += 1

# i = 0 # initialize counter
# while i <= 10:
#     if i == 3: # skip printing 3
#         i += 1
#         continue # skip the rest of the loop and go to the next iteration
#     if i == 6: # skip printing 6
#         i += 1
#         continue # skip the rest of the loop and go to the next iteration
#     if i == 8:
#         i += 1 # skip printing 8
#         break
#     print(i)
#     i += 1

# i = 0
# while i <= 15:
#     if (i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# a = 81
# for elements in num:
#     print(elements)
#     # print(elements**0.5)
#     # print(elements.is_integer()) # Check if the square root is an integer
#     # print(elements%2 == 0) # Check if the number is even
#     # print(elements%2 != 0) # Check if the number is odd
#     # print(elements.as_integer_ratio()) # Get the integer ratio of the number
#     if elements == a:
#         print(f"Found the number {a} in the list.")
#         break

# Measure some strings:
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, "->", len(w))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Code that modifies a collection while iterating over that same collection can be tricky to get right. 
#Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection. See Below examples:

# A dictionary of users and their statuses
# users = {'Rohit': 'active', 'Rishabh': 'inactive', 'Aman': 'active', 'Sonia': 'inactive', 'Priya': 'active'} 
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)
#...................................................OR....................................................
# active_users = {}
# users = {'Rohit': 'active', 'Rishabh': 'inactive', 'Aman': 'active', 'Sonia': 'inactive', 'Priya': 'active'} 
# for  status in users.items():
#     if status == 'active':
#         active_users[users] = status
# print(active_users)

# a = ['mars', 'saturn', 'venus', 'jupiter', 'earth', 'mercury', 'neptune', 'uranus']
# for planets in range(len(a)): # loop through indices of the list
#     print(planets, a[planets]) # print index and corresponding planet
#...................................................OR....................................................
# for index, planet in enumerate(a): # loop through list with index
#     print(index, planet) # print index and corresponding planet

# sum(range(1, 11)) # sum of numbers from 1 to 10
# print(sum(range(1, 11)))

# for i in range(2, 10):
    # for j in range(2, i):
    #     if i % j == 0:
    #         print(f"{i} is equal to {j} * {i//j}") # not a prime number, 4 is equal to 2 * 2
    #         break

    # if i % 2 == 0:
    #     print(f"{i} is an even number.")
    #     continue
    # print(f"{i} is an odd number.")

    # for j in range(2, i): # check for factors from 2 to i-1
    #     if i % j == 0:
    #         print(f"{i} is equal to {j} * {i//j}")
    #         break
    # else:
    #     print(f"{i} is a prime number.") # loop fell through without finding a factor

# num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# print(list(map(lambda x: x**2, num))) # prints the squares of each number in the list using map and lambda function
# for _ in num:
#     print(_**2) # prints the squares of each number in the list using a for loop

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# a = int(input("Enter a number to search in the list: "))
# idx = 0
# for el in num:
#     if el == a:
#         print(f"Found the number {a} at index {idx}.")
#         break
#     idx += 1
# else:
#     print(f"The number {a} is not found in the list.")

# n = int(input("Enter a number to print: "))
# count = 0
# for _ in "x" * n: # loop n times
#     count += 1
#     print(count)

# for _ in range(10): # range(8 stops)
#     print(_)

# for _ in range(2, 10): # range(start, stops)
#     print(_)

# for _ in range(0, 10, 2): # range(start, stops, step)
#     print(_)

# for _ in range(10, 0, -1): # range(start, stops, step)
#     print(_) # prints numbers from 10 to 1 in reverse order

# for _ in range(1, 11):
#     print(3*_) # prints the multiplication table of 3

# for _ in range(1, 11):
#     print(_**2) # prints squares of numbers from 1 to 10

# for _ in range(2, 22, 2):
#     print(_) # prints even numbers from 2 to 20

# for _ in range(1, 21, 2):
#     print(_) # prints odd numbers from 1 to 20

# n = int(input("Enter a number: "))
# sum = 0
# for _ in range(1, n+1): # loop from 1 to n
#     sum += _ # accumulate the sum
# print(f"The sum of numbers from 1 to {n} is {sum}.")

# n = int(input("Enter a number: "))
# factorial = 1
# for _ in range(1, n+1): # loop from 1 to n
#     factorial *= _ # accumulate the product
# print(f"The factorial of {n} is {factorial}.")

# n = int(input("Enter a number:"))
# sum = 0
# i = 0
# while i <= n:
#     sum += i
#     i += 1
# print(f"The sum of numbers from 0 to {n} is {sum}.")

# Calculate factorial using while loop...........................................................

# n = int(input("Enter a number:"))
# factorial = 1 # initialize factorial
# i = 1 # initialize counter
# while i <= n: # loop from 0 to n
#     factorial *= i # accumulate the product
#     i += 1 # increment counter
# print(f"The factorial of {n} is {factorial}.")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

n = int(input("Enter a number: "))
factorial = 1
for _ in range(1, n+1):
    factorial *= _ # accumulate the product
print(f"The factorial of {n} is {factorial}.")