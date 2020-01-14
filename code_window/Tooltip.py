import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QToolTip,QPushButton,QWidget
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initui()

    def initui(self):
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300,300,400,500)
        self.setWindowTitle('设置控件提示消息')

        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这个是一个按钮？')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())