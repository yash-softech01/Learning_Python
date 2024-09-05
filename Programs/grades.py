phy = int(input("Enter marks in physics out of 100: "))
chem = int(input("Enter marks in chemistry out of 100: "))
math = int(input("Enter marks in maths out of 100: "))

marks = (phy+chem+math)/3

print("Percentage: ", marks)

if(marks>= 90):
    print("Grade: A")
elif(marks>= 80 and marks< 90):
    print("Grade: B")
elif(marks>= 70 and marks< 80):
    print("Grade: C")
elif(marks>= 60 and marks< 70):
    print("Grade: D")
else:
    print("You are Fail")