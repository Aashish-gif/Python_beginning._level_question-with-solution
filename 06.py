# 6. Reverse a Number
# Write a program to reverse a given integer.
a=int(input("Enter a Number: "))
reverse=0
while a!=0:
    reverse = reverse * 10+ a % 10
a //=10
print("the reverse of your enter number is:",reverse)
