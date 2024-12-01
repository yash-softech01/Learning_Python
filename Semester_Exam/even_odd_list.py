#WAP to extract even and odd elements and make a new list separately

list = []
even = []
odd = []

n = int(input("Enter the no. of elements in a list: "))

for i in range(0,n):
  a = int(input(f"Enter {i+1} element: "))
  list.append(a)

for j in range(0,n):
  if(list[j] % 2 == 0):
    even.append(list[j])
  else:
    odd.append(list[j])

print("User list", list)
print("Even list: ", even)
print("Odd list: ", odd)