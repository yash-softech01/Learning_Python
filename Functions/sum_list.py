# function to find sum of elements in a list
def sum_list(x):
    sum = 0
    for i in range(0, len(x)):
        sum = sum + x[i]
    return sum    

# main code
list = []

n = int(input("Enter the no. of elements in list: "))

for i in range(0,n):
    a =  int(input("Enter element of the list: "))
    list.append(a)

result = sum_list(list)

print("Sum of elements of list: ", result)

