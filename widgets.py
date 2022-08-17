from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class GridButton:
    def __init__(self, label: str, onpressed, layout, row: int, column: int):
        self.label = label
        self.onpressed = onpressed
        self.layout = layout
        self.row = row
        self.column = column
        self.grid_button()

    def grid_button(self):
        self.button = QPushButton(self.label)
        self.layout.addWidget(self.button, self.row, self.column)
        self.button.pressed.connect(self.onpressed)
