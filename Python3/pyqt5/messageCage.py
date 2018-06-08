# -*- coding: utf-8 -*-
# @Date    : 2018-06-07 19:32:44
# @Author  : mohailang (1198534595@qq.com)

import sys
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication,QPushButton
from PyQt5.QtCore import QCoreApplication
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Message Box')
        self.show()

    def closeEvent(self, QCloseEvent):

        reply=QMessageBox.question(self,'Message',"确定退出？",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

        if reply==QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())