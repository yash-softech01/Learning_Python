# merge 2 list

list1 = []
list2 = []

n1 = int(input("Enter number of elements in list 1 : "))
n2 = int(input("Enter number of elements in list 2 : "))

i1 = 0
while(i1<n1):
    a = int(input("Enter elements of list 1: "))
    list1.append(a)
    i1 += 1

i2 = 0
while(i2<n2):
    b = int(input("Enter elements of list 2: "))
    list1.append(b)
    i2 += 1

new_list = list1 + list2
 
new_list.sort()

print(new_list)
