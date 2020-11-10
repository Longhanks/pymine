# -*- coding: utf-8 -*-
# Python Minesweeper (pymine)
#
# The MIT License (MIT)
#
# Copyright (c) 2014 - 2020 Andreas Schulz
#
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from PyQt5.QtWidgets import QFrame, QLabel, QSizePolicy, QVBoxLayout
from PyQt5.QtCore import QSize, Qt, pyqtSignal


class Tile(QFrame):
    clickedMine = pyqtSignal()
    clickedSuccessfully = pyqtSignal(int, int)

    def __init__(self, x: int, y: int, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setStyleSheet('QFrame { background-color: white; }')
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.isMine = False
        self.x = x
        self.y = y
        self.count = 0

    def sizeHint(self):
        return QSize(20, 20)

    def clickedTile(self, ignoreMark=False):
        if self.label.text() == 'F':
            if not ignoreMark:
                return
            else:
                self.rightClickedTile()

        elif self.label.text():
            return

        elif self.isMine:
            self.clickedMine.emit()
            return

        self.label.setText(str(self.count))
        self.clickedSuccessfully.emit(self.x, self.y)

    def rightClickedTile(self) -> None:
        if self.label.text() and self.label.text() != 'F':
            return

        if self.label.text() == 'F':
            self.label.setStyleSheet('QLabel { color: black; }')
            self.label.setText('')
        else:
            self.label.setStyleSheet('QLabel { color: red; }')
            self.label.setText('F')

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.clickedTile()
        if event.button() == Qt.RightButton:
            self.rightClickedTile()
