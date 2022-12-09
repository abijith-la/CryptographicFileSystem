import os
from delete_dir_cli import *
from down_del_file_cli import *
from functions import *
from password_backend import *

#['Return','New Directory','Delete File','Delete Directory','Upload Files','Download File','Change Password','Quit']
def optionsbackend(optanswer):
    if optanswer == 'New Directory':
        dname = input ('Enter the name of the new directory: ')
        newdir(dname)
    elif optanswer == 'Delete File':
        down_del_file_cli(listonlyfiles())
    elif optanswer == 'Download File':
        down_del_file_cli(listonlyfiles())
    elif optanswer == 'Delete Directory':
        delete_dir_cli(listonlydir())
    elif optanswer == 'Upload Files':
        pass
    elif optanswer == 'Change Password':
        password_change()
    elif optanswer == 'Quit':
        enc_all()
        