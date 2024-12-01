# WAP to find the largest element in the list

list = []

n = int(input("Enter the no. of elements in a list: "))

for i in range(0,n):
  a = int(input(f"Enter {i+1} element: "))
  list.append(a)

#largest = max(list)
list.sort()

print("The largest element is ", list[-1])