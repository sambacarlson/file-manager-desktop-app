import datas

import os
import shutil

path = r'/home/carlson/Documents/programming/test_dir'

### returns a set of all file types in a given path
def fxnFileTypes(path):  
    ext_set = set()
    for roots, dirs, files in os.walk(path):
        for file in files:
            for ext in datas.win_exts:
                if file.endswith(ext):
                    ext_set.add(ext)

    return ext_set


### returns a dictionary with filetypes as keys and lists of files with of those types as values
def fxnGroupSimilar(path):
    dic = {}
   
    return dict



 ###### test function calls
fxnGroupSimilar(path)