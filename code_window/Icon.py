import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin,self).__init__(parent)
        self.initui()

    def initui(self):
        self.setGeometry(200,300,400,500)
        #设置主窗口的标题
        self.setWindowTitle('设置图标')
        #设置窗口标题
        self.setWindowIcon(QIcon('../image/thunder.ico'))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon())
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())