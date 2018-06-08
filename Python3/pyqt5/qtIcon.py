# -*- coding: utf-8 -*-
# @Date    : 2018-06-07 17:04:02
# @Author  : mohailang (1198534595@qq.com)

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('QIcon')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置窗口的图标，引用当前目录下的图片,但显示不出来
    app.setWindowIcon(QIcon('hailang.png'))
    ex = Example()
    sys.exit(app.exec_())
