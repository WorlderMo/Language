# -*- coding: utf-8 -*-
# @Date    : 2018-06-08 16:24:15
# @Author  : mohailang (1198534595@qq.com)


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon, QIntValidator, QDoubleValidator
from PyQt5.QtCore import Qt, QUrl, QThread

class UI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('星巴克数据分析')
        self.setWindowIcon(QIcon('image/StarBucks.png'))

        self.mainWidget = QWidget()  # 主窗体控件
        self.mainLayout = QGridLayout()  # 主窗体layout

        self.menuBar()  # 菜单栏
        self.statusBar()  # 状态栏
        self.setShowQueryTimeMenu()  # 显示时延菜单选项

        self.setShowButton()  # 设置显示统计图的按钮
        self.setFindInfoWidget()

        self.setWebEngineView()

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

        self.center()  # 居中窗口， 但固定窗口大小后失效
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setShowQueryTimeMenu(self):
        menuBar = self.menuBar()
        viewMenu = menuBar.addMenu('View')

        showQueryTimeMenu = QAction(QIcon('image/time.png'), 'show time', self)
        showQueryTimeMenu.setShortcut('Ctrl+1')
        showQueryTimeMenu.setStatusTip('显示时延')

        viewMenu.addAction(showQueryTimeMenu)



    def setWebEngineView(self):
        self.webEngine = QWebEngineView(self)
        self.mainLayout.addWidget(self.webEngine, 1, 8, 11, 15)

    # top-k的输入框，按钮的控件
    def setFindInfoWidget(self):
        longitudeLabel = QLabel()
        latitudeLabel = QLabel()
        rangeLabel = QLabel()
        kLabel = QLabel()
        keyWordLabel = QLabel()

        longitudeLabel.setText("经度: ")
        latitudeLabel.setText("纬度: ")
        rangeLabel.setText("range:")
        kLabel.setText("k: ")
        keyWordLabel.setText("关键词：")

        self.longitudeEdit = QLineEdit()
        self.latitudeEdit = QLineEdit()
        self.rangeEdit = QLineEdit()
        self.kEdit = QLineEdit()
        self.keyWordEdit = QLineEdit()

        longitudeValidator = QDoubleValidator(self)
        longitudeValidator.setRange(-180.00, 180.00)
        longitudeValidator.setNotation(QDoubleValidator.StandardNotation)
        longitudeValidator.setDecimals(2)
        self.longitudeEdit.setValidator(longitudeValidator)

        latitudeValidator = QDoubleValidator(self)
        latitudeValidator.setRange(-90.00, 90.00)
        latitudeValidator.setNotation(QDoubleValidator.StandardNotation)
        latitudeValidator.setDecimals(2)
        self.latitudeEdit.setValidator(latitudeValidator)

        kIntValidator = QIntValidator(self)
        kIntValidator.setRange(0, 25000)
        self.rangeEdit.setPlaceholderText("单位: km")
        self.rangeEdit.setValidator(kIntValidator)

        self.findRangeButton = QPushButton()
        self.findRangeButton.setText("查找range")
        self.findRangeButton.setEnabled(False)

        self.findTopKButton = QPushButton()
        self.findTopKButton.setText("查找top-k")
        self.findTopKButton.setEnabled(False)

        self.longitudeEdit.setStatusTip("经度取值范围: -180.00-180.00")
        self.latitudeEdit.setStatusTip("纬度取值范围: -180.00-180.00")
        self.rangeEdit.setStatusTip("半径取值: 0-25000")

        vBox = QVBoxLayout(self)
        vBox.addWidget(longitudeLabel)
        vBox.addWidget(self.longitudeEdit, 0)
        vBox.addWidget(latitudeLabel)
        vBox.addWidget(self.latitudeEdit, 0)
        vBox.addWidget(rangeLabel)
        vBox.addWidget(self.rangeEdit, 0)
        vBox.addWidget(kLabel)
        vBox.addWidget(self.kEdit, 0)
        vBox.addWidget(keyWordLabel)
        vBox.addWidget(self.keyWordEdit, 0)
        vBox.addWidget(self.findRangeButton, 0)
        vBox.addWidget(self.findTopKButton, 0)

        self.longitudeEdit.setEnabled(False)
        self.latitudeEdit.setEnabled(False)
        self.rangeEdit.setEnabled(False)
        self.kEdit.setEnabled(False)
        self.keyWordEdit.setEnabled(False)

        hWidget = QWidget()
        hWidget.setLayout(vBox)
        self.mainLayout.addWidget(hWidget, 2, 3, 6, 4)

    # 设置基本按钮， 后续可能要重写
    def setShowButton(self):
        self.drawMapButton = QPushButton('世界分布图', self)
        self.drawColorMapButton = QPushButton('国家分布彩色图', self)
        self.countStoreByTimezoneButton_bar = QPushButton('时区店铺数量柱状图', self)
        self.countStoreByTimezoneButton_pie = QPushButton('时区店铺数量饼图', self)
        self.countStoreByCountryButton_bar = QPushButton('国家店铺数量柱状图', self)
        self.countStoreByCountryButton_pie = QPushButton('国家店铺数量饼图', self)

        self.drawMapButton.setEnabled(False)
        self.drawColorMapButton.setEnabled(False)
        self.countStoreByTimezoneButton_bar.setEnabled(False)
        self.countStoreByTimezoneButton_pie.setEnabled(False)
        self.countStoreByCountryButton_bar.setEnabled(False)
        self.countStoreByCountryButton_pie.setEnabled(False)

        self.countStoreByTimezoneButton_bar.clicked.connect(
            lambda: self.drawBar(self.csv_file['Timezone'],
                                 'html/timezoneBar.html', '时区店铺数量柱状图'))
        self.countStoreByTimezoneButton_pie.clicked.connect(
            lambda: self.drawPie(self.csv_file['Timezone'],
                                 'html/timezonePie.html', '时区店铺数量饼图'))
        self.countStoreByCountryButton_bar.clicked.connect(
            lambda: self.drawBar(self.csv_file['Country'],
                                 'html/countryBar.html', '国家店铺数量柱状图'))
        self.countStoreByCountryButton_pie.clicked.connect(
            lambda: self.drawPie(self.csv_file['Country'],
                                 'html/countryPie.html', '国家店铺数量饼图'))

        # 将旧的需求加入到扩展控件中
        self.extensionWidget = QWidget()
        vBox = QVBoxLayout(self)
        vBox.addWidget(self.drawMapButton)
        vBox.addWidget(self.drawColorMapButton)
        vBox.addWidget(self.countStoreByTimezoneButton_bar)
        vBox.addWidget(self.countStoreByTimezoneButton_pie)
        vBox.addWidget(self.countStoreByCountryButton_bar)
        vBox.addWidget(self.countStoreByCountryButton_pie)
        self.extensionWidget.setLayout(vBox)
        self.extensionWidget.hide()

        # 控制显示和隐藏
        self.extensionButton = QPushButton(">>", self)
        self.extensionButton.setCheckable(True)
        self.extensionButton.setAutoDefault(False)
        self.extensionButton.toggled.connect(self.showExtension)

        self.mainLayout.addWidget(self.extensionButton, 1, 3, 1, 1)
        self.mainLayout.addWidget(self.extensionWidget, 1, 1, 7, 1)

    def showExtension(self):
        self.extensionWidget.setVisible(not self.extensionWidget.isVisible())
        if self.extensionWidget.isVisible():
            self.extensionButton.setText("<<")
        else:
            self.extensionButton.setText(">>")


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ui=UI()
    sys.exit(app.exec_())