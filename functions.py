import os
import shutil
from aes1 import *

dir_path = os.path.dirname(os.path.realpath(__file__))
name = 'cfs1234'

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


def enc_all():
	key = b'Sixteen byte key'
	path = dir_path + '/' + 'cfs1234' 
	sup_enc(key, path)

def sup_enc(key, dir):
	change_dir(dir)
	list1 = os.listdir()
	for i in list1:
		if fileordir(os.getcwd(),i) == 1:
			encrypt(key,i)
			del_file(os.getcwd(),i)
		else:
			sup_enc(key, i)
	
def dec_all():
	key = b'Sixteen byte key'
	path = dir_path + '/' + 'cfs1234' 
	sup_dec(key, path)

def sup_dec(key, dir):
	change_dir(dir)
	list1 = os.listdir()
	for i in list1:
		if fileordir(os.getcwd(),i) == 1:
			decrypt(key,i)
			del_file(os.getcwd(),i)
		else:
			sup_dec(key, i)

def zip_enc():
	change_dir(dir_path)
	shutil.make_archive("cfs1234", 'zip', "cfs1234")
	remdir(dir_path,"cfs1234")
	key = b'Sixteen byte key'
	encrypt(key,"cfs1234.zip")
	del_file(dir_path,"cfs1234.zip")


def zip_dec():
	change_dir(dir_path)
	key = b'Sixteen byte key'
	decrypt(key,"(enc)cfs1234.zip")
	del_file(dir_path, "(enc)cfs1234.zip")
	shutil.unpack_archive("cfs1234.zip",dir_path + '/cfs1234','zip')
	del_file(dir_path,"cfs1234.zip")

def download_file(path,fname):
	pass

def del_file(path,fname):
	path = path + '/' + fname
	os.remove(path)

