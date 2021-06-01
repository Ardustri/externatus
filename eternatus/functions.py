import os, sys
import load, out
import command as _command
def run_command(command, count=0):
	for i in range(count):
		os.system(command)

def printinfo():
	out.info("NAME: ", load.f["name"])
	out.info("VERSION:", load.f["version"])
	out.info("COMMAND_LIST: \n", load.f["command"])

def ask():
	command_name = None
	command_args = None
	command_opts = None
	try:
		command_name = sys.argv[1]
	except:
		out.error("No command suplied")
	try:
		command_args = sys.argv[2]
	except:
		pass
	try:
		command_opts = sys.argv[3]
	except:
		pass

	return {"command_name": command_name, "command_args": command_args, "command_opts": command_opts}

command = ask()

def check_command():
	global command
	if command["command_args"] == None:
		del command["command_args"]
	if command["command_opts"] == None:
		del command["command_opts"]

def execute():
	global command
	check_command()
