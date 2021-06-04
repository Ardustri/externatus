from watchgod import watch
import sys, os

def watch_and_run(args):
	for changes in watch(args["command_args"]):
		os.system(args["command_opts"])
