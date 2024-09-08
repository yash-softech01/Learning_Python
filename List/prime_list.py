# make a list of prime numbers between te specified range

l = int(input("Enter lower range: "))
u = int(input("Enter upper range: "))

list = []

for i in range(l,u+1):
    if(i>1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if(i%j == 0):
                is_prime = False
                break
    if(is_prime): 
        list.append(i)

print("Prime number list : ", list)



