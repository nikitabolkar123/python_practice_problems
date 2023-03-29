# program to perform arithmetic operation on numeric values using function
from set import l


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x//y
def mod(x,y):
    return x%y

x=int(input("enter the x value:"))
y=int(input("enter the y value"))
print(x,"+" ,y,"=", add(x,y))
print(x,"-" ,y,"=", sub(x,y))
print(x,"*" ,y,"=", mul(x,y))
print(x,"//",y,"=",div(x,y))
# print(x,"%",y,"=",mod(x,y))

# Write a Python function to find the maximum of three number
def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

max = max_of_three(4, 6, 2)
print(max)

# Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
def sum_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
print(sum_list((5, 6, 2, 3)))

# Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)

def mul_list(lst):
    total = 1
    for i in lst:
        total *= i
    return total
print(mul_list((7, 6, 2, 3)))

# Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def string_reverse(str1):

    rev_str = ""
    l = len(str1)
    while l > 0:
        rev_str += str1[ l - 1 ]
        l = l - 1
    return rev_str
print(string_reverse('1234abcd'))


#Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument. Go to the editor
#Click me to see the sample solution


def fact_no(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
# n=int(input(('enter the no')))
print(fact_no(9))


# Given an array of distinct integers, in-place replace each array element by its corresponding rank in the array.
# The minimum array element has the rank 1; the second minimum element has a rank of 2, and so on.

Input : [10, 8, 15, 12, 6, 20, 1]
Output: [4, 3, 6, 5, 2, 7, 1]

Input : [0, 1, -1]
Output: [2, 3, 1]


def replace_ranks(arr):
    n = len(arr)
    temp = arr.copy()
    temp.sort()
    rank = {}
    for i in range(n):
        rank[temp[i]] = i+1

    return arr
arr1 = [0,1,-1]
print(replace_ranks(arr1))

def replace_ranks(arr):
    n = len(arr)
    idx_arr = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if arr[idx_arr[i]] > arr[idx_arr[j]]:
                temp = idx_arr[i]
                idx_arr[i] = idx_arr[j]
                idx_arr[j] = temp


if __name__ == '__main__':
    print(replace_ranks([10, 8, 15, 12, 6, 20, 1])) # Output: [4, 3, 6, 5, 2, 7, 1]

# arr2 = [0, 1, -1]
# print(replace_ranks(arr2)) # Output: [2, 3, 1]



#Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x
# n=[]
# print(unique_list([l]))
#

def list_element_rank(b_list):
    a = sorted(b_list)
    for i in range(len(b_list)):
        b_list[i] = a.index(b_list[i]) + 1
    return b_list

a=[10, 8, 15, 12, 6, 20, 1]
print(list_element_rank(a))



def list_element_rank(b_list):
    rank_dict = {}
    for num in sorted(b_list):
        if num not in rank_dict:
            rank_dict[num] = len(rank_dict) + 1
    return [rank_dict[num] for num in b_list]

a = [10, 8, 15, 12, 6, 20, 1]
print(list_element_rank(a))







































# ranks = [0] * n
    # for i in range(n):
    #     ranks[idx_arr[i]] = i + 1
    # res_arr = [0] * n
    # for i in range(n):
    #     res_arr[i] = ranks[i]
    # return res_arr