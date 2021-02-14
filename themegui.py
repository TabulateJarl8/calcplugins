import tkinter as tk
from tkinter.colorchooser import *
from tkinter import messagebox
import configparser
from systemPlugins.core import themePath, configPath

config = configparser.ConfigParser()
config.read(configPath)

root = tk.Tk()
root.withdraw()
filevar = tk.StringVar()
namevar = tk.StringVar()
descvar = tk.StringVar()

def on_closing():
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.withdraw()
		root.quit()

def toAnsi(rgb, type, bright=False):
	if rgb == None:
		return "\\u001b[0m"
	if type == "fore":
		ansi = "\\u001b[38;2;" + ";".join(rgb)
	elif type == "back":
		ansi = "\\u001b[48;2;" + ";".join(rgb)
	if bright == True:
		ansi += ";1m"
	else:
		ansi += "m"
	return ansi

def toRGB(hexval):
	if hexval == None:
		return None
	# Remove #
	hexval = hexval.replace("#", "")
	# Convert all 3 base 16 hex values to base 10 values (rgb)
	rgb = (str(int(hexval[0:2], 16)), str(int(hexval[2:4], 16)), str(int(hexval[4:6], 16)))
	return rgb

def getColor(title, type):
	return toAnsi(toRGB(askcolor(title=title + ". Press Cancel to leave default")[1]), type)

def makeTheme():
	root.protocol("WM_DELETE_WINDOW", on_closing)
	root.title("Basic Details")
	root.geometry("300x300")
	filel = tk.Label(root, text="Theme File:").grid(row=0, column=0)
	filext = tk.Label(root, text=".iitheme").grid(row=0, column=2)
	filee = tk.Entry(root, textvariable=filevar).grid(row=0, column=1)
	namel = tk.Label(root, text="Theme Name:").grid(row=1, column=0)
	namee = tk.Entry(root, textvariable=namevar).grid(row=1, column=1)
	descl = tk.Label(root, text="Theme Description:").grid(row=2, column=0)
	desce = tk.Entry(root, textvariable=descvar).grid(row=2, column=1)
	subbtn = tk.Button(root, text="Next", command=next).grid(row=3, column=1)
	root.deiconify()
	root.mainloop()

def next():
	openTheme = configparser.ConfigParser()
	openTheme.add_section("theme")
	openTheme.add_section("styles")
	file = filevar.get()
	name = namevar.get()
	desc = descvar.get()
	if file == "" or name == "" or desc == "":
		return
	else:
		root.withdraw()
	if not file.endswith(".iitheme"):
		file += ".iitheme"
	openTheme["theme"]["name"] = name
	openTheme["theme"]["description"] = desc
	openTheme["theme"]["ansi"] = "true"
	Fore = getColor("Normal foreground", "fore")
	Back = getColor("Normal background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["normal"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["normal"] = Back + Fore
	else:
		openTheme["styles"]["normal"] = Fore + Back
	Fore = getColor("Error foreground", "fore")
	Back = getColor("Error background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["error"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["error"] = Back + Fore
	else:
		openTheme["styles"]["error"] = Fore + Back
	Fore = getColor("Warning foreground", "fore")
	Back = getColor("Warning background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["warning"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["warning"] = Back + Fore
	else:
		openTheme["styles"]["warning"] = Fore + Back
	Fore = getColor("Important foreground", "fore")
	Back = getColor("Important background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["important"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["important"] = Back + Fore
	else:
		openTheme["styles"]["important"] = Fore + Back
	Fore = getColor("Startup message foreground", "fore")
	Back = getColor("Startup message background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["startupmessage"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["startupmessage"] = Back + Fore
	else:
		openTheme["styles"]["startupmessage"] = Fore + Back
	Fore = getColor("Prompt foreground", "fore")
	Back = getColor("Prompt background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["prompt"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["prompt"] = Back + Fore
	else:
		openTheme["styles"]["prompt"] = Fore + Back
	Fore = getColor("Link foreground", "fore")
	Back = getColor("Link background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["link"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["link"] = Back + Fore
	else:
		openTheme["styles"]["link"] = Fore + Back
	Fore = getColor("Answer foreground", "fore")
	Back = getColor("Answer background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["answer"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["answer"] = Back + Fore
	else:
		openTheme["styles"]["answer"] = Fore + Back
	Fore = getColor("Input foreground", "fore")
	Back = getColor("Input background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["input"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["input"] = Back + Fore
	else:
		openTheme["styles"]["input"] = Fore + Back
	Fore = getColor("Output foreground", "fore")
	Back = getColor("Output background", "back")
	if Back == "\\u001b[0m" and Fore == "\\u001b[0m":
		openTheme["styles"]["output"] = Fore
	elif Back == "\\u001b[0m":
		openTheme["styles"]["output"] = Back + Fore
	else:
		openTheme["styles"]["output"] = Fore + Back
	root.quit()
	print("Saving theme...")
	with open(themePath + "/" + file, "w") as themeFile:
		openTheme.write(themeFile)
	print("Theme saved at " + themePath + "/" + file)

def help():
	print("themegui.makeTheme() - Make Theme")
