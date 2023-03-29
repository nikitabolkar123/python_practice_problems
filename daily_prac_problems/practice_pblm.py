
# Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.
# Example
# sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9] # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
# sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
# sum_odd_and_even([0, 0]) ➞ [0, 0])


def sum_odd_and_even(arr):
    if not all(arr):
        return arr
    return [reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 == 0, arr))),
            reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 != 0, arr)))]

# A list is given. Return a new list having the sum of all its elements except itself. For more clarity, check the
# examples below.
# Clarification
# [1, 2, 3, 4] = for first element => sum will be 2+3+4 = [9]
# [1, 2, 3, 4] = for second element => sum will be 1+3+4 = [9, 8]
# [1, 2, 3, 4] = for third element => sum will be 1+2+4 = [9, 8, 7]
# [1, 2, 3, 4] = for fourth element => sum will be 1+2+3 = [9, 8, 7, 6]
# Examples
# lst_ele_sum([1, 2, 3, 2, 1]) ➞ [8, 7, 6, 7, 8]
# lst_ele_sum([1, 2]) ➞ [2, 1]
# lst_ele_sum([1, 2, 3]) ➞ [5, 4, 3]
# lst_ele_sum([1, 2, 3, 4, 5]) ➞ [14, 13, 12, 11, 10]
# lst_ele_sum([10, 20, 30, 40, 50, 60]) ➞ [200, 190, 180, 170, 160, 150]
from functools import reduce

def lst_ele_sum(arr):
    list_ = []
    sum_list = []
    for i in range(len(arr)):
        list_.append(arr[i])
        arr.remove(arr[i])
        sum_ = reduce(lambda x, y: x + y, arr)
        sum_list.append(sum_)
        arr.insert(i, list_[0])
        list_.clear()
    return sum_list

print(lst_ele_sum([10, 20, 30, 40, 50, 60]))



# Given a balanced expression that can contain opening and closing parenthesis, check if it contains any duplicate
# parenthesis or not.
#
# Input: '((x+y))+z'
# Output: True
# Explanation: Duplicate () found in subexpression ((x+y))
#
# Input: '(x+y)'
# Output: False
# Explanation: No duplicate () is found
#
# Input: '((x+y)+((z)))'
# Output: True
# Explanation: Duplicate () found in subexpression ((z))

def duplicate_parenthesis(str):
    for i in range(len(str)-1):
        if str[i] == ')' and str[i+1] == ')':
            return True
    return False
# if __name__ == "__main__":
expression1 = '((x+y)+z)'
print( duplicate_parenthesis(expression1))


# Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a
# dictionary of objects like { "name": "John", "top_note": 5 }.
# Examples
# top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }
# top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }
# top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
def top_note(dict_):
    list_ = dict_.get('notes')
    # bubble sort
    for i in range(len(list_) - 1, 0, -1):
        for j in range(i):
            if list_[j] > list_[j + 1]:
                temp = list_[j]
                list_[j] = list_[j + 1]
                list_[j + 1] = temp
    dict_.update(top_note=list_[-1])
    dict_.pop('notes')
    return dict_

dict = { "name": "John", "notes": [3, 5, 4] }
print( top_note(dict))


# Given a string, return all combinations of non-overlapping substrings of it.
#
# Input : 'ABC'
# Output: {('A', 'B', 'C'), ('A', 'BC'), ('AB', 'C'), ('ABC')}
#
# Input : 'ABCD'
# Output: {('A', 'B', 'C', 'D'), ('A', 'B', 'CD'), ('A', 'BC', 'D'), ('A', 'BCD'), ('AB', 'C', 'D'), ('AB', 'CD'), ('ABC', 'D'), ('ABCD')}

def non_overlap_substrings(str):
    if not str:
        return {()}

    res = set()
    for i in range(1, len(str) + 1):
        prefix = str[:i]
        suffix_combinations = non_overlap_substrings(str[i:])
        for suffix_combination in suffix_combinations:
            res.add((prefix,) + suffix_combination)
        res.add((prefix,))

    return res
if __name__ == '__main__':
    print(non_overlap_substrings('ABC'))




