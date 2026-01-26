# Project 1: 
# Description:
# Code: 
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# Project 1: 
# Description: Write a Python program to print "Hello Python".
# Code: 

# print("Hello Python")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Project 2: 
# Description: Write a Python program to do arithmetical operations addition and division.
# Code: 
# Addition:
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# sum = n1 + n2
# print(f"The sum of {n1} and {n2} is : {sum}")

# Division:
# n3 = float(input("Enter the numerator: "))
# n4 = float(input("Enter the denominator: "))
# if n4 == 0:
#     print("Division by zero is not allowed")
# else:
#     div = n3/n4
#     print(f"The division of {n3} by {n4} is : {div}")


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Project 3: 
# Description: Write a Python program to find the area of a triangle.
# Code: 

# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# area = 0.5*base*height
# print(f"The area of the triangle with base {base} and height {height} is : {area:.2f} sq units")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Project 4: 
# Description: Write a Python program to swap two variables.
# Code: 

# a = float(input("The value the first variable a = "))
# b = float(input("The value the second variable b = "))
# print(f"The original values of 'a' and 'b' are : a={a}, b={b}") # Display the original values
# temp = a
# a = b
# b = temp
# or
# a , b = b , a # for clear readibility
# print(f"The swapped values or 'a' and 'b' are : a={a}, b={b}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 5: 
# Description: Write a Python program to generate a random number
# Code:

# import random
# print(f"Random NUmber is : {random.randint(1,100)}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 6: 
# Description: Write a Python program to convert kilometers to miles
# Code: 

# km = float(input("Enter the distance in km : "))
# factor = 0.62
# miles = km * factor
# print(f"{km} km is equal to {miles : .2f} miles")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 7: 
# Description: Write a Python program to convert Celsius to Fahrenheit
# Code: 

# celcius = float(input("Enter the temp in celcius: "))
# fahreneit = (celcius * 9/5) + 32
# print(f"{celcius} celcius is equal to {fahreneit: .2f} fahreneit")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 8: 
# Description: Write a Python program to display calendar.
# Code: 

# import calendar
# Year = int(input("Enter the Year: "))
# Month = int(input("Enter the Month: "))

# cal = calendar.month(Year, Month)
# print(cal)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 9: 
# Description: Write a Python program to solve quadratic equation.
# Code: 

# import math

# a = float(input("Enter the coefficient of a: "))
# b = float(input("Enter the coefficient of b: "))
# c = float(input("Enter the coefficient of c: "))

# discriminant = b**2 - 4*a*c

# if discriminant > 0:
#     # 2 real and distinct roots
#     root1 = (-b + math.sqrt(discriminant)) / 2*a
#     root2 = (-b - math.sqrt(discriminant)) / 2*a
#     print(f"Root 1 : {root1}")
#     print(f"Root 2 : {root2}")

# elif discriminant == 0:
#     # One real root
#     real_root = -b/2*a

# else: 
#     # Complex Roots
#     real_part = -b/2*a
#     imagenary_part = math.sqrt(abs(discriminant))/2*a
#     print(f"Root 1: {real_part:.2f} + {imagenary_part:.2f}i")
#     print(f"Root 2: {real_part:.2f} - {imagenary_part:.2f}i")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 10: 
# Description: Write a Python program to swap two variables without temp variable.
# Code: 

# a = input("Enter a: ")
# b = input("Enter b: ")
# # swaping without a temporary variable
# a, b = b, a
# print("After Swaping: ")
# print("a =", a)
# print("b =", b)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 11: 
# Description: Write a Python Program to Check if a Number is Positive, Negative or Zero.
# Code:

# n = int(input("Enter the number: "))

# if n > 0:
#     print(f"{n} is a positive number")
# elif n == 0:
#     print(f"{n} is zero")
# else:
#     print(f"{n} is a negative number")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 12: 
# Description: Write a Python Program to Check if a Number is even or odd.
# Code:

# n = int(input("Enter the number: "))
# if n % 2 == 0:
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 13: 
# Description: Write a Python Program to Check Leap Year.
# Code:

# year = int(input("Enter the year: ")) # century year divided by 400 is leap year
# if (year % 400 == 0) and (year % 100 == 0): # divided by 100 means century year (ending with 00)
#     print(f"{year} is a leap year")
# elif (year % 4 == 0) and (year % 100 != 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year") # if not divided by both 400 (century year) and 4 (not century year), year is not leap year
                                        
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 14: 
# Description: Write a Python Program to Check a prime number.
# Code:

# n = int(input("Enter the number: "))
# flag = False
# if n <= 1:
#     print("Not a prime number")
# elif n > 1:
#     for i in range(2,n):
#         if n % i == 0:
#             flag = True
#             break
# if flag:
#     print(f"{n} is not a prime number")
# else:
#     print(f"{n} is a prime number")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 15: 
# Description: Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
# Code:

