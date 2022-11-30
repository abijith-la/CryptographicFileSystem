import os


name = 'crypto'

def listdir():
	list = os.listdir()
	return list

def change_dir(name):
	os.chdir(name)

def remdir(name):
	os.rmdir(name)

def newdir(name):
	os.mkdir(name)

def fileordir(path,fdname):
	path = path + '/' + fdname
	if os.path.isfile(path):
		return 1
	elif os.path.isdir(path):
		return 0
	else:
		return -1

def nothomedir(path):
	return path.rsplit('/')[-1] != name