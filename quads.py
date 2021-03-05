from systemPlugins.core import *
from math import *

#Quadratic Word Problems
def quadWord(a, b, c):
	a = int(a)
	b = int(b)
	c = int(c)
	upsideDown = False
	if a < 0:
		upsideDown = True
	yInt = "(0, " + str(c) + ")"
	negB = "-" + str(b)
	if negB[0] == "-" and negB[1] == "-":
		negB = negB.replace("--", "")
	negB = int(negB)
	doublea = a * 2
	aOs = float((negB)/doublea)
	first = (a * (aOs ** 2))
	second = int(b * aOs)
	equ = str(first) + "+" + str(second) + "+" + str(c)
	equ = equ.replace("+-", "-").replace("-+", "-")
	equ = eval(equ)
	vertex = "(" + str(aOs) + ", " + str(equ) + ")"
	print("")
	print(theme["styles"]["output"] + "Vertex: " + str(vertex))
	print("AOS: " + str(aOs))
	print("Y-Int: " + str(yInt))
	if upsideDown == True:
		print("Parabola is Upside Down")
	print("")

	#Show Work
	print(theme["styles"]["important"] + "Work:")
	equStr = str(a) + "*" + str(aOs) + "^2+" + str(b) + "*" + str(aOs) + "+" + str(c)
	equStr = equStr.replace("+-", "-").replace("-+", "-")
	print(theme["styles"]["output"] + equStr)
	equBefore = str(first) + "+" + str(second) + "+" + str(c)
	equBefore = equBefore.replace("+-", "-").replace("-+", "-")
	print(equBefore)
	print(equ)
	print("")
	print(str(negB) + "/2(" + str(a) + ")")
	print(aOs)

def help():
	print(theme["styles"]["output"] + "quadWord(a_value, b_value, c_value) - Find Parabolla from Quadratic Equation")