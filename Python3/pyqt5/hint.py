import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('sansSerif', 10))
        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('提示<b>提示')
        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('按钮', self)
        btn.setToolTip('QPushButton')
        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())

        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("QToolTip")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
