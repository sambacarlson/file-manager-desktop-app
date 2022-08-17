# from turtle import color
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from widgets import GridButton
from engine import *



class FileManager(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("File Manager")
        self.setFixedSize(550, 420)

        main_layout = QVBoxLayout()
        buttons_layout = QGridLayout()
        display_layout = QGridLayout()
        self.setLayout(main_layout)

        ### MENUBAR
        menubar = QMenuBar()
        main_layout.addWidget(menubar)
        file_menu = menubar.addMenu("File")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Print")
        file_menu.addSeparator()
        file_menu.addAction("Exit")
        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Revert")
        edit_menu.addAction("Redo")
        help_menu = menubar.addMenu("Help")
        help_menu.addAction("About")
        help_menu.addSeparator()
        help_menu.addAction("Guide")
        help_menu.addAction("Wizard")
        help_menu.addSeparator()
        help_menu.addAction("Review")

        ### FRAMES
        buttons_frame = QFrame()
        main_layout.addWidget(buttons_frame)
        buttons_frame.setLayout(buttons_layout)
        buttons_frame.setFrameShape(QFrame.Box)
        buttons_frame.setFrameShadow(QFrame.Sunken)

        display_frame = QFrame()
        main_layout.addWidget(display_frame)
        display_frame.setLayout(display_layout)
        display_frame.setFrameShape(QFrame.Box)
        display_frame.setFrameShadow(QFrame.Sunken)

        ###BUTTONS SECTION
        ##variables
        # file_dialog = QFileDialog()
        ##buttons
        GridButton("Check PWD", lambda: Engine._pwd(console_view), buttons_layout, 0, 0)
        GridButton("Set WD", lambda: Engine._setwd(QFileDialog(), console_view), buttons_layout, 0, 1)
        GridButton("Reset PWD", lambda: Engine._reset_pwd(console_view), buttons_layout, 0, 2)
        GridButton("Save Settings", lambda: Engine._save_settings(console_view), buttons_layout, 0, 3)
        GridButton("Dir Info", lambda: Engine._list(console_view), buttons_layout, 1, 0)
        GridButton("Check Criteria", lambda: Engine._check_criteria(console_view), buttons_layout, 1, 1)
        GridButton("Set Criteria", lambda: Engine._set_criteria(console_view), buttons_layout, 1, 2)
        GridButton("Set Rules", lambda: Engine._set_rules(console_view), buttons_layout, 1, 3)
        GridButton("Review Report", lambda: Engine._review_report(console_view), buttons_layout, 2, 0)
        GridButton("Revert", lambda: Engine._revert(console_view), buttons_layout, 2, 1)
        GridButton("Print Report", lambda: Engine._print_report(console_view), buttons_layout, 2, 2)
        GridButton("Create Map", lambda: Engine._create_map(console_view), buttons_layout, 2, 3)

        ### DISPLAY SECTION
        console_view = QPlainTextEdit()
        display_layout.addWidget(console_view, 0, 0, 1, 4)
        console_view.setReadOnly(True)
        console_view.setPlaceholderText(f"{uname}")
        console_view.setWordWrapMode(QTextOption.NoWrap)
        console_view.setStyleSheet(f"color: white; background-color: black")
        
        GridButton("Commit", lambda: Engine._commit(console_view), display_layout, 1, 0)
        GridButton("Save Log", lambda: Engine._save_logs(console_view), display_layout, 1, 1)
        GridButton("View Logs", lambda: Engine._view_logs(console_view), display_layout, 1, 2)
        GridButton("Clear", lambda: console_view.clear(), display_layout, 1, 3)
    


def main():
    app = QApplication(sys.argv)
    screen = FileManager()
    screen.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()