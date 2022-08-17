import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import dialogs


### VARIABLES
uname = os.uname()[3]
dir = QDir()
main_path = os.getcwd()

###DICTIONARIES
criteria = ['*', '.txt', '.jpg', '.docx', '.py', '.psd']


### CLASSES
class Engine:
    def __init__(self):
        self._path = "/"

    def _pwd(self):
        path = str(os.getcwd())
        return Engine._update_view(self, path, "[PWD]:")
    def _list(self):
        var = os.listdir()
        if len(var) != 0:
            note = "PWD CONTAINS THE FOLLOWING:"
            Engine._update_view(self, note)
            for i in var:
                Engine._update_view(self, i)
        else:
            note = "PWD IS EMPTY"
            Engine._update_view(self, note)
    def _setwd(self, thing):
        path = (self.getExistingDirectory(self,"Choose Directory"))
        try:
            Engine._chdir(path)
        except FileNotFoundError:
            return
        Engine._update_view(thing, path, "[NEW PWD]:")
        

    def _update_view(caller, thing, more=""):
        caller.insertPlainText(f"->>  {more} {thing}\n")

    def _chdir(self):
        os.chdir(self)

    def _reset_pwd(self):
        os.chdir(main_path)
        return Engine._pwd(self)

    def _check_criteria(self):
        criteria_list = []
        for criterium in criteria:
            criteria_list.append(criterium)
        return Engine._update_view(self, criteria_list, "FILE TYPES TO BE REARRANGED INCLUDE:\n")

    def _set_criteria(self):
        Engine._update_view(self, "criteria set")
        dialogs.setcriteria()

    def _set_rules(self):
        Engine._update_view(self, "rules set")
        # dialogs.setrules()

    def _save_settings(self):
        Engine._update_view(self, 'settings saved')

    def _save_logs(self):
        Engine._update_view(self, 'logs saved')

    def _review_report(self):
        Engine._update_view(self, 'reviewing Report')

    def _create_map(self):
        Engine._update_view(self, 'Create Map')
    
    def _commit(self):
        Engine._update_view(self, 'Done')
    
    def _view_logs(self):
        Engine._update_view(self, 'view logs')
        
    def _revert(self):
        Engine._update_view(self, 'revert commit')
    
    def _print_report(self):
        Engine._update_view(self, 'print report')
        


