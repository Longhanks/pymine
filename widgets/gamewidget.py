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

from os import path
from random import randint
from typing import List, Tuple, Iterator

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

from utilities import getResourcesPath
from widgets.tile import Tile


class GameWidget(QWidget):
    gameIsLost = pyqtSignal()
    gameIsWon = pyqtSignal()

    def __init__(self, rows: int, columns: int, mines: int, parent=None):
        super(GameWidget, self).__init__(parent)
        uic.loadUi(path.join(getResourcesPath(), 'ui', 'gamewidget.ui'), self)

        self.matrix: List[List[Tile]] = []

        for column in range(columns):
            self.matrix.append([])
            for row in range(rows):
                btn = Tile(x=column, y=row, parent=self)
                self.mainLayout.addWidget(btn, row, column)
                btn.clickedSuccessfully.connect(self.clickSucceeded)
                btn.clickedMine.connect(lambda: self.gameIsLost.emit())
                self.matrix[column].append(btn)

        # apply the mines
        counter = 0
        while counter < mines:
            x = randint(0, columns - 1)
            y = randint(0, rows - 1)
            if self.matrix[x][y].isMine:
                continue
            else:
                self.matrix[x][y].isMine = True
                counter += 1

        # set the count
        for column in self.matrix:
            for tile in column:
                for coords in self.getValidMatrixIndices(tile.x, tile.y):
                    neighbor = self.matrix[coords[0]][coords[1]]
                    if neighbor.isMine:
                        tile.count += 1

    def clickSucceeded(self, column: int, row: int) -> None:
        btn = self.matrix[column][row]
        if btn.count == 0:
            for coords in self.getValidMatrixIndices(column, row):
                self.matrix[coords[0]][coords[1]].clickedTile(ignoreMark=True)
        self.checkIfGameIsWon()

    def getValidMatrixIndices(self, x: int, y: int) -> Iterator[Tuple[int, int]]:
        topLeft = (x - 1, y - 1)
        top = (x, y - 1)
        topRight = (x + 1, y - 1)
        left = (x - 1, y)
        right = (x + 1, y)
        bottomLeft = (x - 1, y + 1)
        bottom = (x, y + 1)
        bottomRight = (x + 1, y + 1)

        def matrixFilter(coords: Tuple[int, int]) -> bool:
            if coords[0] >= 0 and coords[1] >= 0:
                columns = len(self.matrix)
                rows = len(self.matrix[0])
                if coords[0] < columns and coords[1] < rows:
                    return True
            return False

        return filter(matrixFilter, [topLeft, top, topRight, left, right, bottomLeft, bottom, bottomRight])

    def checkIfGameIsWon(self) -> None:
        for column in self.matrix:
            for btn in column:
                countIsVisible = btn.text() and btn.text() != 'F'
                if not (countIsVisible or btn.isMine):
                    return
        self.gameIsWon.emit()

