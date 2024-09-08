list = []

lower = int(input("Enter the lower limit of list: "))
upper = int(input("Enter the upper limit if list: "))
n = int(input("Enter the number by which to be divided: "))

for i in range(lower, upper+1):
    if(i%n == 0):
        list.append(i)
    else:
        continue

print(list)