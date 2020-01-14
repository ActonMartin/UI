"""
为类添加多个信号
"""
from PyQt5.QtCore import *


class MultiSignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int, str)
    signal4 = pyqtSignal(list)
    signal5 = pyqtSignal(dict)
    # 声明一个重载的信号,也就是槽的参数可以是int和str的类型，也可以是一个str类型的参数
    signal6 = pyqtSignal([int, str], [str])

    def __init__(self):
        super(MultiSignal, self).__init__()
        self.signal1.connect(self.signalcall1)
        self.signal2.connect(self.signalcall2)
        self.signal3.connect(self.signalcall3)
        self.signal4.connect(self.signalcall4)
        self.signal5.connect(self.signalcall5)
        self.signal6[str].connect(self.signalcall6overload)
        self.signal6[int, str].connect(self.signalcall6)

        self.signal1.emit()
        self.signal2.emit(10)
        self.signal3.emit(1, "hello world")
        self.signal4.emit([1, 2, 3, 4, 5, 6])
        self.signal5.emit({"name": "bill", "age": 30})
        self.signal6[int, str].emit(20, "test")
        self.signal6[str].emit("test")

    # 定义的槽函数
    @staticmethod
    def signal_call1():
        print("signal1 emit")

    @staticmethod
    def signal_call2(val):
        print("signal2 emit,value:", val)

    @staticmethod
    def signal_call3(val, text):
        print("signal3 emit,value:",val,text)

    @staticmethod
    def signal_call4(val):
        print("signal4 emit,value:",val)

    @staticmethod
    def signal_call5(val):
        print("signal5 emit,value:",val)

    @staticmethod
    def signal_call6(val, text):
        print("signal6 emit,value:",val,text)

    @staticmethod
    def signal_call6overload(val):
        print("signal6 overload emit,value:", val)


if __name__ == "__main__":
    multi_signal = MultiSignal()
