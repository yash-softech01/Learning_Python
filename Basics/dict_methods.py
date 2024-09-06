
student = {
    "name" : "Yash",
    "age" : 21,
    "sub" : {
        "phy" : 58,
        "chem" : 59,
        "math" : 89
    } 
}

# length of student
print(len(student))
print(" ")

# type casting of dict into list or tuple
print(list(student.keys()))
print(" ")

# return all values
print(student.values())
print(" ")

# .items  return all pairs in tuple forms

print(student.items())
print(" ")

print(list(student.items()))