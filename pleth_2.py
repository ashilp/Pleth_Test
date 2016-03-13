import os

def read_path(path):
    '''
    Function to list out directories, subdirectories, files with proper indentation
    '''
    #indent according to the level of the directory
    level =  path.count("\\")
    print("\n************Output************\n")
    if not os.path.exists(path):
        print("Error: Path does not exist")
        return
    for root, dirs, files in os.walk(path):
        #for indentation of directory, sub-directory, files 
        space = "    "*(root.count("\\")-level)
        if (os.path.isdir(root)):
            print(space+"/"+os.path.basename(root))
        for f in files:
            print (space+"    "+f)
    print("\n******************************\n")

if __name__=="__main__":
    path = input("\nEnter full path of the directory: ")
    read_path(path)

'''
Test Cases Verified:
- Tested invalid or non existent paths
- Tested for valid paths with recursive sub directories and files
- Tests for empty directory
- Tested for directory names containing spaces
- Tested for soft-links or shortcuts 
'''