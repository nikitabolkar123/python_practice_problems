# Write a program to check if the given number is palindrome or not
n = int(input("enter the number"))
temp=n
rev = 0
while temp > 0:
    rem = temp% 10
    rev = rev * 10 + rem
    temp = temp // 10
if n == rev:
    print("pallindrome")
else:
    print("not pallindrome")

#Write a program to check if the given number is Armstrong or not.
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407
# are the Armstrong numbers.
# 153 = (1*1*1)+(5*5*5)+(3*3*3)
# where:
# (1*1*1)=1
# (5*5*5)=125
# (3*3*3)=27
# So:
# 1+125+27=153
n=int(input('enter the number'))
sum=0
temp=n
while temp >0:
    rem=temp%2==0
    cube=rem*temp*temp*temp
    sum=sum+cube+rem
    temp=temp//10
if temp==sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")

# Write a program to find a factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a number to compute the factiorial : "))
print(factorial(n))

# Write a program to find a fibonacci of a number.
# Fibonacci sequence specifies a series of numbers where the next number is found by adding up the two numbers just before it.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, … and so on.
nterms = int(input("How many terms? "))

n1=0
n2 = 1
count = 0

if nterms <= 0:
   print("enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence ",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

def bubble_sort_recursion(a):
    for i in range(len(a)-1): #len[a]=7, 7-1=6
        if a[i]>a[i+1]:  #a[0]>a[1]
            temp = a[i]  # temp = a[0] => temp = 4
            a[i] = a[i+1]    # a[0] = a[1] => a[1] = 4
            a[i+1] = temp  # a[1] = 4
            bubble_sort_recursion(a)
    return a
if __name__ == '__main__':
    a = [4, 3, 5, 6, 99, 12, 2]
    print(bubble_sort_recursion(a))
