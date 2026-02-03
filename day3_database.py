#set
#a set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
#no duplicate values allowed
thisset = {"apple", "banana", "cherry"}
print(thisset)

#inbuilt functions in set
thisset.add("orange") #add item
print(thisset)
thisset.remove("banana") #remove item
print(thisset)
thisset.discard("cherry") #remove item without error if not found
print(thisset)
thisset.clear() #clear set
print(thisset)
#del thisset #delete set
#print(thisset) #this will raise an error because the set no longer exists

set1 = {"a", "b" , "c"}
set2 = {"a", "d" , "e"}
set3 = set1.union(set2) #join two sets
print(set3)
set4 = set1.intersection(set2) #get common items
print(set4)
set5 = set1.symmetric_difference(set2) #get items in either set, but not both
print(set5)
set6 = set1.difference(set2) #get items in set1 but not in set2
print(set6)
set7 = set1.update(set2) #update set1 with items from set2
print(set1)
set8 = set1.copy() #copy set
print(set8)
set9 = set1.pop() #remove and return an arbitrary item
print(set9)

#dictionary
#a dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written
#with curly brackets, and they have keys and values.
thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 }
print(thisdict)
#accessing items
x = thisdict["model"]
print(x)
y = thisdict.get("year")
print(y)
#changing values
thisdict["year"] = 2020
print(thisdict)
#adding items
thisdict["color"] = "red"
print(thisdict)
#removing items
thisdict.pop("model")
print(thisdict)
thisdict.popitem() #removes last inserted item
print(thisdict)
del thisdict["brand"]
print(thisdict)
thisdict.clear() #clear dictionary
print(thisdict)
#del thisdict #delete dictionary
#print(thisdict) #this will raise an error because the dictionary no longer exists

#nested dictionary
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)
#accessing nested dictionary
print(myfamily["child2"]["name"])

#tuple
#a tuple is a collection which is ordered and unchangeable. In Python tuples are written with
#round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#accessing items
print(thistuple[1])
#thistuple[1] = "orange" #this will raise an error because tuples are unchangeable
#tuple methods
print(thistuple.count("apple")) #returns the number of times a specified value occurs in a tuple
print(thistuple.index("cherry")) #searches the tuple for a specified value and returns the position of where it was found
#del thistuple #delete tuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#todays task
#create a system where user types a station name and code prints the ticket price
stations = {
    "new york": 100,
    "los angeles": 200,
    "chicago": 150,
    "houston": 120,
    "phoenix": 180
}
station_name = input("Enter the station name: new york, los angeles, chicago, houston, phoenix: ")
if station_name in stations:
    print(f"The ticket price to {station_name} is ${stations[station_name]}")
else:
    print("Station not found.")
