from pypresence import Presence
import configparser
from dialog import Dialog

class settings:
	choices = [("Discord Rich Presence", "Display ImaginaryInfinity Calculator as your status in Discord"), ("Dynamic RPC", "Update Discord RPC on calculation")]
	
	def settingsPopup(tag, config):
		d = Dialog()
		if tag == "Discord Rich Presence":
			x = d.menu("Discord Rich Presence", choices=[("Enable", "Enable Discord RPC"), ("Disable", "Disable Discord RPC")])
			if x[1] == "Enable":
				config["discord"]["enableRPC"] = "true"
			else:
				config["discord"]["enableRPC"] = "false"
		elif tag == "Dynamic RPC":
			x = d.menu("Update Discord RPC with your last done calculation", choices=[("Enable", "Enable Dynamic RPC"), ("Disable", "Disable Dynamic RPC")])
			if x[1] == "Enable":
				config["discord"]["dynamicPresence"] = "true"
			else:
				config["discord"]["dynamicPresence"] = "false"
		return config

def main():
	global config
	config = configparser.ConfigParser()
	config.read("config.ini")
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
	with open("config.ini", "w") as configFile:
		config.write(configFile)
		configFile.close()

	if config["discord"]["enableRPC"] == "true":
		try:
			global rpc
			rpc = Presence("720335749601296464")
			rpc.connect()
			rpc.update(state="Calculating with ImaginaryInfinity Calculator", details="https://turbowafflz.gitlab.io/iicalc.html", large_image="iicalclogo", large_text="ImaginaryInfinity Calculator")
		except:
			yesno = input("Your system doesn't seem to support Discord rich presence. Would you like to disable it? (Y/n)")
			if yesno.lower() == "y" or yesno.lower() == "":
				config["discord"]["enableRPC"] = "false"
				with open("config.ini", "w") as configFile:
					config.write(configFile)
					configFile.close()

def onInput(arg):
	try:
		if config["discord"]["dynamicPresence"] == "true":
			rpc.update(state="Calculating with ImaginaryInfinity Calculator", details="Just executed " + arg, large_image="iicalclogo", large_text="https://turbowafflz.gitlab.io/iicalc.html", small_text="Just executed " + arg)
	except:
		pass

main()