# lower = 1
# upper = 10
# print(f"The Prime Numbers between {lower} and {upper} are:")
# for number in range(lower, upper+1):
#     if number > 1:
#         for i in range (2, number):
#             if number % i == 0:
#                 break
#         else:
#             print(number)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 16: 
# Description: WWrite a Python Program to Find the Factorial of a Number.
# Code: 

# n = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(f"The factorial of {n} is : {factorial}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 17: 
# Description: Write a Python Program to Display the multiplication Table.
# Code: 

# n = int(input("Enter the number: "))
# for i in range(1,11):
#     x =  n*i
#     print(f"The table of {n} is = {n} * {i} = {x}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 18: 

# Description: Write a Python Program to Print the Fibonacci sequence

# Code: 
# terms = int(input("How many terms: "))
# n1 = 0
# n2 = 1
# count = 0 
# if terms < 0:
#     print("Enter the valid number of terms")
# elif terms == 1:
#     print(f"The Fibonacci sequence upto {terms}: {n1}")
# else:
#     print("Fibonacci Sequence:")
#     while count < terms:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 19: 
# Description: Write a Python Program to Check Armstrong Number
# Code:

# n = int(input("Enter the number: "))
# power = len(str(n))
# sum = 0
# temporary_number = n

# while temporary_number > 0:
#     digit = temporary_number % 10
#     sum = sum + digit**power
#     temporary_number //= 10

# if sum == n:
#     print(f"The number {n} is an Armstrong Number")
# else:
#     print(f"The number {n} is not an Armstrong Number")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 20: 
# Description: Write a Python Program to Find Armstrong Number in an Interval.
# Code:

# lower = int(input("Enter the lower limit number: "))
# upper = int(input("Enter the upper limit number: "))

# for n in range(lower, upper+1):
#     power = len(str(n))
#     temporary_number = n
#     sum = 0

#     while temporary_number > 0:
#         digit = temporary_number % 10
#         sum += digit**power
#         temporary_number //= 10

#     if sum == n:
#         print(n)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 21: 
# Description: Write a Python Program to Find the Sum of Natural Numbers.
# Code:

# limit = int(input("Enter the limit upto which the sum is required: "))
# sum = 0
# for i in range(1, limit+1):
#     sum = sum + i
# print(f"The sum of first {limit} natural numbers : {sum}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 22: 
# Description: Write a Python Program to Find LCM.
# Code:

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# max_num = max(a, b)

# while True:
#     if (max_num % a == 0) and (max_num % b == 0):
#         print(f"The LCM of {a} and {b} is {max_num}")
#         break
#     max_num += 1

# OR
# import math
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# lcm = abs(a*b) // math.gcd(a,b)
# print(f"The LCM of {a} and {b} is {lcm}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 23: 
# Description: Write a Python Program to Find LCM.
# Code: 

# import math
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# hcf = math.gcd(a,b)
# print(hcf)

# OR

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# hcf = 1
# for i in range(1, min(a,b)+1):
#     if a % i == 0 and b % i == 0:
#         hcf = i
# print(f"The HCF of {a} and {b} is {hcf}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 24: 
# Description: Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.
# Code: 

# decimal_number = int(input("Enter the decimal number: "))
# print(f"The decimal value of {decimal_number} is: ")
# print(bin(decimal_number), "in binary")
# print(oct(decimal_number), "in oct")
# print(hex(decimal_number), "in hexadecimal")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 25: 
# Description: Write a Python Program To Find ASCII value of a character.
# Code: 

# character = input("Enter the Character: ")
# print(f"The ASCII value of {character} is {ord(character)}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 26: 
# Description: WWrite a Python Program to Make a Simple Calculator with 4 basic mathematical operations.
# Code: 

# def calculator():
#     while True:
#         try:
#             user_input = input('''
# Menu:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Quit
# ''')
#             if user_input == "1":
#                 print("Add")
#                 x = int(input("Enter the value of x : "))
#                 y = int(input("Enter the value of y : "))
#                 print(f"The addition of {x} and {y} : {x+y}")
#                 # print(x+y)

                
#             elif user_input == "2":
#                 print("Subtraction")
#                 x = int(input("Enter the value of x : "))
#                 y = int(input("Enter the value of y : "))
#                 print(f"The subtraction of {x} and {y} : ")
#                 if x>y:
#                     print(f"The subtraction of {x} and {y} : {x-y}")
#                 else:
#                     print(f"The subtraction of {x} and {y} : {y-x} ")

