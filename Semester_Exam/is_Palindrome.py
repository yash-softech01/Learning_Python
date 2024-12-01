org_n = int(input("Enter a number: "))
temp = org_n
rev_n = 0

while(org_n>0):
  digit = org_n%10
  rev_n = rev_n*10 + digit
  org_n = org_n // 10

if(rev_n == temp):
  print("It is a Palindrome")
else:
  print("It is not Palindrome")