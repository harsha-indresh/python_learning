Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def Ops(a,b,c=0):
	print("sum of three value is:", a+b+c)

	
>>> Ops()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Ops()
TypeError: Ops() missing 2 required positional arguments: 'a' and 'b'
>>> def Ops(a,b,c=0)
SyntaxError: invalid syntax
>>> def Ops(a,b,c=0):
	return a+b+c

>>> Ops()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Ops()
TypeError: Ops() missing 2 required positional arguments: 'a' and 'b'
>>> Ops(3,6)
9
>>> Ops(3,6,1)
10
>>> 
>>> 
>>> """Return statement"""
'Return statement'
>>> def Ops(a,b,c):
	sum=a+b+c
	return
Ops(2+3+4)
SyntaxError: invalid syntax
>>> def Ops(a=2,b=3,c=4):
	sum=a+b+c
	return

>>> Ops()
>>> print(Ops())
None
>>> """Passing only return statement will not retun any value in python"""
'Passing only return statement will not retun any value in python'
>>> """Correct way is:"""
'Correct way is:'
>>> def Ops(a=2,b=4,c=5)
SyntaxError: invalid syntax
>>> def Ops(a=2,b=4,c=5):
	return a+b+c

>>> Ops()
11
>>> def Ops(a=3,b=6):
	sum=a+b
	return sum

>>> Ops()
9
>>> """Global and local variables"""
'Global and local variables'
>>> def glob():
	s="perl"
	print(s)

	
>>> s="python"
>>> glob()
perl
>>> 
>>> 
>>> def glob2()
SyntaxError: invalid syntax
>>> def glob2():
	global s
	print(s)
	s="Mango"
	print(s)

	
>>> s="Apple"
>>> glob2()
Apple
Mango
>>> 
>>> 
>>> """Orbitrary parameters"""
'Orbitrary parameters'
>>> def arithematic_mean(first,*values):
	return (first+sum(values))/(1+len(values))

>>> arithematic_mean(23,83,45,93,26)
54.0
>>> a=[2,3,4,6]
>>> arithematic_mean(*a)
3.75
>>> """Transposing the list"""
'Transposing the list'
>>> myList=[(a,1),(b,2),(c,3),(d,4)]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    myList=[(a,1),(b,2),(c,3),(d,4)]
NameError: name 'b' is not defined
>>> myList=[('a',1),('b',2),('c',3),('d',4)]
>>> list(zip(*myList))
[('a', 'b', 'c', 'd'), (1, 2, 3, 4)]
>>> 
>>> def a(**Hello)
SyntaxError: invalid syntax
>>> def a(**Hello):
	print(Hello)

	
>>> a(h='hi',r='how are',u='you')
{'h': 'hi', 'r': 'how are', 'u': 'you'}
>>> 
