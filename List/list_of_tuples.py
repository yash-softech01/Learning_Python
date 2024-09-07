# Python Program to Create a List of Tuples with the First Element as the Number and 
# Second Element as the Square of the Number

lower = int(input("Enter lower range of the list: "))
upper = int(input("Enter upper range of the list: "))

result = []

for i in range(lower, upper+1):
    a = (i, i**2)
    result.append(a)

print(result)    