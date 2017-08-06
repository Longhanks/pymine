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
    clickedSuccessfully = pyqtSignal()

    def __init__(self, parent=None):
        super(Tile, self).__init__(parent)
        self.setMinimumSize(20, 20)
        self.setMaximumSize(20, 20)
        self.isMine = False
        self.neighbors = []
        self.myX = 0
        self.myY = 0
        self.count = 0
        self.countIsVisible = False
        self.clicked.connect(self.clickedTile)
        self.rightClicked.connect(self.rightClickedTile)

    def clickedTile(self):
        if self.text() == 'F':
            return

        elif self.countIsVisible:
            return

        elif self.isMine:
            self.clickedMine.emit()
            return

        self.setText(str(self.count))
        self.countIsVisible = True
        if self.count == 0:
            for nb in self.neighbors:
                if not nb.countIsVisible:
                    nb.clickedTile()
        self.clickedSuccessfully.emit()

    def rightClickedTile(self):
        if self.countIsVisible:
            return

        if self.text() == 'F':
            self.setStyleSheet('QPushButton {color: black;}')
            self.setText('')
        else:
            self.setStyleSheet('QPushButton {color: red;}')
            self.setText('F')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(False)
        if event.button() == Qt.RightButton:
            self.rightClicked.emit()

