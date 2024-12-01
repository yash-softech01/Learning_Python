#WAP to swap first and last value of the list

list = []

n = int(input("Enter the no. of elements in the list: "))

for i in range(0,n):
  a = int(input(f"Enter {i+1} element: "))
  list.append(a)

print("User List: ", list)

temp = list[0]
list[0] = list[-1]
list[-1] = temp


print("Swapped list:", list)