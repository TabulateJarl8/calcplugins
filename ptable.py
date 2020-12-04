import sys
from systemPlugins.core import theme, configPath
from configparser import ConfigParser
from dialog import Dialog

elements = {
	"h": {"mass": 1.00784, "number": 1, "name": "hydrogen", "melting": -259.1},
	"he": {"mass": 4.002602, "number": 2, "name": "helium", "melting": None},
	"li": {"mass": 6.94, "number": 3, "name": "lithium", "melting": 180.54},
	"be": {"mass": 9.012183, "number": 4, "name": "beryllium", "melting": 1287},
	"b": {"mass": 10.81, "number": 5, "name": "boron", "melting": 2075},
	"c": {"mass": 12.011, "number": 6, "name": "carbon", "melting": 3550},
	"n": {"mass": 14.007, "number": 7, "name": "nitrogen", "melting": -210.1},
	"o": {"mass": 15.999, "number": 8, "name": "oxygen", "melting": -218},
	"f": {"mass": 18.99840, "number": 9, "name": "fluorine", "melting": -220},
	"ne": {"mass": 20.1797, "number": 10, "name": "neon", "melting": -248.6},
	"na": {"mass": 22.98977, "number": 11, "name": "sodium", "melting": 97.720},
	"mg": {"mass": 24.305, "number": 12, "name": "magnesium", "melting": 650},
	"al": {"mass": 26.98154, "number": 13, "name": "aluminium", "melting": 660.32},
	"si": {"mass": 28.085, "number": 14, "name": "silicon", "melting": 1414},
	"p": {"mass": 30.97376, "number": 15, "name": "phosphorus", "melting": 44.15},
	"s": {"mass": 32.06, "number": 16, "name": "sulfur", "melting": 115.21},
	"cl": {"mass": 35.45, "number": 17, "name": "chlorine", "melting": -101.5},
	"ar": {"mass": 39.948, "number": 18, "name": "argon", "melting": -189},
	"k": {"mass": 39.0983, "number": 19, "name": "potassium", "melting": 63.380},
	"ca": {"mass": 40.078, "number": 20, "name": "calcium", "melting": 841.9},
	"sc": {"mass": 44.95591, "number": 21, "name": "scandium", "melting": 1541},
	"ti": {"mass": 47.867, "number": 22, "name": "titanium", "melting": 1668},
	"v": {"mass": 50.9415, "number": 23, "name": "vanadium", "melting": 1910},
	"cr": {"mass": 51.9961, "number": 24, "name": "chromium", "melting": 1907},
	"mn": {"mass": 54.93804, "number": 25, "name": "manganese", "melting": 1246},
	"fe": {"mass": 55.845, "number": 26, "name": "iron", "melting": 1538},
	"co": {"mass": 58.93319, "number": 27, "name": "cobalt", "melting": 1495},
	"ni": {"mass": 58.6934, "number": 28, "name": "nickel", "melting": 1455},
	"cu": {"mass": 63.546, "number": 29, "name": "copper", "melting": 1084.62},
	"zn": {"mass": 65.38, "number": 30, "name": "zinc", "melting": 419.53},
	"ga": {"mass": 69.723, "number": 31, "name": "gallium", "melting": 29.760},
	"ge": {"mass": 72.63, "number": 32, "name": "germanium", "melting": 938.25},
	"as": {"mass": 74.92160, "number": 33, "name": "arsenic", "melting": 816.9},
	"se": {"mass": 78.971, "number": 34, "name": "selenium", "melting": 221},
	"br": {"mass": 79.904, "number": 35, "name": "bromine", "melting": -7.350},
	"kr": {"mass": 83.798, "number": 36, "name": "krypton", "melting": -157.36},
	"rb": {"mass": 85.4678, "number": 37, "name": "rubidium", "melting": 39.310},
	"sr": {"mass": 87.62, "number": 38, "name": "strontium", "melting": 776.9},
	"y": {"mass": 88.90584, "number": 39, "name": "yttrium", "melting": 1526},
	"zr": {"mass": 91.224, "number": 40, "name": "zirconium", "melting": 1855},
	"nb": {"mass": 92.90637, "number": 41, "name": "niobium", "melting": 2477},
	"mo": {"mass": 95.95, "number": 42, "name": "molybdenum", "melting": 2623},
	"tc": {"mass": 98, "number": 43, "name": "technetium", "melting": 2157},
	"ru": {"mass": 101.07, "number": 44, "name": "ruthenium", "melting": 2334},
	"rh": {"mass": 102.9055, "number": 45, "name": "rhodium", "melting": 1964},
	"pd": {"mass": 106.42, "number": 46, "name": "palladium", "melting": 1554.90},
	"ag": {"mass": 107.8682, "number": 47, "name": "silver", "melting": 961.780},
	"cd": {"mass": 112.414, "number": 48, "name": "cadmium", "melting": 321.07},
	"in": {"mass": 114.818, "number": 49, "name": "indium", "melting": 156.60},
	"sn": {"mass": 118.710, "number": 50, "name": "tin", "melting": 231.93},
	"sb": {"mass": 121.760, "number": 51, "name": "antimony", "melting": 630.63},
	"te": {"mass": 127.60, "number": 52, "name": "tellurium", "melting": 449.51},
	"i": {"mass": 126.9045, "number": 53, "name": "iodine", "melting": 113.70},
	"xe": {"mass": 131.293, "number": 54, "name": "xenon", "melting": -111.8},
	"cs": {"mass": 132.9055, "number": 55, "name": "caesium", "melting": 28.440},
	"ba": {"mass": 137.327, "number": 56, "name": "barium", "melting": 730},
	"la": {"mass": 138.9055, "number": 57, "name": "lanthanum", "melting": 919.9},
	"ce": {"mass": 140.116, "number": 58, "name": "cerium", "melting": 797.9},
	"pr": {"mass": 140.9077, "number": 59, "name": "praseodymium", "melting": 930.9},
	"nd": {"mass": 144.242, "number": 60, "name": "neodymium", "melting": 1021},
	"pm": {"mass": 145, "number": 61, "name": "promethium", "melting": 1100},
	"sm": {"mass": 150.36, "number": 62, "name": "samarium", "melting": 1072},
	"eu": {"mass": 151.964, "number": 63, "name": "europium", "melting": 821.9},
	"gd": {"mass": 157.25, "number": 64, "name": "gadolinium", "melting": 1313},
	"tb": {"mass": 158.9254, "number": 65, "name": "terbium", "melting": 1356},
	"dy": {"mass": 162.500, "number": 66, "name": "dysprosium", "melting": 1412},
	"ho": {"mass": 164.9303, "number": 67, "name": "holmium", "melting": 1474},
	"er": {"mass": 167.259, "number": 68, "name": "erbium", "melting": 1497},
	"tm": {"mass": 168.9342, "number": 69, "name": "thulium", "melting": 1545},
	"yb": {"mass": 173.045, "number": 70, "name": "ytterbium", "melting": 818.9},
	"lu": {"mass": 174.9668, "number": 71, "name": "lutetium", "melting": 1663},
	"hf": {"mass": 178.486, "number": 72, "name": "hafnium", "melting": 2233},
	"ta": {"mass": 180.9479, "number": 73, "name": "tantalum", "melting": 3017},
	"w": {"mass": 183.84, "number": 74, "name": "tungsten", "melting": 3422},
	"re": {"mass": 186.207, "number": 75, "name": "rhenium", "melting": 3186},
	"os": {"mass": 190.23, "number": 76, "name": "osmium", "melting": 3033},
	"ir": {"mass": 192.217, "number": 77, "name": "iridium", "melting": 2466},
	"pt": {"mass": 195.084, "number": 78, "name": "platinum", "melting": 1768.3},
	"au": {"mass": 196.9666, "number": 79, "name": "gold", "melting": 1064.18},
	"hg": {"mass": 200.59, "number": 80, "name": "mercury", "melting": -38.830},
	"tl": {"mass": 204.38, "number": 81, "name": "thallium", "melting": 304},
	"pb": {"mass": 207.2, "number": 82, "name": "lead", "melting": 327.46},
	"bi": {"mass": 208.9804, "number": 83, "name": "bismuth", "melting": 271.3},
	"po": {"mass": 209, "number": 84, "name": "polonium", "melting": 255},
	"at": {"mass": 210, "number": 85, "name": "astatine", "melting": 302},
	"rn": {"mass": 222, "number": 86, "name": "radon", "melting": -71.1},
	"fr": {"mass": 223, "number": 87, "name": "francium", "melting": 20.9},
	"ra": {"mass": 226, "number": 88, "name": "radium", "melting": 700},
	"ac": {"mass": 227, "number": 89, "name": "actinium", "melting": 1050},
	"th": {"mass": 232.0377, "number": 90, "name": "thorium", "melting": 1750},
	"pa": {"mass": 231.0359, "number": 91, "name": "protactinium", "melting": 1572},
	"u": {"mass": 238.0289, "number": 92, "name": "uranium", "melting": 1135},
	"np": {"mass": 237, "number": 93, "name": "neptunium", "melting": 644},
	"pu": {"mass": 244, "number": 94, "name": "plutonium", "melting": 640},
	"am": {"mass": 243, "number": 95, "name": "americium", "melting": 1176},
	"cm": {"mass": 247, "number": 96, "name": "curium", "melting": 1345},
	"bk": {"mass": 247, "number": 97, "name": "berkelium", "melting": 1050},
	"cf": {"mass": 251, "number": 98, "name": "californium", "melting": 899.9},
	"es": {"mass": 252, "number": 99, "name": "einsteinium", "melting": 859.9},
	"fm": {"mass": 257, "number": 100, "name": "fermium", "melting": 1500},
	"md": {"mass": 258, "number": 101, "name": "mendelevium", "melting": 830},
	"no": {"mass": 259, "number": 102, "name": "nobelium", "melting": 830},
	"lr": {"mass": 266, "number": 103, "name": "lawrencium", "melting": 1600},
	"rf": {"mass": 267, "number": 104, "name": "rutherfordium", "melting": None},
	"db": {"mass": 268, "number": 105, "name": "dubnium", "melting": None},
	"sg": {"mass": 269, "number": 106, "name": "seaborgium", "melting": None},
	"bh": {"mass": 270, "number": 107, "name": "bohrium", "melting": None},
	"hs": {"mass": 270, "number": 108, "name": "hassium", "melting": None},
	"mt": {"mass": 278, "number": 109, "name": "meitnerium", "melting": None},
	"ds": {"mass": 281, "number": 110, "name": "darmstadtium", "melting": None},
	"rg": {"mass": 282, "number": 111, "name": "roentgenium", "melting": None},
	"cn": {"mass": 285, "number": 112, "name": "copernicium", "melting": None},
	"nh": {"mass": 286, "number": 113, "name": "nihonium", "melting": None},
	"fl": {"mass": 289, "number": 114, "name": "flerovium", "melting": None},
	"mc": {"mass": 290, "number": 115, "name": "moscovium", "melting": None},
	"lv": {"mass": 293, "number": 116, "name": "livermorium", "melting": None},
	"ts": {"mass": 294, "number": 117, "name": "tennessine", "melting": None},
	"og": {"mass": 294, "number": 118, "name": "oganesson", "melting": None}

}

