"""
directory:

Python has the os module that provides us with the many useful methods to work with directories and files as well
"""

import os

# get current directory
print(os.getcwd())

print("Changing directory....")

os.chdir("D:\\Trainings\\python\\python-training-aug-2022")
print(os.getcwd())

print(os.listdir())

# making a new dir
os.mkdir("test")
