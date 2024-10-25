# 11. Swapping Two Numbers
# Write a program to swap two numbers without using a third variable.
a=int(input("enter a number 1: "))
b=int(input("enter a number 2: "))
a=a+b
b=a-b
a=a-b
print("swapping of your enter number is number 1,number 2 respectively",a,b)