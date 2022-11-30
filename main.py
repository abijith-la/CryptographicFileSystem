import os
import time

from aes1 import *
from file_manager_cli import *
from password_cli import *

from pyfiglet import Figlet
f = Figlet(font='cybermedium')

print (f.renderText('Cryptographic File System'))
input("Press Enter to access files...")
os.system('clear')

password_cli()

def Main():
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
		print("No option selected, closing...")



def listdir():
  list = os.listdir()
  return list

def change_dir(name):
  os.chdir(name)

def remdir(name):
  os.rmdir(name)
def newdir(name):
  os.mkdir(name)

#def copyfile():  

#def remfile():

while (True):
  list = listdir()
  answers = file_manager_cli(list)
  answer = answers['ans']
  change_dir(answer)
  os.system('clear')

