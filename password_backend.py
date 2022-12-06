from passlib.hash import pbkdf2_sha256
from functions import *
from password_change_cli import * 
from password_cli import *

def password_backend(password):
    f = open("hashDO_NOT_DELETE.txt",'r+')
    existpass = f.read()
    f.close()
    return pbkdf2_sha256.verify(password, existpass)

def password_verify():
	key = password_change_cli()
	if password_backend(key) == False:
		os.system('clear')
		print("Wrong Password!")
		password_verify()
	else:
		return

def password_verify_start():
	key = password_cli()
	if password_backend(key) == False:
		os.system('clear')
		print("Wrong Password!")
		password_verify_start()
	else:
		return

def password_change():
    os.system('clear')
    password_verify()
    f = open("hashDO_NOT_DELETE.txt",'r+')
    f.truncate(0)
    new_password = input("Enter new password: ")
    new_hash = pbkdf2_sha256.hash(new_password)
    f.write(new_hash)
    f.close()