class settings:
	choices = [("Datatype for ptable", "Change the datatype for ptable")]
	def settingsPopup(tag, config):
		d = Dialog()
		if tag == "Datatype for ptable":
			datatype = d.menu("Datatype for ptable", choices=[("Mass", "Atomic Mass"), ("Number", "Atomic Number"), ("Melting", "Element\'s melting point")])
			if datatype[0] == d.OK:
				config["ptable"]["variableType"] = datatype[1].lower()
		return config

def main():
	config = ConfigParser()
	config.read(configPath)
	if not config.has_section("ptable"):
		config.add_section("ptable")
		config["ptable"]["variableType"] = "mass"
		with open(configPath, "w") as configFile:
			config.write(configFile)
	if not config["ptable"]["variableType"] in elements["h"]:
		input("ptable: Invalid datatype in config: \'" + config["ptable"]["variableType"] + "\'. Restoring to \'mass\'")
		config["ptable"]["variableType"] = "mass"
		with open(configPath, "w") as configFile:
			config.write(configFile)
	#Init variables with mass on start
	for element in elements:
		vars(sys.modules[__name__])[element] = elements[element][config["ptable"]["variableType"]]
		vars(sys.modules[__name__])[elements[element]["name"]] = elements[element][config["ptable"]["variableType"]]

