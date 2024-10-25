# 13. Leap Year Check
# Write a program to check whether a given year is a leap year.
a=int(input("enter a year: "))
if a % 4==0 and a % 100 != 0 or a%400==0:
    print(a,"you enter is leap year")
else:
    print(a,"you enter year is not leap year")