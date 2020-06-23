from math import *
from plugins.core import *
import os
from update_check import *
import time
from tqdm import tqdm		

#Updater
print("Checking for updates...")
for i in tqdm(range(1)):
	x = isUpToDate(__file__, "https://raw.githubusercontent.com/TabulateJarl8/calcplugins/master/formulas/flib.py")
if x == False:
	x = input(theme["styles"]["important"] + "Update? [Y/n] " + theme["styles"]["normal"])
	if x.lower() != 'n':
		print(theme["styles"]["output"] + "Updating flib...")
		os.chdir("plugins")
			
		update(__file__, "https://raw.githubusercontent.com/TabulateJarl8/calcplugins/master/formulas/flib.py")
		os.chdir("..")
		print("")
		print(theme["styles"]["important"] + "flib Updated. Please Restart the Calculator." + theme["styles"]["normal"])
		time.sleep(2)
			
def quadForm(a, b, c):
    negB = b * -1
    bSqu = b ** 2
    second = 4 * a * c
    top = bSqu - second
    doubleA = a * 2
    top = reduced_sqrt(top)
    #print("")
    if (str(top).isalnum()) == False:
        topStr = str(negB) + "\u00B1" + str(top)
        i = 0
        while i < 5 - len(topStr):
            topStr = " " + topStr
            i+=1
        print(theme["styles"]["answer"] + topStr.center(8))
        
        print("\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014")
        i = 0
        doubleA = str(doubleA)
        while i < 5 - len(doubleA):
            doubleA = " " + doubleA
            i+=1
        print(doubleA.center(8))
    else:
        plus = int(negB) + int(top)
        plus = plus / (2*a)
        minus = int(negB) - int(top)
        minus = minus / (2*a)
        print(theme["styles"]["answer"] + "x = " + str(plus))
        print("x = " + str(minus))
    
def perfect_square(limit):  
    accumulation_list = [1]
    index, increment = 0, 3
    while accumulation_list[-1] + increment <= limit:
        accumulation_list.append(accumulation_list[index] + increment)
        index += 1 
        increment = 2 * index + 3
    return accumulation_list


def reduced_sqrt(n):
    """Print most reduced form of square root of n"""
    if n < 0:
        print('Negative input')
        return

    if sqrt(n).is_integer():
        #print(int(sqrt(n)))
        return n

    # Find perfect squares that are factors of n
    factors = [square for square in perfect_square(n/2) if n % square == 0 and square > 1]
    if len(factors) == 0:
        #print("\u221A" + str(n))
        return('\u221A' + str(n)) # Square root is irreducible
    else:
        a = int(sqrt(max(factors))) # Coefficient
        b = int(n / max(factors)) # Argument of the square root
        return(str(a) + '\u221A' + str(b)) # Reduced square root
		
