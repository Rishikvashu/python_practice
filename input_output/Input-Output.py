# status = 'Completed'
# year = 2024
# print(f'Result: {status}, Year: {year}')




# f = open("A:/Python/input_output/demo.txt", "r") # read mode
# data = f.read()
# print(data)
# f.close()

# f = open("A:/Python/input_output/demo.txt", "w") # write mode
# f.write("This is a new line.")
# f.close()

# f = open("A:/Python/input_output/demo.txt", "a") # append mode
# f.write("\nThis line is appended.")
# f.close()

# f = open("A:/Python/input_output/demo.txt", "r+") # read and write mode
# data = f.write("abc")
# print(data)
# f.close()

# with open("A:/Python/input_output/demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("A:/Python/input_output/demo.txt", "w") as f:
#     data = f.write("After writing , the previous content is removed.\nThis is the new content.")
#     # print(data)

import os
from re import search
# file_path = "A:/Python/input_output/demo.txt" 
# if os.path.exists(file_path): # check if file exists
#     with open(file_path, "r") as f: # read mode
#         data = f.read()
#         print(data)
# else:
#     print("File does not exist.")

# os.remove("A:/Python/input_output/demo.txt") # delete the file

# with open("practice.txt", "w") as f: # create and write to a new file
#     f.close() 

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# The following code reads the content of 'practice.txt', replaces all occurrences of 'java' with 'python', 
# and writes the modified content back to the file. 
# This needs to be done carefully and in the right order to avoid data loss.

# with open("practice.txt", "r") as f: # read the original data
#     data = f.read() 
#     print(data)

# new_data = data.replace("python3", "python") # replace 'java' with 'python'

# with open("practice.txt", "w") as f: # write the modified data back to the file
#     f.write(new_data)
# print(new_data)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# The following code searches for a specific word in 'practice.txt' and reports whether it was found.
# def check_word_in_file():
#     search = input("Enter the word to be searched: ")
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if data.find(search) != -1: # or use 'if search in data:'
#             print(f"The word '{search}' is found in the file.")
#         else:
#             print(f"The word '{search}' is not found in the file.")
# check_word_in_file()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# The following code searches for a specific word in line using for loop 'practice.txt' and reports whether it was found.

# def check_word_in_file():
#     search = input("Enter the word to be searched: ")
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         for line in f:
#             if search in line:
#                 print(f"The word '{search}' is found in line {line_no}: {line.strip()}")
#                 data = False
#             line_no += 1
#     if data:
#         print(f"The word '{search}' is not found in the file.")
# check_word_in_file()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# The following code searches for a specific word in line using while loop 'practice.txt' and reports whether it was found.

# def check_word_in_file():
#     search = input("Enter the word to be searched: ")
#     line_no = 1
#     found = False # flag to track if word is found

#     with open("practice.txt", "r") as f:
#         for line in f:
#             if search in line:
#                 print(f"The word '{search}' is found in line {line_no}: {line.strip()}")
#                 found = True
#             line_no += 1
#     if not found:
#         print(f"The word '{search}' was not found in the file.")
# check_word_in_file()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# The following code appends numbers from 1 to 10 to 'practice.txt'.

# with open("practice.txt", "w") as f:
#     f.write("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
#     print("Numbers appended to the file.")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# The following code reads numbers from 'practice.txt', identifies even numbers, prints them, and counts how many there are.

# count = 0
# with open("practice.txt", "r") as f:
#     data = f.read()

#     num = data.split(", ") # splitting the numbers based on comma and space
#     for i in num: # iterating through the list of numbers
#         if int(i) % 2 == 0:
#             # print("Even number found:")
#             print(int(i))
#             count += 1
#              # checking if the number is even # printing the even number
# print(f"The count of even numbers in the file is: {count}")
