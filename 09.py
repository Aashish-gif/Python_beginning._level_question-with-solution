# 9. Prime Number Check
# Write a program to check whether a given number is prime.
a=int(input("Enter a Number: "))
prime=0
for i in range(2,a):
     a % i ==0
     prime + 1
if prime > 0:
 print("it is not prime")
else:
 print ("it is a prime number")