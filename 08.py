# 8. Sum of Digits
# Write a program to find the sum of digits of a given number.
a=int(input("Enter number: "))
digit=0
while a!=0:
    digit=digit+a % 10
    a //=10
print("the sum of you entered number is:",digit)