list = []

n = int(input("Enter the no. of elements in a list: "))
for i in range(0,n):
    a = int(input("Enter element of list: "))
    list.append(a)

even_list = []
odd_list = []

for i in range(0,n):
    if(list[i]%2 == 0):
        even_list.append(list[i])
    else:
        odd_list.append(list[i])

list.sort()
print(" ")
print("This is even list: ", even_list)
print("This is odd list: ", odd_list)