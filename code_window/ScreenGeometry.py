import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton


def onclick_button():
    print('1')
    print("widget.x()= %d" % widget.x())
    print("widget.y()=%d" % widget.y())
    print('widget.width()=%d' % widget.width())
    print('widget.height()=%d' % widget.height())

    print('2')
    print("widget.geometry().x()=%d" % widget.geometry().x())
    print("widget.geometry().y()=%d" % widget.geometry().y())
    print("widget.geometry().width()=%d" % widget.geometry().width())
    print("widget.geometry().height()=%d" % widget.geometry().height())

    print('3')
    print("widget.frameGeometry().x()=%d" % widget.frameGeometry().x())
    print("widget.frameGeometry().y()=%d" % widget.frameGeometry().y())
    print("widget.frameGeometry().width()=%d" % widget.frameGeometry().width())
    print("widget.frameGeometry().height()=%d" % widget.frameGeometry().height())


app = QApplication(sys.argv)

widget = QWidget()
bth = QPushButton(widget)
bth.setText('按钮')
bth.clicked.connect(onclick_button)
bth.move(24,100)
widget.resize(300,200)      # 设置的工作区的尺寸
widget.move(250,200)
widget.setWindowTitle('屏幕坐标系')
widget.show()
sys.exit(app.exec_())

