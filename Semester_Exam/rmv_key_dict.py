# WAP to remove a given key from a dictionary

dict = {'A': 10, 'B': 30, 'C': 50, 'D': 100}

key = input("Enter a key to remove (A-D): ")

if key in dict.keys():
  del dict[key]

print("Updated Dictionary: ", dict)