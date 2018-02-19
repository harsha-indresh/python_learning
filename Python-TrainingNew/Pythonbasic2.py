Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> marks=70
>>> if(marks>70 and marks <100)
SyntaxError: invalid syntax
>>> if(marks>70 and marks <100):
	print("Grade is A")
elif(marks>50 and marks <70):
	print("Grade is B")
elif(marks>40 and marks <50):
	print("Grade is C")
else
SyntaxError: invalid syntax
>>> >>> if(marks>70 and marks <100):
	print("Grade is A")
elif(marks>50 and marks <70):
	print("Grade is B")
elif(marks>40 and marks <50):
	print("Grade is C")
else:
	
SyntaxError: invalid syntax
>>> if(marks>70 and marks <100):
	print("Grade is A")
elif(marks>50 and marks <70):
	print("Grade is B")
elif(marks>40 and marks <50):
	print("Grade is C")
else:
	print("fail")

	
fail
>>> marks=75
>>> if(marks>70 and marks <100):
	print("Grade is A")
elif(marks>50 and marks <70):
	print("Grade is B")
elif(marks>40 and marks <50):
	print("Grade is C")
else:
	print("fail")

	
Grade is A
>>> #Membership Operators
>>> list=[45,76,93]
>>> a=76
>>> if(a in list):
	print("Available")
else:
	print("not available")

	
Available
>>> #Dictionary
>>> empdetails={'name':'Harsha','id':310231234,'dept':'devops'}
>>> print empdetails.keys()
SyntaxError: invalid syntax
>>> empdetails
{'name': 'Harsha', 'id': 310231234, 'dept': 'devops'}
>>> empdetails.keys()
dict_keys(['name', 'id', 'dept'])
>>> print empdetails.keys()
SyntaxError: invalid syntax
>>> data=dict(province="Ontario",capital="Toranto")
>>> data
{'province': 'Ontario', 'capital': 'Toranto'}
>>> print("The capital of {province} is {capital}".format(**data))
The capital of Ontario is Toranto
>>> data=dict(name="Priya",age=56)
>>> data
{'name': 'Priya', 'age': 56}
>>> 
>>> print("Age of {name} is {age}")
Age of {name} is {age}
>>> print("Age of {name} is {age}".format(**data))
Age of Priya is 56
>>> 
>>> 
>>> a=78
>>> b=93
>>> id(a)
505534720
>>> id(b)
505534960
>>> a=3
>>> b=3
>>> id(a)
505533520
>>> id(b)
505533520
>>> if(a is b):
	print("Identical")
else:
	print("Not Identical")

	
Identical
>>> if(a is not b):
	print("Not Identical")
else:
	print("Identical")

	
Identical
>>> capital_country={"Karnataka":"Bengaluru","TamilNadu":"Chennai"}
>>> for c in caital_country:
	print("{country}:{capital}".format(country=c,capital=capital_country[c]))

	
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    for c in caital_country:
NameError: name 'caital_country' is not defined
>>> for c in capital_country:
	print("{country}:{capital}".format(country=c,capital=capital_country[c]))

	
Karnataka:Bengaluru
TamilNadu:Chennai
>>> 
