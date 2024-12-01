str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

count1 = 0
for i in str1:
  count1 += 1

count2 = 0
for j in str2:
  count2 += 1

if(count1 == count2):
  print("Both strings are equal")
elif(count1 > count2):
  print("Largest string: ", str1)
else:
  print("Largest string: ", str2)
