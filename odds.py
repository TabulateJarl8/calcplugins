from system.systemPlugins.core import *

def countOdds(startnum, endnum, showNums=False):
	even = []
	odd = []
	i = startnum
	while i <= endnum:
		if (i % 2) == 0:
			even.append(i)
		else:
			odd.append(i)
		i += 1
	print(theme["styles"]["output"] + "There are " + theme["styles"]["important"] + str(len(odd)) + theme["styles"]["output"] + " odds and " + theme["styles"]["important"] + str(len(even)) + theme["styles"]["output"] + " evens")
	if showNums == True:
		print("Odds: ")
		print(odd)
		print("Evens:")
		print(even)
def help():
	print(theme["styles"]["output"] + "Odds Help")
	print("")
	print("Syntax")
	print("countOdds(Start Number, End Number, Show Lists of Numbers [True/(False)])")