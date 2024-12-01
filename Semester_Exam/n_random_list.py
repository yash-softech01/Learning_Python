# The program takes in the number of elements and generates random numbers from 1 to 20 and appends them to the list.

import random

list = []

n = int(input("Enter the no. of elements in list: "))

for i in range(n):
  a = random.randint(1,20)
  list.append(a)

print("Randomised List: ", list)
