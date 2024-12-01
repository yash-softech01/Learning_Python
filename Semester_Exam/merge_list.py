#WAP to merge two list and sort it

list1 = []
list2 = []

n1 = int(input("Enter the number of elements in list 1: "))
for i in range(0,n1):
  a = int(input(f"Enter {i+1} element: "))
  list1.append(a)

n2 = int(input("Enter the number of elements in list 2: "))
for i in range(0,n2):
  b = int(input(f"Enter {i+1} element: "))
  list1.append(b)

list = list1 + list2

list.sort()

print(list)