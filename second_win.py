# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self): 
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        

        self.name = QLabel(txt_name)
        self.age = QLabel(txt_age)
        self.test1 = QLabel(txt_test1)
        self.test2 = QLabel(txt_test2)
        self.test3 = QLabel(txt_test3)
        self.timer = QLabel()

        self.btn1 = QPushButton(txt_test1)
        self.btn2 = QPushButton(txt_test2)
        self.btn3 = QPushButton(txt_test3)
        self.btn_sendres = QPushButton(txt_sendresults)
        
        
        self.hintname = QLineEdit(txt_hintname)
        self.hintage = QLineEdit(txt_hintage)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)

        
        
        
        self.l_line.addWidget(self.btn1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_sendres, alignment = Qt.AlignCenter)

        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3, alignment = Qt.AlignLeft)
        
        self.l_line.addWidget(self.hintname, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hintage, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest3, alignment = Qt.AlignLeft)   


        self.r_line.addWidget(self.timer, alignment = Qt.AlignRight) 


        self.h_line.addWidget(self.l_line)
        self.h_line.addWidget(self.r_line)
        self.setLayout(self.h_line)


    
    def connects(self): 
        self.btn_sendres.clicked.connect( self.next_click )

    
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

app = QApplication([])
mw = TestWin()
app.exec_()
