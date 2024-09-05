num1 = int(input("Enter the number to check if it is a multiple: "))
num2 = int(input("Enter the number to divide by (divisor): "))

if(num2 != 0):
    if(num1%num2 == 0):
        print(f"{num1} is a multiple of {num2}")
    else:
        print(f"{num1} is not a multiple of {num2}")
else:
    print("Division by 0 is not valid.")