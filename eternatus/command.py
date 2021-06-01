def hello():
	print("hello")

command_flag = ["-c", "-t", "-h", "--timer", "--clear", "--help"]
command_list = {"init": hello, "run": "", "print_info": ""}
