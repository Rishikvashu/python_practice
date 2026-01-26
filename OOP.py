# class University:
#     def __init__(self, name, location, total_students, departments): # Parametrized constructor
#         self.name = name
#         self.location = location
#         self.total_students = total_students
#         self.departments = departments

#     def about_university(self):
#         return f"The name of the university is {self.name} and it is located in {self.location}"
    
#     def add_department(self, department_name):
#         self.departments.append(department_name)
    
#     def get_total_students(self):
#         return self.total_students
    
#     def display_details(self):
#         print(f"\nThe name of the university is {self.name} and it is located in {self.location}\n")
#         print(f"Name: {self.name}\n")
#         print(f"Location: {self.location}\n")
#         print(f"Total Students: {self.total_students}\n")
#         print(f"Departments: {', '.join(self.departments)}\n")

# university_offline = University(
#     name= "Oxford University Offline",
#     location= "Oxford, England",
#     total_students=22000,
#     departments= ["History", "Geography"]
# )

# university_online = University(
#     name= "Oxford University Online",
#     location= "Oxford, England 12",
#     total_students=12000,
#     departments= ["English", "Ethics"]
# )

# # university_online.add_department("Data Science")
# print(university_online.display_details())

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# class Student:

#     def __init__(self, name, msub1, msub2, msub3):
#         self.name = name
#         self.msub1 = msub1
#         self.msub2 = msub2
#         self.msub3 = msub3

#     def average_marks(self):
#         total = self.msub1 + self.msub2 + self.msub3
#         return total/3
    
#     def qualify_status(self):
#         #return self.average_marks() >= 50
#         # Or
#         if self.average_marks() >= 50:
#             return 'Pass'
#         else:
#             return 'Fail'
        
#     def display_details(self):
#         # print(f"Name : {self.name}")
#         # print(f"msub1 : {self.msub1}")
#         # print(f"msub2 : {self.msub2}")
#         # print(f"msub3 : {self.msub3}")
#         print(f"The average marks for {self.name} are : {self.average_marks() : .2f}")
#         print(f"Status : {self.qualify_status()}")
#         # print(f"Status : {'Pass' if self.is_pass() else 'Fail' }")

# name = str(input("Enter the name of student: "))
# msub1 = float(input("Enter the msub1 : "))
# msub2 = float(input("Enter the msub2 : "))
# msub3 = float(input("Enter the msub3 : "))

# student = Student(name, msub1, msub2, msub3)

# student.display_details()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^OOP Aggregation^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# class Customer:

#     def __init__(self, name, phone, address):
#         self.name = name
#         self.phone = phone
#         self.address = address

#     def edit_profile(self, new_name , new_phone, new_city, new_pincode, new_state):
#         self.name = new_name
#         self.phone = new_phone
#         self.address.change_address(new_city, new_pincode, new_state) # Aggregation happening here
        
# class Address:    

#     def __init__(self, city, pincode, state):
#         self.city = city
#         self.pincode = pincode
#         self.state = state

#     def change_address(self, new_city, new_pincode, new_state):
#         self.city = new_city
#         self.pincode = new_pincode
#         self.state = new_state

# address = Address("Agra", 283204, "Uttar Pradesh")
# customer = Customer("Rishi", 7530929027, address)
# print(customer.address.city)
# customer.edit_profile("Harsh", 788876788, "Mathura", 978776, "Delhi" )
# print(customer.name)
# # print(customer.address) # prints: <__main__.Address object at 0x000002A5637A86E0>
# print(address.pincode)
# address2 = Address("Mumbai", 400001, "Maharashtra")
# customer.address = address2
# print(address.city)           # Mathura (old object)
# print(customer.address.city)  # Mumbai (new object)
# print(address.pincode)           
# print(customer.address.pincode)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class Atm:
# Functions: 
# 1: Create_pin
# 2: Deposit
# 3: Withdraw
# 4: Check_balance


    def __init__(self):
        self.pin = None
        self.balance = 0

    def menu(self):
        while True:
            user_input = input("""
Hello, How would you like to proceed?
1. Enter 1 to Create Pin
2. Enter 2 to Deposit
3. Enter 3 to Withdraw
4. Enter 4 to Check Balance
5: Enter 5 to Exit
""")
        
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Exited Successfully")
                break
            else:
                print("Invalid Choice")

    def create_pin(self):
        self.pin = int(input("Enter your pin:"))
        print("Pin created successfully")

    def deposit(self):
        if self.pin is None:
            print("Create pin first")
            return

        pin = int(input("Enter Your Pin:"))
        if pin == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance = self.balance + amount
            print(f"{amount} Rs. deposited successfully")
        else:
            print("Invalid Pin")
    
    def withdraw(self):
        pin = int(input("Enter Your Pin:"))
        if pin == self.pin:
            amount = int(input("Enter the amount to Withdraw: "))
            if  amount <= self.balance:
                self.balance = self.balance - amount
                print(f"Please collect the amount: {amount}Rs.")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")
    
    def check_balance(self):
        pin = int(input("Enter Your Pin:"))
        if pin == self.pin:
            print(f"Current Balance: {self.balance} Rs." )
        else:
            print("Invalid Pin")

sbi = Atm()
sbi.menu()
