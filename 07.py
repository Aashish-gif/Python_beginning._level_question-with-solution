# 7. Palindrome Check
# Write a program to check whether a given number is a palindrome.
a=int(input("enter a number: "))
reverse=0
b=a
while a!=0:
    reverse=reverse*10+a % 10
    a //=10
if(reverse==b):
    print("enter number is palindrome")
else:
    print("enter number is not palindome")
            

    
