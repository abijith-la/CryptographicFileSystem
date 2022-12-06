import os
from delete_dir_cli import *
from down_del_file_cli import *
from functions import *

#['Return','New Directory','Delete File','Delete Directory','Upload Files','Download File','Quit']
def optionsbackend(optanswer):
    if optanswer == 'New Directory':
        dname = input ('Enter the name of the new directory: ')
        newdir(dname)
    elif optanswer == 'Delete File':
        down_del_file_cli(listdir())
    elif optanswer == 'Delete Directory':
        delete_dir_cli(optanswer)
    elif optanswer == 'Quit':
        check_all_enc()
        