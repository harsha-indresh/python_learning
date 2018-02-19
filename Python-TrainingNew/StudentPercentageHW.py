Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def percentage(marks_obtained):
	total_marks=600
	return((marks_obtained/total_marks)*100)

>>> for s in(467,543,356,587,434):
	for n in("Harsha","Anush","Prasad","Chandra","Nelson"):
		print("Percentage of student",n,"is:",percentage(s))

		
Percentage of student Harsha is: 77.83333333333333
Percentage of student Anush is: 77.83333333333333
Percentage of student Prasad is: 77.83333333333333
Percentage of student Chandra is: 77.83333333333333
Percentage of student Nelson is: 77.83333333333333
Percentage of student Harsha is: 90.5
Percentage of student Anush is: 90.5
Percentage of student Prasad is: 90.5
Percentage of student Chandra is: 90.5
Percentage of student Nelson is: 90.5
Percentage of student Harsha is: 59.333333333333336
Percentage of student Anush is: 59.333333333333336
Percentage of student Prasad is: 59.333333333333336
Percentage of student Chandra is: 59.333333333333336
Percentage of student Nelson is: 59.333333333333336
Percentage of student Harsha is: 97.83333333333334
Percentage of student Anush is: 97.83333333333334
Percentage of student Prasad is: 97.83333333333334
Percentage of student Chandra is: 97.83333333333334
Percentage of student Nelson is: 97.83333333333334
Percentage of student Harsha is: 72.33333333333334
Percentage of student Anush is: 72.33333333333334
Percentage of student Prasad is: 72.33333333333334
Percentage of student Chandra is: 72.33333333333334
Percentage of student Nelson is: 72.33333333333334
>>> for s in(467,543,356,587,434):
	for n in("Harsha","Anush","Prasad","Chandra","Nelson"):
print("Percentage of student",n,"is:",percentage(s))
SyntaxError: expected an indented block
>>> for s in(467,543,356,587,434):
	for n in("Harsha","Anush","Prasad","Chandra","Nelson"):
	print("Percentage of student",n,"is:",percentage(s))
	
SyntaxError: expected an indented block
>>> for s in(467,543,356,587,434):
for n in("Harsha","Anush","Prasad","Chandra","Nelson"):
	print("Percentage of student",n,"is:",percentage(s))
	
SyntaxError: expected an indented block
>>> for s in(467,543,356,587,434):
    for n in("Harsha","Anush","Prasad","Chandra","Nelson"):
	print("Percentage of student",n,"is:",percentage(s))
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
