#Python Program to Read a Number n and Print the Natural Numbers Summation Pattern

n = int(input("Enter a number: "))

for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end="")
    if (j < i):
      print(" + ", end="")
  
  print(" =", sum(range(1,i+1)))
