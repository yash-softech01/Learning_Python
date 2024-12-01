#WAP to take a marks of 5 subjects and show grades 

sub1 = int(input("Enter marks of 1 subject: ")) 
sub2 = int(input("Enter marks of 2 subject: ")) 
sub3 = int(input("Enter marks of 3 subject: ")) 
sub4 = int(input("Enter marks of 4 subject: ")) 
sub5 = int(input("Enter marks of 5 subject: ")) 

avg = (sub1 + sub2 + sub3 + sub4 + sub5)/5

if(avg >= 90):
  print("Grade: A")
elif(avg >= 80 and avg < 90):
  print("Grade: B")
elif(avg >= 70 and avg < 80):
  print("Grade: C")
elif(avg >= 60 and avg < 70):
  print("Grade: D")
elif(avg >= 50 and avg < 60):
  print("Grade: E")
else:
  print("You are Fail")