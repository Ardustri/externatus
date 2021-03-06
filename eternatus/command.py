import load, out, os
from watchrun import watch_and_run
def init(args=""):
	print("Creating Project...")

def check_command(args):
	for key in load.f.keys():
		for i in load.f["command"].keys():
			if i == args:
				return(load.f["command"][i])
				break

def run(args, opts=None, flag=None):
	opts = args["command_opts"]
	if opts != None:
		for i in range(int(opts)):
			os.system(check_command(args["command_args"]))
	else:
		os.system(check_command(args["command_args"]))

def show_info(args):
	out.succeed(f"NAME: {load.f['name']}")
	out.info(f"VERSION: {load.f['version']}")
	out.info(f"COMMAND_LIST: \n{load.f['command']}")

def hello(args):
	print("helo yati")

def hello_qila(args):
	os.system("php test.php")

command_flag = ["-c", "-t", "-h", "--timer", "--clear", "--help"]
command_list = {"init": init, "run": run, "show_info": show_info, "watch": watch_and_run, "yati": hello, "aqila": hello_qila, }
