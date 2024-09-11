def factorial(x):
    if(x == 0 or x == 1):
        return 1
    fact = x * factorial(x-1)
    return fact

n = int(input("Enter the number: "))

result = factorial(n)
print(f"The factorial of {n} is equal to {result}")

