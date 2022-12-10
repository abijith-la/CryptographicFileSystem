from functions import *

def down_file_backend(path, filename):
    print("Do you want to download", filename, "?")
    ch = input("(y/n): ")
    if ch == 'y':
        download_file(path, filename)
        print(filename, "has been downloaded in /Downloads")
        print("Do you also want to delete", filename, "from your encrypted storage ?")
        ch2 = input("(y/n): ")
        if ch2 == 'y':
            del_file(path, filename)
            print(filename, " has been deleted.")
        else:
            os.system('clear')
            return
    else:
        os.system('clear')
        return
