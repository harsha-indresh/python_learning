Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> """Renaming a Namespace"""
'Renaming a Namespace'
>>> import math as mathematics
>>> print(mathematics.sin(mathematics.pi))
1.2246467991473532e-16
>>> """ same can be done for functions"""
' same can be done for functions'
>>> 
>>> 
>>> """Time Library"""
'Time Library'
>>> import time
>>> tics=time.time()
>>> print("Number of tics since 12 AM, january 1,1970:", tics)
Number of tics since 12 AM, january 1,1970: 1518747586.6113334
>>> print(time.localtime())
time.struct_time(tm_year=2018, tm_mon=2, tm_mday=16, tm_hour=7, tm_min=51, tm_sec=38, tm_wday=4, tm_yday=47, tm_isdst=0)
>>> localtime=time.asctime(time.localtime(time.time()))
>>> print("Formatted current local time is:",localtime)
Formatted current local time is: Fri Feb 16 07:52:36 2018
>>> """Calender Library"""
'Calender Library'
>>> import calender
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
>>> import calendar
>>> cal=calendar.month(2017,1)
>>> print(cal)
    January 2017
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

>>> 
