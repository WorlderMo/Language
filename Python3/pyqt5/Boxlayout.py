# -*- coding: utf-8 -*-
# @Date    : 2018-06-07 20:55:09
# @Author  : mohailang (1198534595@qq.com)

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        okButton=QPushButton('OK')
        cancelButton=QPushButton('Cancel')

        hbox=QHBoxLayout()
        # 伸缩量
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Layout')
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
