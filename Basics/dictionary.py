info = {
    "Enroll No." : 23071368,
    "CGPA" : 9.02,
    "Roll No." : 61,
    "Subject"  : ['C', "Python", "Java", "HTML", "CSS", "JavaScript"],
    "Name" : "Yash Izate",
    "College" : "YCCE, Nagpur",
    "Topics" : ("dict", "set", "list", "tuple"),
    "isAdult" : True
}

# Adding Value
info["Branch"] = "VLSI"

# Printing Keys and Values
print(info["College"])
print(info["Name"])
print(info["Enroll No."])
print(info["Roll No."])
print(info["CGPA"])
print(info["Subject"])
print(info["Topics"])
print(info["isAdult"])

print(" ")

# Changing and Adding Values

info["Name"] = "Sharwari Mondhe"
info["College"] = "SIPNA, Amravati"
info["CGPA"] = 9.3
info["Gender"] = "Female"

# Printing Dictionary
print(info["College"])
print(info["Name"])
print(info["Enroll No."])
print(info["Roll No."])
print(info["CGPA"])
print(info["Subject"])
print(info["Topics"])


# Creating null dictionary

null_dict = {}

null_dict["Job"] =  "Web Developer" 

print(null_dict["Job"])

# Nested Dictionary

student = {
    "name" : "Yash",
    "age" : 21,
    "sub" : {
        "phy" : 58,
        "chem" : 59,
        "math" : 89
    } 
}

print(student)
print(student["sub"])
print(student["sub"]["chem"])