# print numbers in range that are not divisible by 2 or 3

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for i in range(lower, upper+1):
    if(i%2!=0 and i%3 != 0):
        print(i)
        