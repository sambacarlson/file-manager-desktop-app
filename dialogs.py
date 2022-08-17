from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def setrules():
    rules = QDialog()
    rules.setWindowTitle("Set Rules")
    rules.setWindowModality(Qt.ApplicationModal)
    rules.exec_()

def setcriteria():
    criterials = QDialog()
    criterials.setWindowTitle("Set Criteria")
    criterials.setWindowModality(Qt.ApplicationModal)
    # criterials.setSizeGripEnabled(True)
    criterials_layout = QGridLayout()

    criterials.setLayout(criterials_layout)

    title = QLabel("Choose the various file types you want to be included in the rearangements")
    title.setWordWrap(True)
    criterials_layout.addWidget(title, 0, 0, 1, 2)

    type1 = QCheckBox("All types")
    criterials_layout.addWidget(type1, 1, 0)
    type2 = QCheckBox("Documents(txt, docx, odt, pdf, ...)")
    criterials_layout.addWidget(type2, 2, 0)
    type3 = QCheckBox("Media files(mp3, mp4, wav, avi, m4a, ...)")
    criterials_layout.addWidget(type3, 2, 1)
    type4 = QCheckBox("Picutures(png, jpg, gif, ...)")
    criterials_layout.addWidget(type4, 3, 0)
    type5 = QCheckBox("Programs(exe, zip, iso, ...)")
    criterials_layout.addWidget(type5, 3, 1)

    add_type = QPushButton("Add type")
    add_type.pressed.connect(lambda: fxn_add_type(custom_group_layout))
    criterials_layout.addWidget(add_type, 4, 0)

    remove_type = QPushButton("remove type")
    criterials_layout.addWidget(remove_type, 4, 1)

    custom_group_layout = QVBoxLayout()
    custom_group = QGroupBox()
    criterials_layout.addWidget(custom_group, 5, 0, 1, 2)
    custom_group.setLayout(custom_group_layout)
    custom_group.setTitle("Custom Types")

    buttonbox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
    criterials_layout.addWidget(buttonbox, 6, 1)

    criterials.exec_()

def fxn_add_type(position):
    check = QCheckBox()
    position.addWidget(check)
    value = 'new type'
    check.setText(value)

    
    