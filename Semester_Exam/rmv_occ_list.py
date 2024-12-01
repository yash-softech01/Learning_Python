# WAP to remove the ith occurance of the given word in a list where words can repeat

# list = []
# new_list = []

# n = int(input("Enter the number of elements in a list: "))
# for i in range(0, n):
#     a = input(f"Enter {i+1} element: ")
#     list.append(a)

# print("User List: ", list)

# str = input("Enter the element to remove: ")

# for j in range(0,n):
#     if(str != list[j]):
#         new_list.append(list[j])
#     else:
#         continue

# print("Updated List: ", new_list)



# Input the list

list = []

n = int(input("Enter the number of elements in a list: "))
for i in range(n):
    a = input(f"Enter element {i+1}: ")
    list.append(a)

print("User List:", list)

# Input the word to remove and the occurrence number
word = input("Enter the word to remove: ")
occurrence = int(input("Enter the occurrence to remove (1 for first, 2 for second, etc.): "))

# Logic to remove the ith occurrence
count = 0
for i in range(len(list)):
    if list[i] == word:
        count += 1
        if count == occurrence:
            del list[i]
            break

# Output the updated list
print("Updated List:", list)