#             elif user_input == "3":
#                 print("Multiply")
#                 x = int(input("Enter the value of x : "))
#                 y = int(input("Enter the value of y : "))
#                 print(f"The multiplication of {x} and {y} : {x*y}")
#                 # print(x*y)

            
#             elif user_input == "4":
#                 print("Divide")
#                 x = int(input("Enter the value of x : "))
#                 y = int(input("Enter the value of y : "))
#                 if y == 0:
#                     raise ZeroDivisionError("Can not divide by zero")
#                 else:
#                     print(f"The division of {x} and {y} : {x/y : .2f} ")
#                     # print(x/y)

#             elif user_input == "5":
#                 print("Calculator Turned Off")
#                 break
#             else:
#                 print("Invalid input, Enter from the given choices")

#         except ZeroDivisionError as e:
#             print("Error:", e)
#             print("Please try again")

#         # except ValueError:
#         #     print("Error, Please enter the valid integer")

# calculator()

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 27: 

# Description: Write a Python Program to Display Fibonacci Sequence Using Recursion.

# Code: 

# def recursive_fib_sequence(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return recursive_fib_sequence(n - 1) + recursive_fib_sequence(n - 2)
    
# terms = int(input("Enter the number of terms (Greater than 0) : "))

# if terms <= 0:
#     print("Enter the valid number")
# else:
#     print("Fibonacci Sequence: ")
#     for i in range(terms):
#         print(recursive_fib_sequence(i))

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 28: 

# Description: Write a Python Program to Find Factorial of Number Using Recursion

# Code: 

# def recurrinng_factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * recurrinng_factorial(n-1)

# n = int(input("Enter the number : "))

# if n < 0:
#     print("Factorial does not exist for Negative Numbers")
# elif n == 0 :
#     print("The factorial of 0 is 1")
# else:
#     print(f"The factorial of {n} is {recurrinng_factorial(n)}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 29: 

# Description: Write a Python Program to calculate your Body Mass Index.

# Code: 

# def bodymassindex(weight, height):
#     return round((weight/height**2),2)

# weight = float(input("Please Enter your weight in kg: "))
# height = float(input("Please Enter your height in mtr: "))

# bmi = bodymassindex(weight, height)
# print(f"Your BMI is {bmi}")

# if bmi <= 18:
#     print("You are underweight")
# elif 18 < bmi <= 24.9:
#     print("Your weight is normal")
# elif 25 < bmi <= 50:
#     print("You are overweight")
# else:
#     print("You are obese")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 30: 

# Description: Write a Python Program to calculate the natural logarithm of any number.

# Code: 

# import math
# n = int(input("Enter a number : "))
# if n <= 0:
#     print("Please enter the valid number")
# else:
#     result = math.log(n)
#     print(f"The Logarithmic Nummber of {n} is : {result : .2f}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 31: 

# Description: Write a Python Program for cube sum of first n natural numbers?

# Code: 

# def cube_sum_of_natural_numbers(n):

#     total = 0
#     expression = []

#     if n <= 0:
#         print("Please enter the number bigger than 0")

#     for i in range(1, n+1):
#         total += i**3
#         expression.append(f"{i}³")

#     print(f"{'+'.join(expression)} = {total}")
    
# n = int(input("Enter the number for cube: "))
# cube_sum_of_natural_numbers(n)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 32: 

# Description: Write a Python Program to find sum of array.

# Code: 

# arr = [1,2,3,4,5,6,7,8,9]
# result = sum(arr)
# print(result)

# OR....................................................

# def sum_of_array(array):
#     total = 0
#     for elements in array:
#         total += elements
#     return total
# array = [1,2,3,4,5,6,7,8,9]
# result = sum_of_array(array)
# print(result)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 33: 

# Description: Write a Python Program to find largest element in an array.

# Code: 

# def find_largest_element(arr):
#     if not arr:
#         return "Erray is empty"
    
#     largest_element = arr[0]

#     for element in arr:
#         if element > largest_element:
#             largest_element = element

#     return largest_element
# arr = [2,5,3,8,9,6,7]
# result = find_largest_element(arr)
# print(f"The largest element in the array is : {result}")

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Project 34: 

# Description: Write a Python Program for array rotation.

# # Code: 

# def array_rotation(arr, displacement):
#     print(f"The length of array is : {len(arr)}")
#     length_of_array = len(arr)
#     if displacement < 0 or displacement >= length_of_array:
#         print(f"{displacement} is an Invalid Rotation Value")
#         return arr

#     rotated_array = [0] * length_of_array

#     for i in range(length_of_array):
#         rotated_array[i] = arr[(i+displacement) % length_of_array]
#     return rotated_array

# arr = [1,2,3,4,5,6,7]
# displacement = 2
# result = array_rotation(arr, displacement)
# print(f"When displacement is {displacement}: The original array {arr} becomes {result}")

