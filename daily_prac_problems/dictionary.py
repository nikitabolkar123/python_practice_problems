#Dictionary represents a group of elements in the form of key and value pairs
#dictionary in python is an ordered collection
#dict are mutable so we can modify its item without changing their identity
#dict are represented using {} curly bracket
#e.g...
student={101:"nikita",102:"saurav",103:"rani"}
print(student)

#dict are represented key and value pair so key cant be repeated and must be immutable
#value can be of any data type and can be duplicate
#keys are case sensitive

#Accessing Dictionary
#we can access value of a dictionary by referring to its key name,inside square brackets
student={101:"nikita",102:"saurav",103:"rani"}
print(student[101])
print(student[102])

student1={"nikita":101,"saurav":102,"rani":103}
print(student1["nikita"])
print(student1["saurav"])
print(student1.keys())
print(student1.values())

print(len(student))

#any() method
student={"nikita":101,"saurav":102,"rani":103}
print(any(student))


my_dict = {'a': 5, 'b': 8, 'c': 12, 'd': 6}
result = any(value > 10 for value in my_dict.values())
print(result)  # True
# check if any of them are greater than 10.
# The any() function then returns True because the value 12 satisfies the condition.

#all()
# The all() function returns True if all items in an iterable are true, otherwise it returns False
# If the iterable object is empty, the all()...function also returns True.
student={"nikita":101,"saurav":102,"rani":103}
print(all(student))

# The items() method returns a view object. The view object contains the key-value pairs of the dictionary,
# as tuples in a list.
student={"nikita":101,"saurav":102,"rani":103}
print(student.items())

#The get() method returns the value of the item with the specified key.

student={"nikita":101,"saurav":102,"rani":103}
print(student.get("nikita"))
print(student.get("ni"))

# if key not present and u tried to get it will give u none

# The clear() method removes all the elements from a dictionary.
student.clear()
print(student)

# The copy() method returns a copy of the specified dictionary.
student={"nikita":101,"saurav":102,"rani":103}
a=student.copy()
print(a)

#The pop() method removes the specified item from the dictionary.
# keyname	Required. The keyname of the item you want to remove
# defaultvalue--> Optional. A value to return if the specified key do not exist.
# If this parameter is not specified, and the no item with the specified key is found, an error is raised
a={1:"A",2:"B",3:"C"}
print(a.pop(2))
print(a.pop(12,6))# default 6 item

# The popitem() method removes the item that was last inserted into the dictionary.
# The removed item is the return value of the popitem() method, as a tuple
a={1:"A",2:"B",3:"C"}
print(a.popitem())

# The fromkeys() method returns a dictionary with the specified keys and the specified value.
dict= ('A', 'B', 'C')
d={}
thisdict ={}
thisdict=d.fromkeys(dict)
thisdict=d.fromkeys(dict,10) #bydefault value 10 for all
print(thisdict)
# bydefault value will none for all keys


# The update() method inserts the specified items to the dictionary.
a={1:"A",2:"B",3:"C"}
print(a)
a.update({4:"D"})
print(a)
a.update({1:"E"})
print(a)

