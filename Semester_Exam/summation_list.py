# The program takes a list from the user and finds the cumulative sum of a list where the ith element is the sum of the first i+1 elements from the original list.

list = []
new_list = []

n = int(input("Enter the no. of elements in a list: "))

for i in range(0,n):
  a = int(input(f"Enter {i+1} element: "))
  list.append(a)

print("User List: ", list)


for x in range(0,len(list)):
  b = sum(list[0:x+1])
  new_list.append(b)

print("New List: ", new_list)


