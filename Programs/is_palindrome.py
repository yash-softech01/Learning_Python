# list1 = [1, 2, 3, 2, 1]
# list1 = [5, 6, 8, 9, 0]
list1 = ['a', 'm', 'c', 'm', 'a']

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")