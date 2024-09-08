n = int(input("Enter the number: "))

if(n < 0):
    is_Prime = False
else:
    is_Prime = True

for i in range(2,n):
    if(n%i == 0):
        is_Prime = False

if(is_Prime):
    print("Prime No.")
else:
    print("Not Prime")
 
