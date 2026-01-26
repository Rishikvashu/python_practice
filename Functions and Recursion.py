# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# n = int(input("Enter a number: "))
# result = factorial(n)
# print(f"The factorial of {n} is {result}.")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# def cal_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum
# cal_sum(3, 5)
# cal_sum(10, 20)
# cal_sum(-1, 1)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# def calculate_average(n):
#     sum = 0
#     average = 0
#     for _ in range(1, n+1): # loop from 1 to n
#         sum += _ # accumulate the sum
#     if n > 0:
#         average = sum / n
#     else:
#         average = 0
#     return average
# n = int(input("Enter a number: "))
# average = calculate_average(n)
# print(f"The average of numbers from 1 to {n} is {average}.")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# cities = ["Agra", "Mumbai", "Chennai", "Pune", "Delhi", "Kolkata", "Bangalore"]
# cars = ["BMW", "Audi", "Toyota", "Honda", "Ford", "Chevrolet"]
# def list_length(list):
#     print(len(list))
#     return len(list)
# list_length(cities)
# list_length(cars)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# cities = ["Agra", "Mumbai", "Chennai", "Pune", "Delhi", "Kolkata", "Bangalore"]
# def print_list(list):
#     for i in list:
#         print(i, ",", end=" ")
# print_list(cities)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# n = int(input("Enter a number: "))
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# result = factorial(n)
# print(f"The factorial of {n} is {result}.")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact
# n = int(input("Enter a number: "))
# result = factorial(n)
# print(f"The factorial of {n} is {result}.")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# def rate_conversion(usd):
#     inr = usd * 90
#     return inr
# usd = float(input("Enter the amunt in USD: "))
# rs = rate_conversion(usd)
# print(f"The amount in INR is {rs} rupees.")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# def even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# n = int(input("Enter a number: "))
# result = even_odd(n)
# print(f"The number {n} is an {result} number .")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^RECURSION ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Writing a recursive function to calculate the sum of first n natural numbers

# def calculate_sum(n):
#     if n ==0 or n == 1:
#         return n
#     return calculate_sum(n-1) + n # recursive call
# n = int(input("Enter a number: "))
# result = calculate_sum(n)
# print(f"The sum of the first {n} natural numbers is {result}.")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Writing a function to print the elements of a list using recursion

def print_list(list, index): # recursive function
    if index >= len(list): # base case
        return
    print(list[index]) # print current element
    
    print_list(list, index + 1) # recursive call
cities = ["Agra", "Mumbai", "Chennai", "Pune", "Delhi", "Kolkata", "Bangalore"]
print_list(cities, 0)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^