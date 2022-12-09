import os
import shutil
from aes1 import *

name = 'crypto - Copy'

def listdir():
	list = os.listdir()
	return list

def listonlydir():
	list = os.listdir()
	path = os.getcwd()
	list1 = []
	for name in list:
		if fileordir(path,name) == 0:
			list1.append(name)
	return list1

def listonlyfiles():
	list = os.listdir()
	path = os.getcwd()
	list1 = []
	for name in list:
		if fileordir(path,name) == 1:
			list1.append(name)
	return list1

def change_dir(name):
	os.chdir(name)

def remdir(path,fdname):
	shutil.rmtree(path  + '/' + fdname)

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


def enc_all(main_path):
	change_dir(main_path + '/' + 'cfs1234' )
	print(os.getcwd())
	
	

def download_file(path,fname):
	pass

def del_file(path,fname):
	pass 

