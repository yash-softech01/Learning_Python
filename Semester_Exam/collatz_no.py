# WAP to test collatz conjecture for a given number

n = int(input("Enter a number: "))

while n > 1:
    print(n, end=''+ " ")
    if(n%2): #odd
        n = 3*n + 1
    else: #even
        n = n//2

print(1, end='')
