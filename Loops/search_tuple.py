tup = (1,4,9,16,25,36,49,64,81,100)
n = int(input("Enter the element to be found: " ))
i=0
while(i<len(tup)):
    if(tup[i] == n):
        print("Element found at index: ", i)
        break
    i+=1