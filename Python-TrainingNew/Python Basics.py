Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> a=3
>>> print("Value of A is:",a)
Value of A is: 3
>>> print(a)
3
>>> a
3
>>> print("Good Morning",end="")
Good Morning
>>> i/p
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    i/p
NameError: name 'i' is not defined
>>> #i/p
>>> x=input("Enter the value:")
Enter the value:4
>>> x
'4'
>>> 
>>> #Memory management
>>> #And garbage collection
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x=5
>>> del a,3
SyntaxError: can't delete literal
>>> y=6
>>> del x,y
>>> y
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> x
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> 5 Data types
SyntaxError: invalid syntax
>>> #5Data type
>>> #1.Numbers
>>> b=7
>>> c=34.56
>>> d=23483478
>>> e=3+5j
>>> a+c
37.56
>>> c+e
(37.56+5j)
>>> #String
>>> str="Hello"
>>> str
'Hello'
>>> str[0]
'H'
>>> str[2:3]
'l'
>>> str[3:]
'lo'
>>> str*3
'HelloHelloHello'
>>> str+Harsha
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    str+Harsha
NameError: name 'Harsha' is not defined
>>> str+"Harsha"
'HelloHarsha'
>>> #List
>>> a=[2,'Hi',3.4,6]
>>> b=[3,8,'Hello']
>>> a[0]
2
>>> a[2:4]
[3.4, 6]
>>> a+b
[2, 'Hi', 3.4, 6, 3, 8, 'Hello']
>>> tuple1=('efh',287)

