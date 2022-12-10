import os

from aes1 import *
from file_manager_cli import *
from password_cli import *
from options_cli import *
from functions import *
from optionsbackend import *
from down_file_backend import *
from password_backend import *

from pyfiglet import Figlet
f = Figlet(font='cybermedium')


os.system('clear')
main_path = os.getcwd()
password_verify_start()
if os.path.exists(dir_path + "/cfs1234"):
	pass
elif os.path.exists(dir_path + "/(enc)cfs1234.zip"):
	zip_dec()
	if os.path.exists(dir_path + "/cfs1234"):
		if len(os.listdir(dir_path + "/cfs1234")) > 0:
			dec_all()
	else:
		newdir('cfs1234')
else:
	newdir('cfs1234')
change_dir(dir_path + "/cfs1234")

def Main():
	while (True):
		list = listdir()
		answer = file_manager_cli(list)
		if answer == '//More Options//':
			optionsbackend(options_cli())
		elif fileordir(os.getcwd(),answer) == 0:
			change_dir(answer)
		else:
			down_file_backend(os.getcwd(),answer)
			 
Main()	


			



