# -*- coding: utf-8 -*-
# @Date    : 2018-06-08 17:18:36
# @Author  : mohailang (1198534595@qq.com)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QFileInfo


class UI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar()

        self.mainWidget = QWidget()
        self.grid = QGridLayout()

        self.setButton()
        self.setWebView()
        self.setInfoButton()

        self.mainWidget.setLayout(self.grid)
        self.setCentralWidget(self.mainWidget)
        self.setGeometry(1000, 1000, 1000, 600)
        self.setWindowTitle("星巴克数据分析")
        self.center()
        self.show()

    def getData(self):

        # 获取输入框的值
        self.longitude = self.longitudeEdit.text()
        self.latitude = self.latitudeEdit.text()
        self.k = self.kEdit.text()
        self.keyWord = self.keyWordEdit.text()

        print(self.k)

    def setInfoButton(self):
        longitudeLabel = QLabel("经度: ")
        latitudeLabel = QLabel("纬度: ")
        kLabel = QLabel("k值: ")
        keyWordLabel = QLabel("关键词：")

        self.longitudeEdit = QLineEdit()
        self.latitudeEdit = QLineEdit()
        self.kEdit = QLineEdit()
        self.keyWordEdit = QLineEdit()

        findTopKButton = QPushButton("查找top-k")

        # findTopKButton 点击触发事件
        findTopKButton.clicked.connect(self.getData)

        self.kEdit.setPlaceholderText("单位: km")
        self.longitudeEdit.setStatusTip("经度取值范围: -180.00-180.00")
        self.latitudeEdit.setStatusTip("纬度取值范围: -180.00-180.00")
        self.kEdit.setStatusTip("请输入k值")
        self.keyWordEdit.setStatusTip("请输入关键字")

        vBox1 = QVBoxLayout()
        vBox1.addWidget(longitudeLabel)
        vBox1.addWidget(self.longitudeEdit)
        vBox1.addWidget(latitudeLabel)
        vBox1.addWidget(self.latitudeEdit)
        vBox1.addWidget(kLabel)
        vBox1.addWidget(self.kEdit)
        vBox1.addWidget(keyWordLabel)
        vBox1.addWidget(self.keyWordEdit)
        vBox1.addStretch(1)
        vBox1.addWidget(findTopKButton)

        inputWidgets = QWidget()
        inputWidgets.setLayout(vBox1)
        self.grid.addWidget(inputWidgets, 2, 24, 7, 4)

    def setWebView(self):
        self.webEngine = QWebEngineView()
        self.grid.addWidget(self.webEngine, 1, 8, 11, 15)

    def setButton(self):
        button1 = QPushButton('11111111')
        button2 = QPushButton('22222222')
        button3 = QPushButton('33333333')
        button4 = QPushButton('44444444')
        button5 = QPushButton('55555555')
        button6 = QPushButton('66666666')
        button7 = QPushButton('77777777')

        button1.clicked.connect(self.buttonClicked)
        button2.clicked.connect(self.buttonClicked)
        button3.clicked.connect(self.buttonClicked)
        button4.clicked.connect(self.buttonClicked)
        button5.clicked.connect(self.buttonClicked)
        button6.clicked.connect(self.buttonClicked)
        button7.clicked.connect(self.buttonClicked)

        vBox = QVBoxLayout()
        vBox.addWidget(button1)
        vBox.addWidget(button2)
        vBox.addWidget(button3)
        vBox.addWidget(button4)
        vBox.addWidget(button5)
        vBox.addWidget(button6)
        vBox.addWidget(button7)

        buttonWidgets = QWidget()
        buttonWidgets.setLayout(vBox)
        self.grid.addWidget(buttonWidgets, 2, 3, 7, 4)

    def buttonClicked(self):
        sender = self.sender()
        # 获取按钮名称
        title = sender.text()
        # 在状态栏显示按钮名称
        self.statusBar().showMessage(title)
        # 获取绝对路径
        url = QFileInfo(title+"html").absoluteFilePath()
        url = "file://" + url

        # 根据按钮名称来选择文件打开
        if title == "11111111":
            self.webEngine.load(QUrl(url))
        elif title == "22222222":
            self.webEngine.load(QUrl(url))
        elif title == "":
            pass
        # todo

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())
