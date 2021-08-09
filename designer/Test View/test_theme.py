import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from themetester import *

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

with open("../style/davtheme.qss", 'r') as file:
    qss = file.read()
    app.setStyleSheet(qss)

window_ui = Ui_MainWindow()
window_ui.setupUi(window)
window.show()
sys.exit(app.exec_())