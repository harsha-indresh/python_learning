Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> marks=[67,98,43,56,89,84,72]
>>> eligible_marks=list(lambda x: x>=70,marks)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    eligible_marks=list(lambda x: x>=70,marks)
TypeError: list() takes at most 1 argument (2 given)
>>> marks=[67,98,43,56,89,84,72]
>>> eligible_marks=list(lambda x: x>=70,marks)
SyntaxError: multiple statements found while compiling a single statement
>>> marks=[67,98,43,56,89,84,72]
>>> eligible_marks=list(filter(lambda x: x>=70,marks))
>>> print("eligible marks=",eligible_marks())
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("eligible marks=",eligible_marks())
TypeError: 'list' object is not callable
>>> print("eligible marks=",eligible_marks)
eligible marks= [98, 89, 84, 72]
>>> 
>>> 
>>> 
>>> """Mulitiples of 5"""
'Mulitiples of 5'
>>> nums=[5,38,45,87,25,15]
>>> muloffive=list(filter(lambda n: n%5==0, nums))
>>> print("Multiples of five=",muloffive)
Multiples of five= [5, 45, 25, 15]
>>> 
