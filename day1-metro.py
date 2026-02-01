#comments are lines that are not executed by the program and are used to explain the code
#for single line comments

'''
multiple lines
comment
'''

print("Hello, World!")  # This line prints a greeting message to the console

#data types in python
#1.string
"This is a string"
#2.integer
12345
#3.float
12.34
#4.boolean
True
False
#5.list
[1, 2, 3, 4, 5]
#6.tuple
(1, 2, 3, 4, 5)
#7.dictionary
{"key1": "value1", "key2": "value2"}
#8.set
{1, 2, 3, 4, 5}

#variables in python
#variable is a container that holds a value and is used to store data
name = "John Doe"  # string variable
age = 30           # integer variable
height = 5.9      # float variable
is_student = True  # boolean variable
fruits = ["apple", "banana", "cherry"]  # list variable
person = {"name": "John", "age": 30}  # dictionary variable 
unique_numbers = {1, 2, 3, 4, 5}  # set variable
coordinates = (10.0, 20.0)  # tuple variable

#to check the data type of a variable
print(type(name))        # Output: <class 'str'>
print(type(age))         # Output: <class 'int'>
print(type(height))      # Output: <class 'float'>  
print(type(is_student))  # Output: <class 'bool'>
print(type(fruits))      # Output: <class 'list'>
print(type(person))      # Output: <class 'dict'>
print(type(unique_numbers))  # Output: <class 'set'>
print(type(coordinates))  # Output: <class 'tuple'>

#math operations in python
a = 10
b = 5
addition = a + b          # Addition
subtraction = a - b       # Subtraction
multiplication = a * b    # Multiplication
division = a / b          # Division
modulus = a % b           # Modulus ,modulus gives the remainder of the division
exponentiation = a ** b   # Exponentiation
floor_division = a // b   # Floor Division ,floor division gives the largest integer less than or equal to the division result

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
print("Floor Division:", floor_division)

firsrt_name = "John"
last_name = "Doe"
print("Full Name:", firsrt_name + " " + last_name)  # String concatenation
print("my first name is {} and my last name is {}".format(firsrt_name, last_name))  # String formatting using format()

#len function
print("Length of first name:", len(firsrt_name))  # Output: Length of first name: 4
print("Length of last name:", len(last_name))    # Output: Length of last name: 3

#logical operations in python
#and, or, not
x = 10
y = 5
print(x > 5 and y < 10)  # Output: True , for and both conditions should be true
print(x > 5 or y > 10)   # Output: True , for or at least one condition should be true
print(not(x > 5))        # Output: False , not negates the condition

#list operations in python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)          # Add an element to the end of the list
numbers.remove(3)         # Remove an element from the list
numbers.sort()           # Sort the list in ascending order
numbers.reverse()        # Reverse the order of the list
numbers.insert(2, 10)   # Insert an element at a specific index
numbers.pop()              # Remove and return the last element of the list
numbers.count(2)          # Count occurrences of an element in the list
numbers.extend([7, 8, 9])  # Extend the list by appending elements from another list
print("List after append and remove:", numbers)  # Output: List after append and remove: [1, 2, 4, 5, 6]
print("Length of the list:", len(numbers))        # Output: Length of the list:
print("First element:", numbers[0])               # Output: First element: 1
print("Last element:", numbers[-1])               # Output: Last element: 6
print("Sliced list (index 1 to 3):", numbers[1:4])  # Output: Sliced list (index 1 to 3): [2, 4, 5]


#todays task
#script that calculates the fare for a metro ride based number of stations traveled
name = input("Enter your name: ")
stations = input("Enter number of stations traveled: ")
stations = int(stations)
fare = 10 + (stations * 5)
print("--------------------------------")
print("Metro Ride Receipt")
print("--------------------------------")
print("Name:", name)
print("Stations Traveled:", stations)
print("Total Fare: $", fare)
print("--------------------------------")
print("Thank you for riding the metro!")