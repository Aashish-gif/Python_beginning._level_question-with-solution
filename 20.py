# 20. LCM of Two Numbers
# Write a program to find the least common multiple (LCM) of two numbers.
a=int(input("Enter a Number 1: "))
b=int(input("Enter a Number 2: "))
x=a
y=b
while a!=b:
    if a>b:
       a=a-b
    else:
        b=b-a
        print("The LCM of two Number is ",(x*y)/a)