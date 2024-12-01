# WAP to check if a number is a armstrong number (no equal to the sum of its digit's cube)

n = int(input("Enter a number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum += digit**3
    n //= 10
  
if(temp == sum):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")