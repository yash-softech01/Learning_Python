# WAP to swap first and last value of the list

list = [23,45,67,32,65,76,54]

temp = list[0]
list[0] = list[-1]
list[-1] = temp

print(list)