#set is a collection which is unordered and unindexed, that is iterable, mutable and has no duplicate elements.
#sets are written in {} brackets
#we cant get numbers using indexed number
s={10,20,30,40,50}
print(s)
for l in s:
    print(l)

#set()
l=[1,2,3,4,5]
s=set(l)
print(s)
#The add() method adds an element to the set.
# If the element already exists, the add() method does not add the element.

thisset = {"apple", "banana", "cherry"}

thisset.add("ap")

print(thisset)

#Remove()
#The remove() method removes the specified element from the set.
# This method is different from the discard() method, because the remove() method will raise an error if the specified
# item does not exist, and the discard() method will not.
s1={10,20,30,40,50}
s1.remove(20)
print(s1)

# The discard() method removes the specified item from the set.
#
# This method is different from the remove() method, because the remove() method will raise an error
# if the specified item does not exist, and the discard() method will not.
s1={10,20,30,40,50}
s1.discard(30)
print(s1)

# The pop() method removes a random item from the set.
# This method returns the removed item.
s1={10,20,30,40,50}
s1.pop()
print(s1.pop())
print(s1)

# The add() method adds an element to the set.
# If the element already exists, the add() method does not add the element.
s1={10,20,30,40,50}
s1.add(60)
print(s1)

# The update() method updates the current set, by adding items from another set (or any other iterable).
# If an item is present in both sets, only one appearance of this item will be present in the updated set.
l=[10,20,30,40,50]
s={1,2,3,4,5}
s.update(l)
print(s)

# The clear() method removes all elements in a set.
s1={10,20,30,40,50}
s1.clear()
print(s1)

