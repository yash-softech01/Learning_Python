# WAP to check wether a number is a Perfect Number (number which are sum of its factor)

n = int(input("Enter a number: "))

sum = 0

for i in range(1,n):
  if(n%i == 0):
    sum += i
  else: 
    continue


if(sum == n):
  print("It is a Perfect Number")
else:
  print("Not a Perfect Number")
