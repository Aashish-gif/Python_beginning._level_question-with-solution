# 5. Factorial of a Number
# Write a program to calculate the factorial of a given number.
a=int(input("Enter a Number: "));
factorial=1
for i in range(1,a+1):
   factorial=factorial*i
print("factorial of your entered number",factorial);