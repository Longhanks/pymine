# -*- coding: utf-8 -*-
# Python Minesweeper (pymine)
#
# The MIT License (MIT)
#
# Copyright (c) 2014 - 2017 Andreas Schulz
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

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, pyqtSignal


class Tile(QPushButton):
    rightClicked = pyqtSignal()
    clickedMine = pyqtSignal()
    clickedSuccessfully = pyqtSignal(int, int)

    def __init__(self, x: int, y: int, parent=None):
        super(Tile, self).__init__(parent)
        self.setMinimumSize(20, 20)
        self.setMaximumSize(20, 20)
        self.isMine: bool = False
        self.x: int = x
        self.y: int = y
        self.count: int = 0
        self.clicked.connect(self.clickedTile)
        self.rightClicked.connect(self.rightClickedTile)

    def clickedTile(self, ignoreMark: bool=False):
        if self.text() == 'F':
            if not ignoreMark:
                return
            else:
                self.rightClickedTile()

        elif self.text():
            return

        elif self.isMine:
            self.clickedMine.emit()
            return

        self.setText(str(self.count))
        self.clickedSuccessfully.emit(self.x, self.y)

    def rightClickedTile(self) -> None:
        if self.text() and self.text() != 'F':
            return

        if self.text() == 'F':
            self.setStyleSheet('QPushButton {color: black;}')
            self.setText('')
        else:
            self.setStyleSheet('QPushButton {color: red;}')
            self.setText('F')

    def mousePressEvent(self, event):
        super(Tile, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.clicked.emit(False)
        if event.button() == Qt.RightButton:
            self.rightClicked.emit()
