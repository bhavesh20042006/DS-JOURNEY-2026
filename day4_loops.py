#loops
#they are used to repeat a block of code until a certain condition is met
#there are two types of loops in python: for and while

#for loop
#it is used to iterate over a sequence (list, tuple, string) or other iterable objects

#example
name = "John"
for letter in name:
    print(letter)
    if letter == "o":
        print("Found the letter o!")
        break #this will exit the loop when the letter o is found

colours = ["red", "green", "blue"]
for colour in colours:
    print(colour)

for i in range(5): #this will iterate from 0 to 4
    print(i)

for i in range(1, 10, 2): #this will iterate from 1 to 9 with a step of 2
    print(i)

#todays task 
#create a smart tool that calculates the ticket ptice based on number of stations using a for loop
stations = int(input("Enter the number of stations: "))
ticket_price = 0
for i in range(stations):
    ticket_price += 5 #assuming each station costs 5 units
print(f"The ticket price is: {ticket_price} units")
