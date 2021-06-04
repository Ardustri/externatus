import os, sys
import out
import command as _command

def ask():
	command_name = None
	command_args = None
	command_opts = None
	try:
		command_name = sys.argv[1]
	except:
		out.error("No command suplied")
		quit()
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
		command["command_args"] = None
	if command["command_opts"] == None:
		command["command_opts"] = None

def execute():
	global command
	for i in _command.command_list.keys():
		if i == command["command_name"]:
			_command.command_list[str(i)](command)
			break
	check_command()
