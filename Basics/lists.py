marks = [23,56,54,12,78]

print(marks)
print(marks[2])
print(marks[-2])

student = ["Yash","Izate", 61, "VLSI", 23071368, "YCCE", "Nagpur"]

print(student[2])
print("Name:", student[0]+ " " + student[1])
print("Roll NO.:", student[2])
print("Enrollement No.:", student[4])
print("College:", student[-2])
print("City:", student[-1])

# list are mutable , string are immutable

student[0] = "Sharwari"
print(student)

# List Slicing, ending index is excluded

print(marks[2:5])
print(student[-4:-1])

