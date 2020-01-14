import sys

from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,150)
    w.move(300,300)
    w.setWindowTitle('Thanks')
    w.show()
    sys.exit(app.exec_())

