# A function without name is called as anonynous function... also known as lambda function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax
# lambda arguments : expression
# Add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(5))


# without lambda
def show(x):
    print(x)
show(5)
# with lambda
show = lambda x: print(x)
show(7)

# Lambda functions can take any number of arguments:
# Multiply argument a with argument b and return the result:
x = lambda a, b: a * b
print(x(5, 6))
# square,cube and avg of number
double = lambda a: a * a
cube = lambda a: a * a * a
avg = lambda x, y: (x + y) // 2
print(double(7))
print(cube(3))
print(avg(4, 6))

# *********************map function***********************
# The map() function executes a specified function for each item in an iterable
# The item is sent to the function as a parameter.
# The map() function is a built-in Python function that takes two arguments: a function and an iterable.
# The map() function applies the given function to each element of the iterable
# nd returns a new iterable with the results.
# syntax:--->map(function, iterable)
# function is the function to apply to each element of the iterable
# iterable is the iterable to apply the function to... an iterable like sets, lists, tuples, etc
# The map() function returns a map object, which is an iterator that generates the results of applying the given function
# to each element of the iterable.

fruits = ["apple", "banana", "cherry"]
upper_fruits = map(str.upper, fruits)
print(list(upper_fruits))


# The map() function returns an object of map class. The returned value can be passed to functions like
# list() - to convert to list
# set() - to convert to a set, and so on.
def calculateSquare(n):
    return n * n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
# print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

# In the above example, each item of the tuple is squared.

# How to use lambda function with map()?

numbers = (1, 2, 3, 4)
result = map(lambda x: x * x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

# Passing Multiple Iterators to map() Using Lambda
# In this example, corresponding items of two lists are added.
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1 + n2, num1, num2)
print(list(result))

# without using map
num = [1, 2, 3, 4, 5]
sqr_lst = []
sqr = lambda n: n ** 2
for n in num:
    sqr_lst.append(sqr(n))
print(sqr_lst)

# using map

num = [1, 2, 3, 4, 5]
sqr_num = list(map(lambda x: x ** 2, num))
print(sqr_num)

# *************filter***************************
# in Python, the filter() function is a built-in function that allows you to filter elements from
# an iterable (list, tuple, set, etc.) based on a given condition.
# filter out even number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = (filter(lambda x: x % 2 == 0, numbers))
# filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #if u convert into list will able to print filter obj again
print(list(filtered_numbers))
print(list(filtered_numbers))  # empty list...if we want to print

# True False
numbers = [True, True, False, 0, 1, 2, 3, None]
print(list(filter(None, numbers)))

# filter the vowel numbers
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False


filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)

# reduce() function:---is used to reduce the sequence of the elements to a single value by a processing elements
# according to the functioned supplied. it returns the single value
# function is a part of functool module so u have to import it before using it
