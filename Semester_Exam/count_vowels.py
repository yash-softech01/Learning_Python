#WAP to count no. of vowels in a string 

str = input("Enter a string: ")

count = 0

for i in str:
  if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
    count += 1
  else:
    continue

print(f"No. of vowels in {str} is ", count)


print(str[:4])