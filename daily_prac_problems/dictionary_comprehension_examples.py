# Dictionary comprehension is an elegant and concise way to create dictionaries.
# without comprehension
dict1 = {}
for num in range(1, 11):
    dict1[num] = num * num
print(dict1)

# with dictionary comprehension example
square_dict = {num: num * num for num in range(1, 11)}
print(square_dict)

# we can use conditions in that
# dictionary comprehension example
square_dict = {num: num * num for num in range(1, 11) if num % 2 == 0}  # if num%3==0}
print(square_dict)

# else
dict2 = {n: (n if n % 2 == 0 else 'invalid') for n in range(10)}
print(dict2)

# tuple convert into dict
lst = [(101, "rahul"), (102, "ram")]
dict1 = {k: v for k, v in lst}
print(dict1)

lst = [n * n for n in range(10)]
print(lst)
dict = {n: n * n for n in range(1, 10)}
print(dict)
lst = [1, 2, 3, 4, 5]
lst.extend([2])
print(lst)
lst.insert(1, 7)
print(lst)
lst.remove(3)
print(lst)
