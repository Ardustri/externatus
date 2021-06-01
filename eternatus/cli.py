from command import *
import sys
command_name:str = sys.argv[1]
command_args:str = sys.argv[2]
try:
	command_opts:str = sys.argv[3]
except:
	opts = None
