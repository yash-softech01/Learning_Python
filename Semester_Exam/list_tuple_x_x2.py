#WAP to create a list of tuple with the first element as the number and second element as the square of them

lower = int(input("Enter lower limit of range: "))
upper = int(input("Enter upper limit of range: "))

list = []

for i in range(lower, upper+1):
  a = (i,i**2)
  list.append(a)

print(list) 