# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:09:55 2019

Should work with both python 2.7 and python 3.x (written in 3.6)

Will open a new dialogue window with a button to choose the folder where stimuli are located
Using the button will open a file explorer to select the location of the folder, this will update the first field
In the second field, specify the file extension you wish to rename within the folder (defaults to .wav)
If you wish to add anything to the beginning of each name (sampling rate, speaker, etc) enter this into the 3rd field
Anything you wish to add to the end of each base file name (before the file extension) goes in the fourth field
The 5th and 6th fields are for removing a set number of characters from the beginning or the end of each file respectively
For example, if you have files named back1_0, back2_0, back3_0, etc. and want to remove the "_0" from each file
You would enter 2 into field six.

Fields 3 and 4 may be left blank if you do not wish to add anything new to the beginning or end of the file
And you can complete one and leave the other blank safely as well

Feel free to get in touch with Francis if anything isn't working when you try this.

Last Updated: 7/3/2019

@author: fxsmith
"""

import os
try:
    import Tkinter as tk
    import tkFileDialog as filedialog
except ImportError:
    import tkinter as tk
    from tkinter import filedialog

dirText = "Select the folder where your files are located"

def openDirectory():
    global e1default
    dirName = filedialog.askdirectory(parent=root, title=dirText)
    e1default.set(str(dirName))

def batchRename():
    filepath = e1.get()
    extension = e2.get()
    prepend = e3.get()
    append = e4.get()
    removeBegin = int(e5.get())
    removeEnd = int(e6.get())
    
    for file_name in os.listdir(filepath):
        if file_name.endswith(extension):
            file, ext = os.path.splitext(file_name)
            if removeEnd == 0:
                new_file_name = file
            else:
                new_file_name = file[:-removeEnd]
            new_file_name = new_file_name[removeBegin:]
            new_file_name = prepend + new_file_name
            new_file_name = new_file_name + append
            new_file_name = new_file_name + extension
            os.rename(os.path.join(filepath, file_name), os.path.join(filepath, new_file_name))
        else:
            continue   
    
root = tk.Tk()
root.title("Batch File Rename")
tk.Label(root, text="Location of files (path to folder)").grid(row=1)
tk.Label(root, text="Extension of files (.wav, .aiff, etc.)").grid(row=2)
tk.Label(root, text="Text to prepend to base file names (leave blank to add nothing)").grid(row=3)
tk.Label(root, text="Text to append to base file names (leave blank to add nothing)").grid(row=4)
tk.Label(root, text="Number of characters to remove from the beginning of base file names").grid(row=5)
tk.Label(root, text="Number of characters to remove from the end of base file names").grid(row=6)

e1default = tk.StringVar()
e2default = tk.StringVar()
e5default = tk.StringVar()
e6default = tk.StringVar()

dirBut = tk.Button(root, text=dirText, command=openDirectory).grid(row=0, column=1, pady=5)
e1 = tk.Entry(root, textvariable=e1default, width=100)
e2 = tk.Entry(root, textvariable=e2default, width=100)
e3 = tk.Entry(root, width=100)
e4 = tk.Entry(root, width=100)
e5 = tk.Entry(root, textvariable=e5default, width=100)
e6 = tk.Entry(root, textvariable=e6default, width=100)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)

e1default.set("Choose your folder above")
e2default.set(".wav")
e5default.set("0")
e6default.set("0")

tk.Button(root, text="Rename Files", command=batchRename).grid(row=7, column=0, pady=4)
tk.Button(root, text="Quit", command=root.destroy).grid(row=7, column=1, pady=4)

root.mainloop()
