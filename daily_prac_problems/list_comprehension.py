# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# list comprehension represents creation of new list from an iterable object that satisfying a given condition

# syntax:--
# new_list=[exp for an item in iterable_obj if statement]
# there can be zero or more if statements
# there can be one or  multiple for loops

# e.g without list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# with list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# there can be zero or more if statement
# there can be one or multiple for loops

lst1 = [i + 1 for i in range(20) if i % 2 == 0]
print(lst1)

lst2 = [i + 1 for i in range(20) if i % 2 == 0 if i % 3 == 0]
print(lst2)

n = [m for m in range(1, 50)]
print(n)

# Nested list comprehension
a = [[24, 30, 36], [28, 35, 42]]

for i in range(6, 8):
    for j in range(4, 7):
        pass

lst = [[i * j for j in range(4, 7)] for i in range(6, 8)]
print(lst)
