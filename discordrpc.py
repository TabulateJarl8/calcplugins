from pypresence import Presence
import configparser
import time
from systemPlugins.core import configPath

def main():
	global config
	config = configparser.ConfigParser()
	config.read(configPath)
	if not config.has_section("discord"):
		config.add_section("discord")
		config["discord"]["enableRPC"] = "ask"
	if not config.has_option("discord", "dynamicPresence"):
		config["discord"]["dynamicPresence"] = "true"
		with open("config.ini", "w") as configFile:
			config.write(configFile)
			configFile.close()
	if config["discord"]["enableRPC"] == "ask":
		yn = input("Would you like to enable Discord rich presence? (Y/n)")
		if yn.lower() == "y":
			config["discord"]["enableRPC"] = "true"
		elif yn.lower() == "n":
			config["discord"]["enableRPC"] = "false"
		elif yn.lower() == "askagain":
			config["discord"]["enableRPC"] = "ask"
		else:
			config["discord"]["enableRPC"] = "true"
	with open(configPath, "w") as configFile:
		config.write(configFile)
		configFile.close()

	if config["discord"]["enableRPC"] == "true":
		global start
		start = str(time.time()).split(".")[0]
		try:
			global rpc
			rpc = Presence("720335749601296464")
			rpc.connect()
			rpc.update(state="Calculating with ImaginaryInfinity Calculator", details="https://turbowafflz.gitlab.io/iicalc.html", large_image="iicalclogo", large_text="ImaginaryInfinity Calculator", start=start)
		except:
			yesno = input("Your system doesn't seem to support Discord rich presence. Would you like to disable it? (Y/n)")
			if yesno.lower() == "y" or yesno.lower() == "":
				config["discord"]["enableRPC"] = "false"
				with open(configPath, "w") as configFile:
					config.write(configFile)
					configFile.close()

def onInput(arg):
	try:
		if config["discord"]["dynamicPresence"] == "true":
			rpc.update(state="Calculating with ImaginaryInfinity Calculator", details="Just executed " + arg, large_image="iicalclogo", large_text="https://turbowafflz.gitlab.io/iicalc.html", small_text="Just executed " + arg, start=start)
	except:
		pass

main()
