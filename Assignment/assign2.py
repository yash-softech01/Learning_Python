# compute n+nn+nnn

n = int(input("Enter the number: "))
temp = str(n)

t1 = temp + temp 
t2 = temp + temp + temp

compute = n + int(t1) + int(t2)

print(compute)