import numpy as np
import matplotlib.pyplot as plt
import re
from systemPlugins.core import configPath, theme
from configparser import ConfigParser
import os

config = ConfigParser()
config.read(configPath)

def graph(y, axisRange=[-10, 10, -10, 10], title="", points=[], grid=True, numPoints=100, save=False):

	if isinstance(y, str):
		y = [y, 'blue']

	for i in range(0, len(y), 2):
		# Match a number or a function call, followed by a variable or parentheses.
		y[i] = re.sub(r"((?:\d+)|(?:[a-zA-Z]\w*\(\w+\)))((?:[a-zA-Z]\w*)|\()", r"\1*\2", y[i])

		# Repalce ^ with **
		y[i] = y[i].replace("^", "**")

	# Graph settings
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')

	plt.gca().xaxis.get_major_ticks()[5].label1.set_visible(False)

	ax.yaxis.set_ticks_position('left')

	plt.axis(axisRange)

	if grid == True:
		plt.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

	# Generate evenly spaced numbers over a specified interval
	x = np.linspace(axisRange[0], axisRange[1], numPoints)

	for i in range(0, len(y), 2):
		plt.plot(x, eval(y[i]), y[i + 1])

	# Plot points
	for xpnt, ypnt, c in points:
		plt.scatter(xpnt, ypnt, color=c)

	# Metadata for graph
	if title != "" and isinstance(title, str):
		plt.title(title)

	if save == True:
		# Make graphs directory
		if not os.path.exists(os.path.join(config["paths"]["userPath"], "graphs")):
			os.mkdir(os.path.join(config["paths"]["userPath"], "graphs"))

		# Get current filename increment
		i = 0
		while os.path.isfile(os.path.join(config["paths"]["userPath"], "graphs", "graph%s.png" % i)):
			i += 1

		# Save figure
		plt.savefig(os.path.join(config["paths"]["userPath"], "graphs", "graph%s.png" % i))

	# Show graph
	plt.show(block=False)

def help():
	print(theme['styles']['prompt'] + "graph.graph(<equation>, [title], [xLabel], [yLabel], [axisRange=[-10, 10, -10, 10]], [points=[]], grid=True, numPoints=100, save=False)" + theme['styles']['normal'])
	print()
	print(theme['styles']['important'] + "equation" + theme['styles']['normal'] + " - The equation that you want to graph. Example: " + theme['styles']['input'] + "(5x^2)2x+3" + theme['styles']['normal'] + ". Can also be a list in the format of " + theme['styles']['input'] + "[equation, color]" + theme['styles']['normal'] + ". Supports matplotlib color notation, example: " + theme['styles']['input'] + "['3x+2', 'red', '2x+6', 'blue']" + theme['styles']['normal'])
	print(theme['styles']['important'] + "title" + theme['styles']['normal'] + " - Optional title of graph, deafults to nothing")
	print(theme['styles']['important'] + "axisRange" + theme['styles']['normal'] + " - List specifying the minimum and maximum values for your axes, " + theme['styles']['input'] + "[xMin, xMax, yMin, yMax]" + theme['styles']['normal'])
	print(theme['styles']['important'] + "points" + theme['styles']['normal'] + " - List of tuples specifying points to graph, " + theme['styles']['input'] + "[(xVal, yVal, \'color\')]" + theme['styles']['normal'])
	print(theme['styles']['important'] + "grid" + theme['styles']['normal'] + " - Show grid, can be True or False")
	print(theme['styles']['important'] + "numPoints" + theme['styles']['normal'] + " - Number of points on the graph to calculate, larger number may produce more accurate results, but take more processing power")
	print(theme['styles']['important'] + "save" + theme['styles']['normal'] + " - Save graph in `graphs` folder in user directory, can be True or False")
