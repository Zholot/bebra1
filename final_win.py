# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        
        self.show()

    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    
    def initUI(self): 
        
        self.line = QVBoxLayout()

        self.index = QLabel(txt_index)
        self.workheart = QLabel(txt_workheart)
    
        self.line.addWidget(self.index, alignment = Qt.AlignCenter)
        self.line.addWidget(self.workheart, alignment = Qt.AlignCenter)

       
app = QApplication([])
mw = FinalWin()
app.exec_()