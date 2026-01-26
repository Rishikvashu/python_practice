# print("Hi")
# name = "Rishi"
# age = 21
# print(f"My name is {name} and I am {age} years old.")
# print("My name is", name + "and my age is", age)

f_string = 68
print(f"The value of the temperature is {(f_string-32)/1.8 : .2f} degree Celsius.")

f_string = 2000000
print(f"The value of the temperature is {(f_string-32)/1.8 :,.2f} degree Celsius.")



# marks = float(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade A")
# elif (90 > marks >= 80):
#     print("Grade B")
# elif (80 > marks >= 70):
#     print("Grade C")
# elif (70 > marks >= 60):
#     print("Grade D")
# else:
#     print("Grade F")


#Strings in Python #################################################################

# stmt = str("I am the best in this world")
# print(stmt.count("i"))
# print(stmt.lower().count("i"))
# print(stmt.find("best"))
# print(stmt.lower().count("t"))
# print(stmt.replace("world", "universe"))
# print(stmt.upper())
# print(len(stmt))

#Slicing .............................................................................................

# name = "Vashishtha"
# print(name[0:5]) # Vashi
# print(name[5:]) # shtha
# print(name[:5]) # Vashi
# print(name[-1]) # a
# print(name[-3:]) #tha
# print(name[::2]) #Vsihh
# print(name[::-1]) #ahthsihsaV
# print(name[1::2]) #ahsta
# print(name[-1::-2]) #atsha

# Even Odd Program #######################################################################################
# num1 = int(input("Enter the number: "))

# if num1 % 2 == 0:
#     print(f"{num1} is an Even number")
# else:
#     print(f"{num1} is an Odd number")
#.............................................................................................................
# num2 = int(input("Enter the number: "))

# if num2 % 7 == 0:
#     print(f"{num2} is divisible by 7")
# else:
#     print(f"{num2} is not divisible by 7")

#.............................................................................................................
# a = int(input("Enter first number a: "))
# b = int(input("Enter second number b: "))
# c = int(input("Enter third number c: "))

# if a >= b and a >= c:
#     print(f"{a} is the greatest number")
# elif b >= c:
#     print(f"{b} is the greatest number")
# else:
#     print(f"{c} is the greatest number")

# List in Python ########..Mutable..###################################################################

# mylist = [1, 2, 3, 4, 5]
# print(mylist)
# print(len(mylist))
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[-1])
# print(mylist[1:4])
# mylist.append(6) # add 6 at the end of the list
# print(mylist)
# mylist.remove(3) # remove 3 from the list
# print(mylist)
# mylist.insert(2, 10) # insert 10 at index 2
# print(mylist)
# mylist.sort(reverse=True) # reverse the list
# print(mylist)
# mylist.pop() # remove the last element
# print(mylist)
# mylist.pop(4) # remove element at index 4
# print(mylist)
# mylist.extend([7, 8, 9]) # extend the list by adding multiple elements
# print(mylist)
# mylist.append(2)
# mylist.append(1)
# mylist.append(3)
# print(mylist.sort()) # sort the list
# print(mylist)

# movies = []
# mov1 = input("Enter the name of first movie: ")
# mov2 = input("Enter the name of second movie: ")
# mov3 = input("Enter the name of third movie: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print("The Movies you entere are:", movies)
#....................................................OR.................................................
# movies = []
# for i in range(3):
#     mov = input(f"Enter the name of movie {i+1}: ")
#     movies.append(mov)
# print("The Movies you entered are:", movies)

#....................................................OR.................................................
# movies = [input(f"Enter the name of movie {i+1}: ") for i in range(3)]
# print("The Movies you entered are:", movies)

#....................................................OR.................................................
# movies = []
# i = 1
# while i <= 3:
#     mov = input(f"Enter the name of movie {i}: ")
#     movies.append(mov)
#     i += 1
# print("The Movies you entered are:", movies)

#....................................................OR.................................................
# movies = []
# movies.append(input("Enter the name of first movie: "))
# movies.append(input("Enter the name of second movie: "))
# movies.append(input("Enter the name of third movie: "))
# print("The Movies you entered are:", movies)

# list1 = [1, 2, 3, 2, 4]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if list1 == copy_list1:
#     print("The list is a palindrome")
# else:
#     print("The list  is not a palindrome")

