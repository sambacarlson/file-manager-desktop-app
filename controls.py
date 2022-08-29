import datas

import os
import shutil
from pathlib import Path, PurePath

path = Path(datas.working_path) # must be a path-like object
rules = datas.rules # note that all keys are pre-defined. changing any key  itself may result in errors

### returns a set of all file types in a given path
def fxnFileTypes(path):  
    ext_set = set()
    for file in path.iterdir():
        if file.is_file():
            if file.suffix in datas.win_exts:
                ext_set.add(file.suffix)
    return ext_set

### returns list of filetypes not given in win_exts
def fxnOtherTypes(path):
    ext_set = set()
    for x in path.iterdir():
        if x.is_file():
            if x.suffix not in datas.win_exts:
                ext_set.add(x.suffix)
    return ext_set

### returns a dictionary with filetypes as keys and lists of files with of those types as values
def fxnGroupSimilar(path):
    dict = {}
    for extension in fxnFileTypes(path):
        dict[extension]= [i for i in path.iterdir() if i.is_file() and i.suffix == extension]
    return dict

### returns a list of duplicate file lists from  given two directories.
def fxnCheckDuplicate(src, dest):
    dup_list = []
    src_list = []
    dest_list = []
    if src == dest:
        return []
    if src.is_file() or dest.is_file():
        return []
    else:
        src_list = os.listdir(src)
        dest_list = os.listdir(dest)
        for i in src_list:
            if i in dest_list:
                for j in src_list:
                    if i == j:
                        dup_list.append([i, j])
    return dup_list

### returns dictionary of filetype frequencies for given path
"""
It ignores filetypes not included in win_exts
Also, it doesn't pick .txt files on Posix
"""
def fxnTypeFrequency(path):  
    dict = {}
    ext_list = list()
    for file in path.iterdir():
        if file.is_file():
            if file.suffix in datas.win_exts:
                ext_list.append(file.suffix)
    for i in ext_list:
        num = ext_list.count(i)
        if i in dict:
            continue
        else:
            dict[i] = num
    return dict

### Returns a tree structure(list) of all files(and their extensions) of any given path
def fxnFileMap(path):
    _map =[]
    return _map

###  Analyses rules and returns detailed dictionary of changes to be effected
def fxnAnalyse(rules):
    dict = {}

    return dict

###  calls corresponding functions to apply rules set
def fxnSmartDir(rules):
    
    return True ## returns true if no faults.


###### test function calls 
p1 = Path("/home/carlson/Documents/programming/test_dir/fol1")
p2 = Path("/home/carlson/Documents/programming/test_dir/fol2")
# print(fxnFileTypes(path))
# print(fxnOtherTypes(path))
# # print(fxnGroupSimilar(path))
# print(fxnCheckDuplicate(p1, p2))
# print(fxnTypeFrequency(p1))
print(fxnFileMap())
# print(fxnSmartDir())