import numpy as np  
import matplotlib.pyplot as plt
import re 

def graph(formula, minx=None, maxx=None):
	if minx is None and maxx is None:
		minx = -10
		maxx = 11
	elif not minx is None and maxx is None:
		minx = int(minx)
		maxx = minx + 21
	elif minx is None and not maxx is None:
		maxx = int(maxx)
		minx = maxx - 21
	formula = re.sub(r"(\))([a-zA-Z]|[0-9])", r"\1*\2", formula)
	formula = re.sub(r"([0-9])([a-zA-Z])", r"\1*\2", formula)
	formula = formula.replace("^", "**") 
	x = np.array(range(minx, maxx))
	y = eval(formula)
	plt.plot(x, y)  
	plt.show()
	
def help():
	print("graph.graph(<equation>, [minx=<minx>], [maxx=<maxx>])")
	print()
	print("equation - The equation that you want to graph. Example: (5x^2)2x+3")
	print("minx - Optional argument to specify the graph\'s minimum X value")
	print("maxx - Optional argument to specify the graph\'s maximum X value")
	print("Example: graph.graph(\"(2x^2)+3\", minx=30)")
