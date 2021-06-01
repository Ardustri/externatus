from watchgod import watch
import sys, os

try:
	path = sys.argv[1]
except:
	print("Invalid Path")
	quit()
try:
	command = sys.argv[2]
except:
	print("Invalid command")
	quit()

for changes in watch(path):
	os.system(command)
