Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def temp(t):
	def celtofar(x):
		return 9*x/5+32
	
	result="Current temperature is"+str(celtofar(t))
	return result

>>> temp(40)
'Current temperature is104.0'
>>> 
>>> 
>>> """Lambda Expression"""
'Lambda Expression'
>>> sum=lambda x,y:x+y
>>> print(sum(3,3))
6
>>> celtofar=lambda t:9*t/5+32
>>> lambda(68)
SyntaxError: invalid syntax
>>> celtofar=lambda t:9*t/5+32
>>> celtofar(68)
154.4
>>> 
>>> def sum(a,b):
	return a+b

>>> def Mul(c,d):
	return c*d

>>> def far(t):
	return ((float(9)/5*t+32))

>>> def cel(t):
	return ((float(5)/9*t-32))

>>> temp=[45.6,67,23.6,7]
>>> F=map(far,temp)
>>> C=map(cel,F)
>>> temp_in_Far=list(map(far,temp))
>>> temp_in_Cel=list(map(cel,temp_in_Far))
>>> print(tem_in_Far)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(tem_in_Far)
NameError: name 'tem_in_Far' is not defined
>>> print(temp_in_Far)
[114.08, 152.60000000000002, 74.48, 44.6]
>>> print(temp_in_Cel)
[31.37777777777778, 52.7777777777778, 9.37777777777778, -7.222222222222221]
>>> 
>>> values=[23,45.6,23.6,34]
>>> F=list(map(lambda x: (float(9)/5)*x+32,values))
>>> print(F)
[73.4, 114.08, 74.48, 93.2]
>>> C=list(map(lambda x: (float(9)/5)*x+32,F))
>>> print(C)
[164.12, 237.344, 166.06400000000002, 199.76000000000002]
>>> def far(t):
	return ((float(9)/5*t+32))
def cel(t):
	return ((float(5)/9*t-32))
SyntaxError: invalid syntax
>>> def cel(t):
	return ((float(5)/9*t-32))

>>> def far(t):
	return ((float(9)/5*t+32))

>>> temp=[45.6,67,23.6,7]
>>> F=map(far,temp)
>>> C=map(cel,F)
>>> temp_in_Far=list(map(far,temp))
>>> 
>>> 
>>> 
>>> def discount(c):
	return (c-(c*0.5))

>>> cost=[68,36,87,45,78]
>>> disc=map(discount,cost)
>>> disc=list(map(discount,cost))
>>> print(disc)
[34.0, 18.0, 43.5, 22.5, 39.0]
>>> 
>>> 
>>> cost=[54,23,65,45]
>>> disc=list(map(lambda c:(c-(c*0.5)),cost))
>>> print(disc)
[27.0, 11.5, 32.5, 22.5]
>>> 
