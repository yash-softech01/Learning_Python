# WAP to print all the numbers between a range that are not divisible by 2 or 3 either 

lower = int(input("Enter lower limit of range: "))
upper = int(input("Enter upper limit of range: "))

for i in range(lower, upper+1):
  if(i%2 != 0 and i%3 != 0 ):
    print(i)
  else:
    continue


