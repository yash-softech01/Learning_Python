# WAP to find The program takes a dictionary and multiplies all the items in the dictionary.

dict = {
  'A': 100,
  'B': 200,
  'C': 300,
  'D': 400,
  'E': 500
}

tot = 1
sum = 0

for i in dict.values():
  tot *= i
  sum += i

print("Total multiplication is ", tot)
print("Total sum is ", sum)
