import re
from system.systemPlugins.core import *

def absGraph(x, y, slope, upsidedown=False):
	equ = "y="
	if upsidedown == True:
		equ = equ + "-"
	equ = equ + str(slope) + "|x-" + str(x) + "|+" + str(y)
	equ = re.sub("\--", "+", equ)
	equ = re.sub("\+-|\-+", "-", equ)
	equ = re.sub("\-0", "", equ)
	equ = re.sub("\+0", "", equ)
	if equ[2] == "1":
		equ = equ.replace("1", "", 1)
	print(equ)
def help():
	print(theme["styles"]["output"] + "ABSGraph Help")
	print("")
	print(theme["styles"]["output"] + "Syntax")
	print(theme["styles"]["output"] + "absGraph(Vertex X, Vertex Y, Slope, Is Graph Upside Down [True/(False)])")