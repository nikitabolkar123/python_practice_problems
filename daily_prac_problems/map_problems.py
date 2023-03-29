# Write a Python program to triple all numbers in a given list of integers. Use Python map
nums = (1, 2, 3, 4, 5, 6, 7)
print("original list is: ", nums)
result = map(lambda x: x + x + x, nums)
print("\nTriple of list numbers:")
print(list(result))

# 2. Write a Python program to add three given lists using Python map and lambda.
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]
print("list are: ")
print(nums1)
print(nums2)
print(nums3)
result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)
print(list(result))

# Write a Python program to listify the list of given strings individually using Python map.
color = ['Red', 'Blue', 'Black', 'White', 'Pink']
print("Original list: ")
print(color)
print("After listify the list of strings are:")
result = list(map(list, color))
print(result)

# Write a Python program to triple all numbers in a given list of integers. Use Python map.
nums = (1, 2, 3, 4, 5, 6, 7)
print("original list is: ", nums)
result = map(lambda x: x + x + x, nums)
print("triple of list numbers:")
print(list(result))


# Write a Python program to add two given lists and find the difference between them. Use the map() function.

def addition_subtrction(x, y):
    return x + y, x - y


nums_lst1 = [6, 5, 3, 9]
nums_lst2 = [0, 1, 7, 7]
print("original lists is:")
print(nums_lst1)
print(nums_lst2)
result = map(addition_subtrction, nums_lst1, nums_lst2)
print("Result is :", list(result))


# Define a function that doubles even numbers and leaves odd numbers as ii is
def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


numbers = [1, 2, 3, 4, 5]  # here creating list of number to apply the function
result = list(map(double_even, numbers))  # apply the function to each element in the list
print(result)


# Function to calculate sum of all elements in matrix
# an iterable and returns a list of the results.
def findSum(arr):
    return sum(map(sum, arr))


if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [2, 1, 2]]
    print("Sum = ", findSum(arr))

# find the length of some words.
example = ["Welcome", "to", "college"]
x = list(map(len, example))
print(x)


def changeCharacterToUpper(alpha):
    return str(alpha).upper()


charList = {"a", "b", "c", "d"}
result = map(changeCharacterToUpper, charList)
print(set(result))


# Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from
# a given sequence. Use the map() function
def change_cases(s):
    return str(s).upper(), str(s).lower()


chr_ars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("original characters are:\n", chr_ars)
result = map(change_cases, chr_ars)
# print("\nAfter converting above characters in upper and lower cases and eliminating duplicate letters:")
print(set(result))


def count_same_pairs(list1, list2):
    pairs = list(map(lambda x, y: (x, y), list1, list2))
    same_pairs = list(map(lambda pair: 1 if pair[0] == pair[1] else 0, pairs))
    return sum(same_pairs)


list1 = [1, 2, 3, 4]
list2 = [2, 2, 3, 4]
count = count_same_pairs(list1, list2)
print(count)

# Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.
student_data = [('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002', '37kg'),
                ('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]
print("original data:")
print(student_data)
students_data_name = list(map(lambda x: x[0], student_data))
students_data_dob = list(map(lambda x: x[1], student_data))
students_data_weight = list(map(lambda x: int(x[2][:-2]), student_data))
print("Student name:")
print(students_data_name)
print("Student date of birth:")
print(students_data_dob)
print("Student weight:")
print(students_data_weight)


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
#
