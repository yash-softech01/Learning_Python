# Find the largest no in the list

list = []

n = int(input("Enter no. of elements in list: "))

for i in range(0,n):
    a = int(input("Enter the element of list: "))
    list.append(a)

list.sort()
print("The greatest no. in list : ", list[-1])