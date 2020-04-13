#!/usr/bin/env python3

import sys

from PySide2.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)


def open_app(argv: list):
    app = QApplication(argv)
    win = MainWindow()
    win.resize(800, 600)
    win.show()
    return app.exec_()


if __name__ == '__main__':
    open_app(sys.argv)
