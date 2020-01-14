import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin,self).__init__(parent)
        #设置主窗口的标题
        self.setWindowTitle('主窗口')
        #设置主窗口的尺寸
        self.resize(400,300)

        self.status = self.statusBar()
        self.status.showMessage('我只会显示5秒哦',5000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon())
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())