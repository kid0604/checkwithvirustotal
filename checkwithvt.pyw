""" ----- coding:utf-8 -----
@author: Kid0604

"""
import sys
from PyQt4 import QtGui, QtCore
from ui_checkwithvt import Ui_Form
import threading
from checker import VTChecker


class UI(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = UI()
    dlg.show()

    checker = VTChecker(dlg)
    t2 = threading.Thread(target=checker.start())
    t2.start()

    t1 = threading.Thread(target=app.exec_())
    t1.start()
