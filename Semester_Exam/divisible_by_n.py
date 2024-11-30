# Python program to print all the numbers in a range divisible by a number 

lower = int(input("Enter lower limit of range: "))
upper = int(input("Enter upper limit of range: "))

n = int(input("Enter the number to be divided by: "))

print("The numbers are : \n")
for i in range(lower, upper+1): 
  if(i%n == 0):
    print(i)
  else:
    continue
