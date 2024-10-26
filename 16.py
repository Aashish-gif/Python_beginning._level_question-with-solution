# 16. Largest Element in an Array
# Write a program to find the largest element in an array.
a=[1,2,8,18,5]
larget=a[0]
b=len(a)
for i in range(1,b):
  if a[i]>larget:
    larget=a[i]
print("The largest Number in array is",larget)



