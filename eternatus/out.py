from colorama import Fore, Style, init

init(autoreset=True)

def info(message):
	print(f"{Style.BRIGHT}{Fore.BLUE}{message}")

def warn(message):
	print(f"{Style.BRIGHT}{Fore.YELLOW}{message}")

def error(message):
	print(f"{Style.BRIGHT}{Fore.RED}Error: {message}")

def succeed(message):
	print(f"{Style.BRIGHT}{Fore.GREEN}{message}")
