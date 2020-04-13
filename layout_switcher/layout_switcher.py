#!/usr/bin/env python3

import sys

from PySide2.QtCore import QSize, Slot
from PySide2.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QRadioButton, QVBoxLayout, QWidget


class MainWindow(QWidget):
    apply_button = None
    close_button = None

    redmond_example_picture = None
    aqua_example_picture = None
    unity_example_picture = None
    classic_example_picture = None
    basic_example_picture = None

    redmond_radiobutton = None
    aqua_radiobutton = None
    unity_radiobutton = None
    classic_radiobutton = None
    basic_radiobutton = None

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
        self.close_button.clicked.connect(self.close_window)

        # Redmond
        self.redmond_example_picture = QLabel()
        self.redmond_radiobutton = QRadioButton("Redmond")
        self.redmond_radiobutton.clicked.connect(self.redmond_selected)
        redmond_box = self.create_grid_box(self.redmond_example_picture, self.redmond_radiobutton)

        # Aqua
        self.aqua_example_picture = QLabel()
        self.aqua_radiobutton = QRadioButton("Aqua")
        self.aqua_radiobutton.clicked.connect(self.aqua_selected)
        aqua_box = self.create_grid_box(self.aqua_example_picture, self.aqua_radiobutton)

        # Unity
        self.unity_example_picture = QLabel()
        self.unity_radiobutton = QRadioButton("Unity")
        self.unity_radiobutton.clicked.connect(self.unity_selected)
        unity_box = self.create_grid_box(self.unity_example_picture, self.unity_radiobutton)

        # Classic
        self.classic_example_picture = QLabel()
        self.classic_radiobutton = QRadioButton("Classic")
        self.classic_radiobutton.clicked.connect(self.classic_selected)
        classic_box = self.create_grid_box(self.classic_example_picture, self.classic_radiobutton)

        # Basic
        self.basic_example_picture = QLabel()
        self.basic_radiobutton = QRadioButton("Basic")
        self.basic_radiobutton.clicked.connect(self.basic_selected)
        basic_box = self.create_grid_box(self.basic_example_picture, self.basic_radiobutton)

        self.grid_layout.addWidget(redmond_box, 0, 0, 1, 1)
        self.grid_layout.addWidget(aqua_box, 0, 1, 1, 1)
        self.grid_layout.addWidget(unity_box, 0, 2, 1, 1)
        self.grid_layout.addWidget(classic_box, 1, 0, 1, 1)
        self.grid_layout.addWidget(basic_box, 1, 1, 1, 1)

    @staticmethod
    def create_grid_box(example_image: QLabel, button: QRadioButton):
        box = QWidget()
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(example_image)
        vertical_layout.addWidget(button)
        box.setLayout(vertical_layout)
        return box

    def resizeEvent(self, event):
        self.layout_area.resize(self.width(), self.height() - 50)
        self.button_area.move(0, self.height() - 50)
        self.button_area.resize(self.width(), 50)

        self.apply_button.move(self.width() - 160, 5)
        self.close_button.move(self.width() - 80, 5)

    @Slot()
    def close_window(self):
        self.close()

    @Slot()
    def redmond_selected(self):
        if self.aqua_radiobutton.isChecked():
            self.aqua_radiobutton.setChecked(False)
        if self.unity_radiobutton.isChecked():
            self.unity_radiobutton.setChecked(False)
        if self.classic_radiobutton.isChecked():
            self.classic_radiobutton.setChecked(False)
        if self.basic_radiobutton.isChecked():
            self.basic_radiobutton.setChecked(False)

    @Slot()
    def aqua_selected(self):
        if self.redmond_radiobutton.isChecked():
            self.redmond_radiobutton.setChecked(False)
        if self.unity_radiobutton.isChecked():
            self.unity_radiobutton.setChecked(False)
        if self.classic_radiobutton.isChecked():
            self.classic_radiobutton.setChecked(False)
        if self.basic_radiobutton.isChecked():
            self.basic_radiobutton.setChecked(False)

    @Slot()
    def unity_selected(self):
        if self.redmond_radiobutton.isChecked():
            self.redmond_radiobutton.setChecked(False)
        if self.aqua_radiobutton.isChecked():
            self.aqua_radiobutton.setChecked(False)
        if self.classic_radiobutton.isChecked():
            self.classic_radiobutton.setChecked(False)
        if self.basic_radiobutton.isChecked():
            self.basic_radiobutton.setChecked(False)

    @Slot()
    def classic_selected(self):
        if self.redmond_radiobutton.isChecked():
            self.redmond_radiobutton.setChecked(False)
        if self.aqua_radiobutton.isChecked():
            self.aqua_radiobutton.setChecked(False)
        if self.unity_radiobutton.isChecked():
            self.unity_radiobutton.setChecked(False)
        if self.basic_radiobutton.isChecked():
            self.basic_radiobutton.setChecked(False)

    @Slot()
    def basic_selected(self):
        if self.redmond_radiobutton.isChecked():
            self.redmond_radiobutton.setChecked(False)
        if self.aqua_radiobutton.isChecked():
            self.aqua_radiobutton.setChecked(False)
        if self.unity_radiobutton.isChecked():
            self.unity_radiobutton.setChecked(False)
        if self.classic_radiobutton.isChecked():
            self.classic_radiobutton.setChecked(False)


def open_app(argv: list):
    app = QApplication(argv)
    win = MainWindow()
    win.resize(800, 600)
    win.show()
    return app.exec_()


if __name__ == '__main__':
    open_app(sys.argv)
