lst = [i for i in range(10) if i % 2 == 0]
print(lst)

sqr_dict = {n: n * n for n in range(1, 11) if n % 2 == 0}
print(sqr_dict)

sqr_dict.update({11: 114})
sqr_dict.pop(11)
print(sqr_dict)


# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
# Example 1:
#
# Input: s = "hello"
# Output: "holle"
# Example 2:
#
# Input: s = "leetcode"
# Output: "leotcede"

def reverse_string(str):
    v = ""
    for char in str:
        if char in "aeiouAEIOU":
            v = v + char
    res_string = ""  # store res
    for char in str:
        if char in "aeiouAEIOU":
            res_string = res_string + v[-1]  # add last vowel from vowel string
            v = v[:-1]
        else:
            res_string = res_string + char  # add non vowel char
    return res_string

ab="hello"
print(reverse_string(ab))
    # for char in str1:


def reverse_string(str):
    v = []
    for char in str:
        if char.lower() in 'aeiou':
            v.append(char)
    res = ""
    for char in str:
        if char.lower() in 'aeiou':
            res = res + v.pop()
        else:
            res = res + char
    return res

if __name__ == "__main__":
    str = input('enter string')
    print(reverse_string(str))
