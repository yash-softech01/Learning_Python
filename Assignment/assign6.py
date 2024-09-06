# check perfect number - sum of factors excluding itself is equal to the number

n = int(input("Enter the number: "))
sum_factors = 0

for i in range(1,n):
    if(n%i == 0):
        sum_factors += i
    
if(sum_factors == n):
    print(f"{n} is the perfect number")
else:
    print("It is not the perfect number")