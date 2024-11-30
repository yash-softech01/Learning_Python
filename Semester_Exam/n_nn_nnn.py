#WAP to read a number n and compute for n + nn + nnn

n = int(input("Enter a number: "))

temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp

result = n + int(t1) + int(t2)

print("The value is: ",result)