from command import *
from functions import *

for i in command_list:
	if command_list[i] == command_type[0]:
		standalone()
		break
	elif command_list[i] == command_type[1]:
		arguments()
		break

try:
	command_opts:str = sys.argv[3]
except:
	opts = None
