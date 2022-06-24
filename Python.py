"""
Name: pi.py
Purpose: Get the value of Pi to n number of decimal places
Author: Pradipta (geekpradd)
Changes: CyberRangers
Algorithm: Chudnovsky Algorithm
License: MIT
Module Dependencies:
Math provides fast square rooting
Decimal gives the Decimal data type which is much better than Float
sys is needed to set the depth for recursion.
"""#line:12
from __future__ import print_function #line:13
import math ,sys #line:14
from decimal import *#line:15
getcontext ().rounding =ROUND_FLOOR #line:16
sys .setrecursionlimit (100000 )#line:17
python2 =sys .version_info [0 ]==2 #line:19
if python2 :#line:20
	input =raw_input #line:21
def factorial (O0O00000OOO00O0O0 ):#line:23
	"""
	Return the Factorial of a number using recursion
	Parameters:
	n -- Number to get factorial of
	"""#line:28
	if not O0O00000OOO00O0O0 :#line:29
		return 1 #line:30
	return O0O00000OOO00O0O0 *factorial (O0O00000OOO00O0O0 -1 )#line:31
def getIteratedValue (OOOO00O0OOO0OO0OO ):#line:34
	"""
	Return the Iterations as given in the Chudnovsky Algorithm.
	k iterations gives k-1 decimal places.. =>
	Since we need k decimal places
	make iterations equal to k+1
	
	Parameters:
	k  -- Number of Decimal Digits to get
	"""#line:43
	OOOO00O0OOO0OO0OO =OOOO00O0OOO0OO0OO +1 #line:44
	getcontext ().prec =OOOO00O0OOO0OO0OO #line:45
	OO0O0OOO0OO0OO000 =0 #line:46
	print (OOOO00O0OOO0OO0OO )#line:47
	for OOOO00O0OOO0OO0OO in range (OOOO00O0OOO0OO0OO ):#line:48
		OOOOO0000O00O0O00 =factorial (6 *OOOO00O0OOO0OO0OO )*(13591409 +545140134 *OOOO00O0OOO0OO0OO )#line:49
		O0OOO000OO000O000 =factorial (3 *OOOO00O0OOO0OO0OO )*(factorial (OOOO00O0OOO0OO0OO ))**3 *(640320 **(3 *OOOO00O0OOO0OO0OO ))#line:50
		OO0O0OOO0OO0OO000 +=OOOOO0000O00O0O00 /O0OOO000OO000O000 #line:51
	return Decimal (OO0O0OOO0OO0OO000 )#line:52
def getValueOfPi (OO0O000OOOO0OO0OO ):#line:54
	"""
	Returns the calculated value of Pi using the iterated value of the loop
	and some division as given in the Chudnovsky Algorithm
	Parameters:
	k -- Number of Decimal Digits upto which the value of Pi should be calculated
	"""#line:60
	OOO00OOO0O0O0OO00 =getIteratedValue (OO0O000OOOO0OO0OO )#line:61
	OOO000O0OO000OOO0 =426880 *math .sqrt (10005 )#line:62
	OOOOO00OOO00O000O =Decimal (OOO000O0OO000OOO0 )/OOO00OOO0O0O0OO00 #line:63
	return OOOOO00OOO00O000O #line:65
def shell ():#line:67
	"""
	Console Function to create the interactive Shell.
	Runs only when __name__ == __main__ that is when the script is being called directly
	No return value and Parameters
	"""#line:72
	print ("Welcome to Pi Calculator. In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit")#line:73
	while True :#line:75
		print (">>> ",end ='')#line:76
		O000O0OOOO0000000 =input ()#line:77
		if O000O0OOOO0000000 =="quit":#line:78
			break #line:79
		if not O000O0OOOO0000000 .isdigit ():#line:80
			print ("You did not enter a number. How hard can it be to enter a number. Try again!")#line:81
		else :#line:82
			print (getValueOfPi (int (O000O0OOOO0000000 )))#line:83
if __name__ =='__main__':#line:85
	shell ()
