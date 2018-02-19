Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def Student_Grade():
	Name=input("Enter Student Name:")
	ID=int(input("Enter Student ID:")
	Marks=int(input("Enter Student Marks:")
		  
SyntaxError: invalid syntax
>>> def Student_Grade():
	Name=input("Enter Student Name:")
	ID=int(input("Enter Student ID:")
	Marks=int(input("Enter Student Marks:")
		  
SyntaxError: invalid syntax
>>> def Student_Grade():
	Name=input("Enter Student Name:")
	ID=int(input("Enter Student ID:"))
	Marks=int(input("Enter Student Marks:"))
		  if Marks>70 and Marks<100:
		  
SyntaxError: unexpected indent
>>> def Student_Grade():
	Name=input("Enter Student Name:")
	ID=int(input("Enter Student ID:"))
	Marks=int(input("Enter Student Marks:"))
if Marks>70 and Marks<100:
		  
SyntaxError: invalid syntax
>>> def Student_Grade():
	Name=input("Enter Student Name:")
	ID=int(input("Enter Student ID:"))
	Marks=int(input("Enter Student Marks:"))
       if Marks>70 and Marks<100:
		  
SyntaxError: unindent does not match any outer indentation level
>>> def Student_Grade():
Name=input("Enter Student Name:")
ID=int(input("Enter Student ID:"))
Marks=int(input("Enter Student Marks:"))
if Marks>70 and Marks<100:
		  
SyntaxError: expected an indented block
>>> def Student_Grade():
	Name=input("Enter Student Name:")
	ID=int(input("Enter Student ID:"))
	Marks=int(input("Enter Student Marks:"))
	if Marks>=70 and Marks<=100:
		  print("Grade of Student {Name} with ID {ID} is A")
	elif Marks>=50 and Marks<70:
		  print("Grade of Student {Name} with ID {ID} is B")
	elif Marks>=40 and Marks<50:
		  print("Grade of Student {Name} with ID {ID} is C")
	else:
		  print("Fail")

		  
>>> Student_Grade()
		  
Enter Student Name:Harsha
Enter Student ID:310231243
Enter Student Marks:78
Grade of Student {Name} with ID {ID} is A
>>> def Student_Grade():
	Name=input("Enter Student Name:")
	ID=int(input("Enter Student ID:"))
	Marks=int(input("Enter Student Marks:"))
	if Marks>=70 and Marks<=100:
		  print("Grade of Student:" Name "with ID:" ID "is A")
	elif Marks>=50 and Marks<70:
		  print("Grade of Student:" Name "with ID:" ID "is B")
	elif Marks>=40 and Marks<50:
		  print("Grade of Student:" Name "with ID:" ID "is C")
	else:
		  print("Fail")
		  
SyntaxError: invalid syntax
>>> def Student_Grade():
	Name=input("Enter Student Name:")
	ID=int(input("Enter Student ID:"))
	Marks=int(input("Enter Student Marks:"))
	if Marks>=70 and Marks<=100:
		  print("Grade of Student:",Name,"with ID:",ID,"is A")
	elif Marks>=50 and Marks<70:
		  print("Grade of Student:",Name,"with ID:",ID,"is B")
	elif Marks>=40 and Marks<50:
		  print("Grade of Student:",Name,"with ID:",ID,"is C")
	else:
		  print("Fail")

		  
>>> Student_Grade()
		  
Enter Student Name:Anusha
Enter Student ID:23124
Enter Student Marks:92
Grade of Student: Anusha with ID: 23124 is A
>>> 
