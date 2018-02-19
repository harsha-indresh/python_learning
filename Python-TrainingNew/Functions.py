Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=['abc','sdd','dfhj']
>>> type(a)
<class 'list'>
>>> def Fahranit(Convert-To-Celcius):
	
SyntaxError: invalid syntax
>>> def Fahranit(Convert_To_Celcius):
	return(Convert_To_Celcius*9/5)+32

>>> for t in (23,6,32.5,26.8,23.5)
SyntaxError: invalid syntax
>>> for t in (23,6,32.5,26.8,23.5):
	print(t,":",Faharanit(t))

	
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    print(t,":",Faharanit(t))
NameError: name 'Faharanit' is not defined
>>> for t in (23,6,32.5,26.8,23.5):
	print(t,":",Fahranit(t))

	
23 : 73.4
6 : 42.8
32.5 : 90.5
26.8 : 80.24000000000001
23.5 : 74.3
>>> Faharanit(34)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Faharanit(34)
NameError: name 'Faharanit' is not defined
>>> Fahranit(23)
73.4
>>> ########################################################
>>> 
>>> def Average(num1,num2,num3):
	return((num1+num2+num3)/3)

>>> Average(2,4,6)
4.0
>>> def net_amount(cost)
SyntaxError: invalid syntax
>>> def net_amount(cost):
	return(cost-(cost*0.5))

>>> net_amount(64)
32.0
>>> def Message(string="EveryOne"):
	print("GoodMorning"+" "+string)

	
>>> Message()
GoodMorning EveryOne
>>> Message("People")
GoodMorning People
>>> C=input("Enter the cost value:")
Enter the cost value:79
>>> def Discount(c,Discount=0.5)
SyntaxError: invalid syntax
>>> def Discount(c,Discount=0.5):
	return(c-(c*Discount))

>>> Discount()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    Discount()
TypeError: Discount() missing 1 required positional argument: 'c'
>>> def Discount(c,Discount=0.5):
	cst=input("Enter the cost value:")
	return(c-(c*Discount))

>>> Discount()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Discount()
TypeError: Discount() missing 1 required positional argument: 'c'
>>> def Discount(cst,Discount=0.5):
	cst=input("Enter the cost value:")
	return(cst-(cst*Discount))

>>> Discount()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    Discount()
TypeError: Discount() missing 1 required positional argument: 'cst'
>>> def Discount(Discount=0.5):
	cst=input("Enter the cost value:")
	return(cst-(cst*Discount))

>>> Discount()
Enter the cost value:67
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    Discount()
  File "<pyshell#43>", line 3, in Discount
    return(cst-(cst*Discount))
TypeError: can't multiply sequence by non-int of type 'float'
>>> 
def Discount(c,disc=0.5):
	return(c-(c*disc))

>>> Discount(56)
28.0
>>> Discount(79,0.8)
15.799999999999997
>>> def Discount(disc=0.5):
	cst=input("Enter the cost value:")
	return(cst-(cst*disc))

>>> Discount()
Enter the cost value:68
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    Discount()
  File "<pyshell#51>", line 3, in Discount
    return(cst-(cst*disc))
TypeError: can't multiply sequence by non-int of type 'float'
>>> def Discount(disc=0.5):
	cst=int(input("Enter the cost value:"))
	return(cst-(cst*disc))

>>> Discount()
Enter the cost value:87
43.5
>>> def Full_Name(First_Nmae,Last_Name)
SyntaxError: invalid syntax
>>> def Full_Name(First_Nmae,Last_Name):
	return(First_Nmae+Last_Name)

>>> def Full_Name(First_Nmae,Last_Name):
	print("Full Name of new employee is:", Full_Name+Last_Name)

	
>>> Full_Name("Harsha","Indresh")
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    Full_Name("Harsha","Indresh")
  File "<pyshell#61>", line 2, in Full_Name
    print("Full Name of new employee is:", Full_Name+Last_Name)
TypeError: unsupported operand type(s) for +: 'function' and 'str'
>>> def Full_Name(First_Nmae,Last_Name):
	print("Full Name of new employee is:", First_Name+Last_Name)

	
>>> Full_Name("Harsha","Indresh")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    Full_Name("Harsha","Indresh")
  File "<pyshell#64>", line 2, in Full_Name
    print("Full Name of new employee is:", First_Name+Last_Name)
NameError: name 'First_Name' is not defined
>>> 
def Full_Name(First_Name,Last_Name):
	print("Full Name of new employee is:", First_Name+Last_Name)

	
>>> Full_Name("Harsha","Indresh")
Full Name of new employee is: HarshaIndresh
>>> def Math_Op():
	a=int(input("Enter first number:"))
	b=int(input("Enter second value:"))
	Print("Addition of two values=",a+b)
	Print("Subtraction of two values=",a-b)
	Print("Multiplication of two values=",a*b)
	Print("Division of two values=",a/b)

	
>>> Math_Op()
Enter first number:2
Enter second value:4
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    Math_Op()
  File "<pyshell#78>", line 4, in Math_Op
    Print("Addition of two values=",a+b)
NameError: name 'Print' is not defined
>>> def Math_Op():
	a=int(input("Enter first number:"))
	b=int(input("Enter second value:"))
	print("Addition of two values=",a+b)
	print("Subtraction of two values=",a-b)
	print("Multiplication of two values=",a*b)
	print("Division of two values=",a/b)

	
>>> Math_Op()
Enter first number:3
Enter second value:6
Addition of two values= 9
Subtraction of two values= -3
Multiplication of two values= 18
Division of two values= 0.5
>>> 
