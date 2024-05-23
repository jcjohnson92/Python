# get list of ports that are open
# ie nmap scan and shows 80,139,445 
# Make a file for each for note
# make a direcotry for enumeration, exploit, and the main directory

import os
import sys


directory_list = ["1_enumeration", "2_exploit"]
main_directory = sys.argv[1]
parent_directory = "D:/HackingNotes"
path = os.path.join(parent_directory,main_directory)
try:
    print(f"Creating directory {main_directory}")
    os.mkdir(path)
except FileExistsError:
    print("File Exists")
    exit

#Create the sub directories
for i in directory_list:
    print(f"Creating Diretory {i}")        
    os.mkdir(os.path.join(path,i))


port_file = open(f"D:/HackingNotes/nmap/{sys.argv[2]}")
folder_intialization = os.chdir(path + "/" + directory_list[0])

# Create the notes for each port
for i in port_file:
    
    p = (i.strip())
    print(f"Creating {p}.md")
    with open(f"{p}.md", "w") as file:
        file.write(f"# Enumeration - {p}")