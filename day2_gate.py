#conditional operators: >, <, >=, <=, ==, !=
x = 10
y = 20
print("x > y:", x > y)   #False
print("x < y:", x < y)   #True
print("x >= y:", x >= y) #False
print("x <= y:", x <= y) #True
print("x == y:", x == y) #False
print("x != y:", x != y) #True

#conditional statements
#if, else, elif
a = int(input("Enter your age: "))
print("Your age is:", a)
if a < 18:
    print("You are a minor.")  #if condition is true
elif a == 18:
    print("You are just an adult.")  #elif condition is true
else:
    print("You are an adult.")  #else condition is executed when all above conditions are false

# indentation in python
# indentation is very important in python as it defines the block of code
b = int(input("Enter a number: "))
if b % 2 == 0:
    print(b, "is an even number.")  #indented block
    print("This number is divisible by 2.")
else:
    print(b, "is an odd number.")   #indented block
    print("This number is not divisible by 2.")

apple_price = 210
budget = 200
if apple_price <= budget:
    print("You can buy the apple.")
elif apple_price - budget <= 20:
    print("You are short of money, but you can still buy the apple.")
else:
    print("You cannot buy the apple.")

num = int(input("Enter a number to check if it's positive, negative or zero: "))
if num > 0:
    print(num, "is a positive number.") #if block
elif num < 0:
    print(num, "is a negative number.") #elif block
else:
    print("The number is zero.")        #else block

#nested if-else
#when an if-else statement is present inside another if or else block
marks = int(input("Enter your marks: "))
if marks >= 0 and marks <= 100:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Invalid marks entered.")

#todats task
#you are coding a logic for a metro gate it needs to check if passenger has enough money
balance = float(input("Enter your metro card balance: "))
if balance < 20:
    print("Insufficient balance. Please recharge your metro card.")
elif balance >= 20 and balance < 50:
    print("You have enough balance for a single ride.")
else:
    print("You have enough balance for multiple rides.")


