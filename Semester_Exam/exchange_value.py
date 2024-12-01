# WAP to exchange the value of two number without using a temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a+b
b = a-b
a = a-b

print("a is: ", a, "and b is: ", b)