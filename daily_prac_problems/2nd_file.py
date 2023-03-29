# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
# unique and you may return the result in any order.
# from grid import grid
#
# arr = []
# for row in grid:
#     arr.extend(row)
#     ans = 0
# for ele in arr:
#     if ele < 0:
#         ans += 1
#     return ans

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of
# negative numbers in grid.

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
def countNegatives(grid):
    m = len(grid)
    n = len(grid[0])
    count = 0
    row = 0
    col = n - 1
    while row < m and col >= 0:
        if grid[row][col] < 0:
            count += m - row
            col -= 1
        else:
            row += 1
    return count


grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
num_negatives = countNegatives(grid)
print(num_negatives)


# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
#
# Return all the common strings with the least index sum. Return the answer in any order.
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        for i in list1:
            if i in list2:
                c = list2.index(i) + list1.index(i)
                d[c] = d.get(c, []) + [i]
        return d.get(min(d.keys()))


sol = Solution()
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
result = sol.findRestaurant(list1, list2)
print(result)


# Largest Number At Least Twice of Others\class Solution(object):
# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is,
# return the index of the largest element, or return -1 otherwise.
class Solution:
    def dominantIndex(self, nums):
        a = sorted(nums)
        if a[-1] >= a[-2] * 2:
            return nums.index(a[-1])
        else:
            return -1


sol = Solution()
nums = [3, 6, 12, 0]
result = sol.dominantIndex(nums)
print(result)

# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also
# create a lambda function that multiplies argument x with argument y and prints the result. Go to the editor
# Sample Output:
# 25
# 48
a = lambda x: x + 15
print(a(5))
r = lambda a: a + 15
print(r(10))
r = lambda x, y: x * y
print(r(12, 4))


# Write a Python program to create a function that takes one argument, and that argument will be multiplied
# with an unknown given number. Go to the editor
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# # Quintuple the number 15 = 75
def multiply(n):
    return lambda x: x * n


result = multiply(2)
print("double the number of 15", result(15))
result = multiply(3)
print("triple the number of 15", result(15))
result = multiply(4)
print("Quadruple the number of 15", result(15))
result = multiply(5)
print("Quintuple the number 15 =", result(15))
#
# . Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key=lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)


#
# # Define a list
# my_list = [10, 20, 30, 40, 50]
#
# # Create a new list with the swapped elements
# new_list = [my_list[-1]] + my_list[1:-1] + [my_list[0]]
#
# # Print the original and updated lists
# print(my_list)
# print(new_list)
def swapList \
                (newList):
    size = len(newList)

    # Swapping
    temp = newList[0]  # 12
    newList[0] = newList[size - 1]  # 3

    newList[size - 1] = temp

    return newList


newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# Examples:
#
# Input: List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output: [19, 65, 23, 90]
#
# Input: List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output: [1, 5, 3, 4, 2]
def a(lst):
    size = len(lst)
    for i in range(size):
        temp = lst[1]
        lst[1] = lst[-1]
        lst[-1] = temp
    return lst


lst = [12, 35, 9, 56, 24]
print(a(lst))


def swap_elements(lst, pos1, pos2):
    """
    Swaps the elements at positions pos1 and pos2 in the list lst.
    """
    # lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    temp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = temp
    return lst


# Example usage
my_list = [23, 65, 19, 90]
pos1 = 1
pos2 = 3
print("Before swap:", my_list)

# Swap the elements at positions pos1 and pos2
swap_elements(my_list, pos1, pos2)
print("After swap:", my_list)


# Given two numbers, write a Python code to find the Maximum of these two numbers.
#
# Examples:
#
# Input: a = 2, b = 4
# Output: 4
def max_num(n1, n2):
    # leng=len(no)
    # for i in range(leng):
    #     for j in range(i,i+1):
    if n1 > n2:
        # print(n1)
        return n1
    else:
        return n2


print(max_num(-1, -2))

lst = [1, 6, 3, 5, 3, 4]
# checking if element 7 is present
# in the given list or not
i = 7
# if element present then return
# exist otherwise not exist
if i in lst:
    print("exist")
else:
    print("not exist")

a = [6, 0, 4, 1]
c = 0
for i in a:
    c += i
avg = c / 2
print(avg)
print(c)

# Python program to find smallest number in a list
# Input : list1 = [10, 20, 4]
# Output : 4
#
# Input : list2 = [20, 10, 20, 1, 100]
# Output : 1
# list1 = [10, 20, 4, 45, 99]

# define a function to find the smallest element
list1 = [10, 20, 2, 45, 99]


def smallest_num(lst):
    smallest = lst[0]
    for element in lst:
        if element < smallest:
            smallest = element
    return smallest


# call the function and print the result
smallest_element = smallest_num(list1)
print("Smallest element is:", smallest_element)

# Python program to print even numbers in a list
Input: list1 = [2, 7, 5, 64, 14]
Output: [2, 64, 14]


def even(lst):
    even_nums = []
    for no in lst:
        if no % 2 == 0:
            even_nums.append(no)
    return even_nums


# Example usage
a = [2, 7, 5, 64, 14]
even_list = even(a)
print(even_list)

# Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# Input: list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

# Input: list2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1
list1 = [10, -21, 4, -45, 66, -93, 1]
p_count = 0
n_count = 0
for i in list1:
    if i > 0:
        p_count += 1
    else:
        n_count += 1

print("positive no:", p_count)
print("negative no:", n_count)


def lengthOfLongestSubstring(s):
    # Base condition
    if s == "":
        return 0
    start = 0
    # Ending index of window
    end = 0
    # Maximum length of substring without repeating characters
    maxLength = 0
    # Set to store unique characters
    unique_characters = set()
    # Loop for each character in the string
    while end < len(s):
        if s[end] not in unique_characters:
            unique_characters.add(s[end])
            end += 1
            maxLength = max(maxLength, len(unique_characters))
        else:
            unique_characters.remove(s[start])
            start += 1
    return maxLength


s = "pwwkew"
print(lengthOfLongestSubstring(s))
