# Pleth_Test


# Part 2: Scripting Exercise

      Language used: Python 3.3
      OS           : Windows
  
#Execution Steps:
      1. Run the script pleth_2.py using Python3.3
      2. Enter the full path of the directory when prompted 
#Test Cases Verified:
      1. Tested invalid or non existent paths
      2. Tested for valid paths with recursive sub directories and files
      3. Tests for empty directory
      4. Tested for directory names containing spaces
      5. Tested for soft-links or shortcuts 
#Example:
  
      C:\Python27\My_Programs>python pleth_2.py

      Enter full path of the directory: C:\Projects\Plethora

      ************Output************

      /Plethora
        logo.gif
        readme.txt
        /bin
          program.exe
          /config
            api.config
            ui.config
        /localization
          en-us.html

      ******************************

