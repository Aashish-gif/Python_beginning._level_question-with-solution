# 19. GCD of Two Numbers
# Write a program to find the greatest common divisor (GCD) of two numbers.
a=int(input("Enter a Number 1: "))
b=int(input("Enter a Number 2: "))
while a!=b:
 if a>b:
    a=(a-b)
 else:
    b=(b-a)
print("The GCD of number you enter is",a)