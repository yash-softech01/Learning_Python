# The program takes a dictionary and checks if a given key exists in a dictionary or not

dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

key = input("Enter a key to find: ")

if key in dict.keys():
  print("Key is present and its value is ", dict[key])
else:
  print("Key isn't present")


