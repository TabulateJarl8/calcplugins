from pypresence import Presence
import configparser
import time
from systemPlugins.core import configPath, pluginPath, themePath
from dialog import Dialog
from glob import glob
import traceback
import shutil

class settings:
	choices = [("Discord RPC Settings", "Settings for the discordrpc plugin")]
	def settingsPopup(tag, config):
		if tag == "Discord RPC Settings":
			d = Dialog()
			drpcmenu = d.menu("Discord RPC Settings", choices=[("Discord Rich Presence", "Display ImaginaryInfinity Calculator as your status in Discord"), ("Dynamic RPC", "Update Discord RPC on calculation"), ("Plugins and Themes in RPC", "Show number of Installed Plugins/Themes"), ("Buttons", "Show buttons in RPC"), ("Debug", "Debug Mode")], width=0, height=0)
			if drpcmenu[1] == "Discord Rich Presence":
				x = d.menu("Discord Rich Presence", choices=[("Enable", "Enable Discord RPC"), ("Disable", "Disable Discord RPC")])
				if x[1] == "Enable":
					config["discord"]["enableRPC"] = "true"
				else:
					config["discord"]["enableRPC"] = "false"
			elif drpcmenu[1] == "Dynamic RPC":
				x = d.menu("Update Discord RPC with your last done calculation", choices=[("Enable", "Enable Dynamic RPC"), ("Disable", "Disable Dynamic RPC")])
				if x[1] == "Enable":
					config["discord"]["dynamicPresence"] = "true"
				else:
					config["discord"]["dynamicPresence"] = "false"
			elif drpcmenu[1] == "Plugins and Themes in RPC":
				if config["discord"]["showAmountOfPlugins"] == "true":
					pluginStatus = "on"
				else:
					pluginStatus = "off"
				if config["discord"]["showAmountOfThemes"] == "true":
					themeStatus = "on"
				else:
					themeStatus = "off"
				x = d.checklist("Show number of installed plugins/themes", choices=[("Plugins", "Show number of installed plugins", pluginStatus), ("Themes", "Show number of installed themes", themeStatus)])
				if "Plugins" in x[1]:
					config["discord"]["showAmountOfPlugins"] = "true"
				else:
					config["discord"]["showAmountOfPlugins"] = "false"
				if "Themes" in x[1]:
					config["discord"]["showAmountOfThemes"] = "true"
				else:
					config["discord"]["showAmountOfThemes"] = "false"
			elif drpcmenu[1] == "Buttons":
				x = d.menu("Show Buttons", choices=[("True", "Show buttons in RPC"), ("False", "Hide buttons in RPC")])
				if x[1] ==  "True":
					config["discord"]["showButtons"] = "true"
				else:
					config["discord"]["showButtons"] = "false"
			elif drpcmenu[1] == "Debug":
				x = d.menu("Debug Mode", choices=[("On", "Debug mode on"), ("Off", "Debug mode off")])
				if x[1] ==  "On":
					config["discord"]["debug"] = "true"
				else:
					config["discord"]["debug"] = "false"
		return config

def main():
	global config
	config = configparser.ConfigParser()
	config.read(configPath)
	changed = False
	if not config.has_section("discord"):
		config.add_section("discord")
		config["discord"]["enableRPC"] = "ask"
		changed = True
	if not config.has_option("discord", "dynamicPresence"):
		config["discord"]["dynamicPresence"] = "true"
		changed = True
	if not config.has_option("discord", "showAmountOfPlugins"):
		config["discord"]["showAmountOfPlugins"] = "true"
		changed = True
	if not config.has_option("discord", "showAmountOfThemes"):
		config["discord"]["showAmountOfThemes"] = "true"
		changed = True
	if not config.has_option("discord", "showButtons"):
		config["discord"]["showButtons"] = "true"
		changed = True
	if not config.has_option("discord", "debug"):
		config["discord"]["debug"] = "false"
		changed = True
	if config["discord"]["enableRPC"] == "ask":
		yn = input("Would you like to enable Discord rich presence? (Y/n)")
		if yn.lower() == "y":
			config["discord"]["enableRPC"] = "true"
			changed = True
		elif yn.lower() == "n":
			config["discord"]["enableRPC"] = "false"
			changed = True
		elif yn.lower() == "askagain":
			config["discord"]["enableRPC"] = "ask"
		else:
			config["discord"]["enableRPC"] = "true"
			changed = True
	if changed == True:
		with open(configPath, "w") as configFile:
			config.write(configFile)

	if config["discord"]["enableRPC"] == "true":
		global start
		start = str(time.time()).split(".")[0]
		try:
			global rpc
			rpc = Presence("720335749601296464")
			rpc.connect()
			large_text = "ImaginaryInfinity Calculator  "
			if config["discord"]["showAmountOfPlugins"] == "true":
				large_text += str(len(glob(pluginPath + "/*.py"))) + " Plugin"
				if str(len(glob(pluginPath + "/*.py"))) != 1:
					large_text += "s"
			if config["discord"]["showAmountOfThemes"] == "true":
				if large_text.endswith("Plugins") or large_text.endswith("Plugin"):
					large_text += " | "
				large_text += str(len(glob(themePath + "/*.iitheme")) + len(glob(config["paths"]["systemPath"] + "/themes/*.iitheme"))) + " Theme"
				if str(len(glob(pluginPath + "/*.py"))) != 1:
					large_text += "s"
			if config["discord"]["showButtons"] == "true":
				buttons = [{"label": "Github", "url": "https://github.com/TurboWafflz/ImaginaryInfinity-Calculator"}]
			else:
				buttons = None
			rpc.update(state="Calculating with ImaginaryInfinity Calculator", details="https://turbowafflz.gitlab.io/iicalc.html", large_image="iicalclogo", large_text=large_text, start=start, buttons=buttons)
		except Exception as e:
			if config["discord"]["debug"] == "true":
				traceback.print_exc()
			if shutil.which("discord") == None:
				yesno = input("Discord is not detected, so rich presence cannot be run, maybe try starting discord? Would you like to disable the plugin? (Y/n)")
				if yesno.lower() == "y" or yesno.lower() == "":
					config["discord"]["enableRPC"] = "false"
					with open(configPath, "w") as configFile:
						config.write(configFile)
						configFile.close()

def onInput(arg):
	try:
		if config["discord"]["dynamicPresence"] == "true":
			large_text = "ImaginaryInfinity Calculator  "
			if config["discord"]["showAmountOfPlugins"] == "true":
				large_text += str(len(glob(pluginPath + "/*.py"))) + " Plugin"
				if str(len(glob(pluginPath + "/*.py"))) != 1:
					large_text += "s"
			if config["discord"]["showAmountOfThemes"] == "true":
				if large_text.endswith("Plugins") or large_text.endswith("Plugin"):
					large_text += " | "
				large_text += str(len(glob(themePath + "/*.iitheme")) + len(glob(config["paths"]["systemPath"] + "/themes/*.iitheme"))) + " Theme"
				if str(len(glob(pluginPath + "/*.py"))) != 1:
					large_text += "s"
			if config["discord"]["showButtons"] == "true":
				buttons = [{"label": "Github", "url": "https://github.com/TurboWafflz/ImaginaryInfinity-Calculator"}]
			else:
				buttons = None
			rpc.update(state="Calculating with ImaginaryInfinity Calculator", details="Just executed " + arg, large_image="iicalclogo", large_text=large_text, small_text="Just executed " + arg, start=start, buttons=buttons)
	except Exception as e:
		if config["discord"]["debug"] == "true":
			traceback.print_exc()

main()
