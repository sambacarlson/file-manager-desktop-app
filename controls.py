# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

import os
import sys


def fxnFileTypes():  ### returns a list of all file types in a given path
    path = r'/home/carlson/Documents/programming/'
    for roots, dirs, files in os.walk(path):
        print (files)


fxnFileTypes()       
