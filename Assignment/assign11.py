# Swap the value without using third variable

a = int(input("Enter the value of first element: "))
b = int(input("Enter the value of second element: "))

a = a + b
b = a - b
a = a - b

print("Value of a: ", a, " Value of b: ", b)