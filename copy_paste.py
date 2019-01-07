
'''
Name: copy paste
Author: Lawrance Glenn
Description: A simple program allowing user to move, copy and paste files with a single click.
'''
from maya import cmds
import shutil, os
files = ['file1.txt', 'file2.txt', 'file3.txt']
for f in files:
    shutil.copy(f, 'dest_folder')

    ''' user interface still needed'''