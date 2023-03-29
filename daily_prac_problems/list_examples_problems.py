#List
#Lists are used to store multiple items in a single variable.
#list represents group of elements
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#list are similar to array but major difference is that arrray can store only one type of elements whereas list can
#store different type of elements. it can allow duplicate value
#list are mutable so we can modify its elements
#list are dynamic means which size can not fixed

my_list = [1,2,3,5.5,-1,"apple","orange"]
print(my_list)

#Accessing List's elements
###two ways to access list elements#####
#1...Indexing--->it is used to access individual (single) elements in a list
my_list = [1,2,3,5.5,-1,"apple","orange"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])
print(my_list[6])
print(my_list[-1])
print(my_list[-4])
print(my_list[:6])
print("***************************")
#2...slicing ---->its used to access group of elements of list..we can access range of elements using slicing
#The format for list slicing is [start:stop:step].
# start is the index of the list where slicing starts.
# stop is the index of the list where slicing ends.
# step allows you to select nth item within the range start to stop.

my_list = [1,2,3,5.5,-1,"apple",[5,6,7,8]]
print(my_list[2:4])
print(my_list[:2])
print(my_list[2:])
#my_list[:] ----->copy of the whole array
print(my_list[:])
#last two items...start -2 rest of elements can print
print(my_list[-2:])

#start not given end is -2 everything except the last two items
print(my_list[:-2])

#all the items in array or list reversed
print(my_list[::-1])


print("*****************************************")
#modify or updating elements
my_list = [1,2,3,5.5,-1,"apple","orange"]
print(my_list,id(my_list))
my_list[1]=9
print(my_list[1])
print(my_list,id(my_list))
#before and after modification address will be same,,,its shows that list is mutable

#type
my_list = [1,2,3,5.5,-1,"apple","orange"]
print(type(my_list))


##append the list
#To add an item to the end of the list, use the append() method:
my_list = [1,2,3,5.5,-1,"apple","orange"]
my_list.append("nikita")
print(my_list)

# Adding List to a List
my_list = [1,2,3,5.5,-1,"apple","orange"]
n_list=['vinay','saurav','sakshi']
my_list.append((n_list))
print('updates list is',my_list)

#extend() methods add items to list
my_list = [1,2,3,5.5,-1,"apple","orange"]
print(my_list)
my_list.extend([2,3,4])
print(my_list)

#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an item at the specified index:
my_list = [1,2,3,5.5,-1,"apple","orange"]
my_list.insert(0,8) #--->0 is index and 8 is element which we have to put that position but 1 value of item will be 1st index
print(my_list)

#The remove() method removes the specified item.
my_list = [1,2,3,5.5,-1,"apple","orange"]
my_list.remove(1)
print(my_list)

#The pop() method removes the specified index.
my_list = [1,2,3,5.5,-1,"apple","orange"]
my_list.pop(1)
print(my_list)
#If you do not specify the index, the pop() method removes the last item.
my_list = [1,2,3,5.5,-1,"apple","orange"]
my_list.pop()
print(my_list)

#The del keyword also removes the specified index:
my_list = [1,2,3,5.5,-1,"apple","orange"]
del my_list[5]
print(my_list)

#The del keyword can also delete the list completely.
my_list = [1,2,3,5.5,-1,"apple","orange"]
del my_list
# print(my_list)
##this will cause an error because you have succsesfully deleted "mylist".


#clear() list
#The clear() method empties the list.
#The list still remains, but it has no content.
my_list = [1,2,3,5.5,-1,"apple","orange"]
my_list.clear()
print(my_list)

#Python count() method returns the number of times element appears in the list. If the element is not present in the list,
# it returns 0.

apple = ['a','p','p','l','e']
# Method calling
count = apple.count('p')
# Displaying result
print("count of p :",count)

#The sort() method sorts the list ascending by default.

# You can also make a function to decide the sorting criteria(s).
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# # use to store different types of data type values also can store same type of values
# # Ordered, unchangeable and allow duplicates
# stor = ("car", 'like', 'apple', 30, 40, 3.2, True, 30)
# print(stor)
#
# # In tuple we can't store only single value if we do that then it will become a string not will tuple
# # for tuple we have to use quama (,) at least then only it will consider as it is tuple
# # we can not append in tuple
# print(len(stor))  # to check length
# print(type(stor))  # to check type
#
# print(stor[0])
# print(stor[5])
# print(stor[2:5])
# print(stor[:5])
# print(stor[2:])
# print("***")
#
# if "apple" in stor:
#   print("Yes, 'apple' is in the fruits tuple")
#
#
# # To update
# y = list(stor)
# y[1] = "Oranges"
# x = tuple(y)
# print(x)
#
#
# # To add values
# y = list(stor)
# y.append("banana")
# stor = tuple(y)
# print(stor)
#
#
# # Adding second tuple in previous tuple
# second_tuple = (100, 200)
# stor += second_tuple
# print(stor)
#
#
# y = list(stor)
# y.remove("apple")
# stor = tuple(y)
#
# for i in range(len(stor)):
#   print(stor[i])
#
#
# var = stor.count(100)
# print(var)
#
#
# temp = stor.index(100)
# print(temp)
#
# del stor