def setElementVars(type):
	config = ConfigParser()
	config.read(configPath)
	if str(type) in elements["h"]:
		config["ptable"]["variableType"] = str(type)
		with open(configPath, "w") as configFile:
			config.write(configFile)
		for element in elements:
			vars(sys.modules[__name__])[element] = elements[element][str(type)]
			vars(sys.modules[__name__])[elements[element]["name"]] = elements[element][str(type)]
	else:
		print(theme["styles"]["error"] + "Invalid datatype: \'" + str(type) + "\'")

def currentDataType():
	config = ConfigParser()
	config.read(configPath)
	print(config["ptable"]["variableType"])

def onSettingsSaved():
	config = ConfigParser()
	config.read(configPath)
	if config["ptable"]["variableType"] in elements["h"]:
		for element in elements:
			vars(sys.modules[__name__])[element] = elements[element][config["ptable"]["variableType"]]
			vars(sys.modules[__name__])[elements[element]["name"]] = elements[element][config["ptable"]["variableType"]]

def help():
	print("ptable.setElementVars(<\"mass\"|\"number\"|\"melting\">) - Set a variable with the corresponding element symbol for every element containing the specified data")
	print("Access these variables with ptable.[symbol] or ptable.[name]. For example, ptable.h would return hydrogen and ptable.zinc would return zinc")
	print()
	print("ptable.currentDataType() - Prints the current datatype, like mass or melting")

main()
