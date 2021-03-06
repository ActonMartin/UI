import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDesktopWidget, QHBoxLayout, QWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        # 设置窗口的大小
        self.resize(400, 120)
        # 设置窗口标题
        self.setWindowTitle('退出应用程序')
        # 添加button
        self.button1 = QPushButton('退出应用程序1')
        # 将信号与槽关联
        self.button1.clicked.connect(self.onclick_button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法（自定义的槽）
    def onclick_button(self):
        sender = self.sender()
        print(sender.text())
        # print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
