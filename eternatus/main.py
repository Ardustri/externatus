import os, sys, re
import json
os.system("clear")

def run_command(command:str, count:int=1):
	for i in range(count):
		os.system(command)

opts = ""
char:int = 0
command_name:str = sys.argv[1]
command_args:str = sys.argv[2]
try:
	command_opts:str = sys.argv[3]
except:
	opts = None

def _error(message):

	print(Exception("\nError: " + message + "\n"))
	raise Exception("Error: " + message + "\n")

with open("eternatus.json", "r") as f:
	f = f.read()

_data = json.loads(f)

def check_command(data):
	if command_name == "run":
		os.system(str(data[command_args]))
		if opts != None:
			try:
				run_command(data[command_args], count=int(float(command_opts)))
			except Exception as e:
				print(e)
				_error("Invalid Argument")


check_command(_data)
