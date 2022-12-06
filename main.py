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
password_verify_start()





""" def Main():
	choice = input("Would you like to (E)encrypt or (D)Decrypt ")

	if choice == 'E':
		filename = input("File to encrypt: ")
		encrypt(key, filename)     
		print('Done.')
	elif choice == 'D':
		filename = input("File to decrypt: ")
		decrypt(key, filename)
		print("Done.")

	else:
		print("No option selected, closing...") """

#def copyfile():  

#def remfile():
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
			#redirect to download module
			 
Main()	


			



