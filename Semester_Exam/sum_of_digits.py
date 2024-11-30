#  WAP to find sum of digits of a number

n = int(input("Enter a number: "))

sum = 0;

while(n>0):
  digit = n % 10 
  sum += digit
  n = n//10

print("The sum of digits of a number is ", sum)