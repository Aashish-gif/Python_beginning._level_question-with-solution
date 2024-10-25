# 15. Sum of Array Elements
# Write a program to find the sum of all elements in an array.
arr=[1,2,3,4,8]
b=len(arr)
sum=0
for i in range(0,b):
    sum=sum+arr[i]
print("sum of array is: ",sum)
