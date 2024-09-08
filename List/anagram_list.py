str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")

if(sorted(str1) == sorted(str2)):
    print("Strings are anagram")
else:
    print("Strings are not anagram")
