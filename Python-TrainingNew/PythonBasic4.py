Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> numbers=[23,43,54,65,22,76,56,98]
>>> no=int(input("Enter a number:"))
Enter a number:65
>>> for num in numbers:
    if(num==no):
	print("Number is available")
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for num in numbers:
    if num==no:
       print("Number is available")
       break
    else:
       print("number is not available")

       
number is not available
number is not available
number is not available
Number is available
>>> for num in numbers:
   if num==no:
       print("Number is available")
       break
else:
       print("number is not available")

       
Number is available
>>> #Continue statement
>>> for letter in 'PYTHON':
    if(letter=='T'):
	continue
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for letter in 'PYTHON':
    if letter=='T':
       continue
       print("Current value:",letter)

       
>>> for letter in 'PYTHON':
   if letter == 'T':
       continue
      print("Current value:",letter)
      
SyntaxError: unindent does not match any outer indentation level
>>> for letter in 'PYTHON':
   if letter == 'T':
       continue
   print("Current value:",letter)

   
Current value: P
Current value: Y
Current value: H
Current value: O
Current value: N
>>> var=10
>>> while var>0:
	var=var-1
	if var == 5:
		continue
	print("Current number:")

	
Current number:
Current number:
Current number:
Current number:
Current number:
Current number:
Current number:
Current number:
Current number:
>>> while var>0:
	var=var-1
	if var == 5:
		continue
	print("Current number:",var)

	
>>> while var>0:
	var=var-1
    if var == 5:
	continue
	print("Current number:",var)
	
SyntaxError: unindent does not match any outer indentation level
>>> while var>0:
    var=var-1
   if var == 5:
      continue
      print("Current number:",var)
      
SyntaxError: unindent does not match any outer indentation level
>>> var=10
>>> while var>0:
var=var-1
SyntaxError: expected an indented block
>>> var=10
>>> while var>0:
	var=var-1
	
SyntaxError: multiple statements found while compiling a single statement
>>> while var>0:
  var=var-1
  if var == 5:
     continue
  print("Current number:",var)

  
Current number: 9
Current number: 8
Current number: 7
Current number: 6
Current number: 4
Current number: 3
Current number: 2
Current number: 1
Current number: 0
>>> person=[["Harsha","Indresh"],["29","Bengaluru","India"],"9851468514"]
>>> name=person[0]
>>> name
['Harsha', 'Indresh']
>>> FirstName=person[0][0]
>>> FirstName
'Harsha'
>>> Age=person[1][0]
>>> Age
'29'
>>> 
