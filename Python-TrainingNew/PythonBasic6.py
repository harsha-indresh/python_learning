Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def Student_Grade():
	count=0
	while(count<=1):
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
		count=count+1

		
>>> Student_Grade()
Enter Student Name:Anusha
Enter Student ID:1
Enter Student Marks:46
Grade of Student: Anusha with ID: 1 is C
Enter Student Name:Pooja
Enter Student ID:2
Enter Student Marks:78
Grade of Student: Pooja with ID: 2 is A
>>> 
>>> """Recurring function"""
'Recurring function'
>>> def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

	
>>> factorial(3)
6
>>> factorial(1)
1
>>> def fact(n):
	print("Factorial for:",n)
	if n==1
	
SyntaxError: invalid syntax
>>> def fact(n):
	print("Factorial for:",n)
	if n==1:
		return 1
	else:
		result=n*fact(n-1)
		print("factorial of", n,"=", result)
		return result

	
>>> fact(4)
Factorial for: 4
Factorial for: 3
Factorial for: 2
Factorial for: 1
factorial of 2 = 2
factorial of 3 = 6
factorial of 4 = 24
24
>>> """functions can be used for incrementing list"""
'functions can be used for incrementing list'
>>> fruits=['Apple','Mango','Banana']
def funct(fruits):
	
SyntaxError: multiple statements found while compiling a single statement
>>> fruits=['Apple','Mango','Banana']
	def funct(fruits):
		
SyntaxError: multiple statements found while compiling a single statement
>>> def funct(fruits):
	print("list of fruits:", fruits)
	fruits_inc=fruits+['grapes','oraange']
	print("Incremented list of fruits is: ",fruits_inc)

	
>>> fruits=['Apple','Mango']
>>> funct(fruits)
list of fruits: ['Apple', 'Mango']
Incremented list of fruits is:  ['Apple', 'Mango', 'grapes', 'oraange']
>>> 
>>> 
>>> 
>>> """Decorator or Alias name for Function"""
'Decorator or Alias name for Function'
>>> def dec(n)
SyntaxError: invalid syntax
>>> def dec(n):
	return n+1

>>> n=3
>>> decorator=dec
>>> decorator(4)
5
>>> dec(4)
5
>>> del dec
>>> dec(3)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    dec(3)
NameError: name 'dec' is not defined
>>> decorator(3)
4
>>> 
