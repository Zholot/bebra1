# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
from second_win import *



class MainWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()# устанавливает, как будет выглядеть окно
        self.initUI() # создаём и настраиваем графические элементы (виджеты)
        self.connects() # устанавливает связи между элементами
        self.show() # старт

    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self): 
        self.hello_text = QLabel(txt_hello)
        #self.hello_text = QWidget(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.bnt_next = QPushButton(txt_next)
        
        self.layout = QVBoxLayout()
        #self.hello_text.addWidget(self.layout)
        #self.instruction.addWidget(self.layout)
        #self.bnt_next.addWidget(self.layout)

        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.bnt_next, alignment = Qt.AlignLeft)




    def connects(self): 
        self.bnt_next.clicked.connect( self.next_click )

    
    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()

