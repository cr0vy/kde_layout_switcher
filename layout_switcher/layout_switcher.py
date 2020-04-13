#!/usr/bin/env python3

import sys

from PySide2.QtCore import QSize
from PySide2.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget


class MainWindow(QWidget):
    apply_button = None
    close_button = None

    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumSize(QSize(600, 400))

        self.layout_area = QWidget(self)
        self.button_area = QWidget(self)

        self.grid_layout = QGridLayout()
        self.layout_area.setLayout(self.grid_layout)

        self.setup_window()

    def setup_window(self):
        self.apply_button = QPushButton("Apply", self.button_area)
        self.apply_button.resize(75, 40)
        self.apply_button.setEnabled(False)

        self.close_button = QPushButton("Close", self.button_area)
        self.close_button.resize(75, 40)

    def resizeEvent(self, event):
        self.layout_area.resize(self.width(), self.height() - 50)
        self.button_area.move(0, self.height() - 50)
        self.button_area.resize(self.width(), 50)

        self.apply_button.move(self.width() - 160, 5)
        self.close_button.move(self.width() - 80, 5)


def open_app(argv: list):
    app = QApplication(argv)
    win = MainWindow()
    win.resize(800, 600)
    win.show()
    return app.exec_()


if __name__ == '__main__':
    open_app(sys.argv)
