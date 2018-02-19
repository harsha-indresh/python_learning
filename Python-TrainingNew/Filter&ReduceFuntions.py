Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> numbers=[4,6,3,22,45,32,2]
>>> greater_numbers=list(filter(lambda x: x>10,numbers))
>>> print(greater_numbers)
[22, 45, 32]
>>> 
>>> 
>>> """reduce"""
'reduce'
>>> import functools
>>> functools.reduce(lambda x,y: x+y,[23,12,34,54])
123
>>> 
>>> functools.reduce(lambda a,b: a if(a>b) else b, [1,32,23,45,75])
75
>>> functools.reduce(lambda a,b: a+b, range(1,100))
4950
>>> 
>>> 
>>> functools.reduce(lambda a,b:a*b, range(44,50))/reduce(lambda x,y:x*y, range(1,7))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    functools.reduce(lambda a,b:a*b, range(44,50))/reduce(lambda x,y:x*y, range(1,7))
NameError: name 'reduce' is not defined
>>> functools.reduce(lambda a,b:a*b, range(44,50))/functools.reduce(lambda x,y:x*y, range(1,7))
13983816.0
>>> 
>>> 
>>> """Dir() Function"""
'Dir() Function'
>>> import math
>>> content=dir(math)
>>> print(content)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.pi
3.141592653589793
>>> math.sin(math.pi)
1.2246467991473532e-16
>>> from math import *
>>> sin(3.5)+tan(2.5)+e
1.620476303530765
>>> 
