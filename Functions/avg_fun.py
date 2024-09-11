def average(x,y,z):
    sum = (x+y+z)
    avg = sum/3
    return avg

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

result = average(a,b,c)

print("Average : ", result)
