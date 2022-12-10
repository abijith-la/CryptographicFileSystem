import os
import sys
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
        if len(listonlyfiles()) > 0:
            down_del_file_cli(listonlyfiles())
        else:
            input("No Files in current directory\nPress ENTER to continue")

    elif optanswer == 'Download File':
        if len(listonlyfiles()) > 0:
            down_del_file_cli(listonlyfiles())
        else:
            input("No Files in current directory\nPress ENTER to continue")
            
    elif optanswer == 'Delete Directory':
        if len(listonlydir()) > 0:
            delete_dir_cli(listonlydir())
        else:
            input("No Subdirectories in current directory\nPress ENTER to continue")

    elif optanswer == 'Upload Files':
        list = os.listdir(dir_path + '/cfsuploads')
        if len(list) > 0:
            for i in list:
                path = dir_path + '/cfsuploads/' + i
                if os.path.isfile(path):
                    shutil.copy2(path, os.getcwd())
                elif os.path.isdir(path):
                    shutil.copytree(path, os.getcwd() + '/' + i)
            ch = input("Files/Directories have been uploaded\nDo you want to clear out /cfsuploads ?\n(y/n)")
            if ch == 'y':
                del_contents_ofdir(dir_path + '/cfsuploads')
                input("/cfsuploads is cleared\nPress Enter to continue")
            else:
                return
        else:
            input("No Files/Directories to upload\nPlease copy files to /cfsuploads before trying again\nPress ENTER to continue")

    elif optanswer == 'Change Password':
        password_change()

    elif optanswer == 'Quit':
        enc_all()
        zip_enc()
        sys.exit()

        