#Write a Python Program to Map Two Lists into a dictionary

keys = []
values = []

n = int(input("Enter no. of elements for a dictionary: "))

print("\nFor Key: ")
for i in range(0,n):
  key = input(f"Enter {i+1} key: ")
  keys.append(key)

print("\nFor Values: ")
for i in range(0,n):
  value = input(f"Enter {i+1} value: ")
  values.append(value)

dictionary = dict(zip(keys,values))

print("\nDictionary: " , dictionary)