# list1 = ["A", "B", "C", "D", "E", "A", "G", "A", "I", "A"]
# list1 = list(set(list1)) # remove duplicates by converting to set and back to list
# list1.sort()
# print("The sorted list is:", list1) 

# Another way to remove duplicates while preserving order...................................................
# unique_list = []
# for item in list1:
#     if item not in unique_list:
#         unique_list.append(item)
# print("List without duplicates:", unique_list)

# Another way to remove duplicates while preserving order....................................................
# list1 = ["A", "B", "C", "D", "E", "A", "G", "A", "I", "A"]
# list1 = list(dict.fromkeys(list1))
# print(list1)


# Tuple in Python ########..Immutable..###################################################################
# mytuple = (1, 2, 3, 4, 5)
# print(mytuple)
# mytuple.count(2)
# mytuple.index(4)
# print(mytuple.count(2)) # print the count of 2 in the tuple
# print("The index of 4 is:", mytuple.index(4)) # print the index of 4 in the tuple

# grades = ("A", "B", "C", "D", "E", "A", "G", "A", "I", "A")
# print("The count of A is:", grades.count("A"))


#........................DICTIONARIES IN PYTHON............Key-Value Pairs......................................
# my_dict = {
#     "name": "Rishi",
#     "age": 21,
#     "city": "New York",
#     "subjects": ["Math", "Science", "English"],
#     "grades" : ("A", "B", "A", "C")

# }
# print(my_dict)
# print(my_dict["name"]) # access the value of name
# print(my_dict["subjects"]) # access the list of subjects
# my_dict.pop("age") # remove age from the dictionary
# print(my_dict) 
# my_dict["age"] = 22 # update the age
# print(my_dict)
# my_dict["name"] = "Rishi Kumar" # update the name
# print(my_dict)
# print(list(my_dict.keys())) # print all the keys
# pairs = list(my_dict.items())# get all key-value pairs
# print(pairs[0:2]) # print first two key-value pairs
# print(list(my_dict.items())[:2]) # print first two key-value pairs
# print(len(my_dict)) # print the length of the dictionary


# null_dict = {}
# num = int(input("Enter the number of key-value pairs you want to add: "))
# for i in range(num):
#     key = str(input(f"Enter key {i+1}: "))
#     value = int(input(f"Enter value for key {key}: "))
#     null_dict[key] = value  
# print("The dictionary you created is:", null_dict)

# student= {} #empty dictionary for students and their subjects
# number_of_students = int(input("Enter number of students: ")) #number of students
# for i in range(n): #for each student
#     student_name= str(input("Enter the name of the student: ")) #student name
#     subject = {} #empty dictionary for subjects and marks
#     number_of_subjects = int(input(f"Enter number of subjects for {student_name}: ")) #number of subjects for the student
#     for j in range(number_of_subjects): #for each subject
#         subject_name = str(input(f"Enter subject name for {student_name}: ")) #subject name
#         marks = int(input(f"Enter marks for {subject_name} for {student_name}: ")) #marks for the subject
#         subject[subject_name] = marks #add subject and marks to the subject dictionary
#     student[student_name] = subject #add student and their subjects to the student dictionary
# print("The dictionary you created is:", student) #print the student dictionary










# ............................Set in Python ########..Mutable..No Duplicates..Unordered..################################
# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(2)
# myset.add(3)
# print(myset) # {1, 2, 3}
# myset.remove(2)
# print(myset) # remove 2 from the set
# myset.add("RishiKumar")
# myset.add((4, 5, 6))
# myset.add(2)
# print(myset)
# myset.clear()
# print(myset) # clear the set
# myset.add(1)
# myset.add(2)
# myset.add(2)
# myset.add(3)
# print(myset) # {1, 2, 3}
# # myset.remove(2)
# # print(myset) # remove 2 from the set
# myset.add("RishiKumar")
# myset.add((4, 5, 6))
# myset.add(2)
# print(myset)
# myset.pop()
# print(myset) # remove an arbitrary element from the set
# print(len(myset)) # print the length of the set

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print("Set1:", set1)
# print("Set2:", set2) 
# print("Union:", set1.union(set2))
# print("Intersection:", set1.intersection(set2))
# print("Difference:", set1.difference(set2))
# print("Symmetric Difference:", set1.symmetric_difference(set2))


