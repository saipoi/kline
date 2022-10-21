import os
import sys
import Kline
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Kline')
        self.setGeometry(5, 30, 1850, 1100)
        self.browser = QWebEngineView()
        # #加载外部的web界面
        url = os.getcwd() + os.path.sep + 'kline_volume_signal.html'
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    Kline.ShowInfo()
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
