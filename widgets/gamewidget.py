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

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

from utilities import getResourcesPath
from widgets.tile import Tile


class GameWidget(QWidget):
    gameIsLost = pyqtSignal()
    gameIsWon = pyqtSignal()

    def __init__(self, rows, columns, mines, parent=None):
        super(GameWidget, self).__init__(parent)
        uic.loadUi(path.join(getResourcesPath(), 'ui', 'gamewidget.ui'), self)

        self.btns = []
        self.btnDict = {}

        for column in range(columns):
            for row in range(rows):
                btn = Tile(self)
                self.mainLayout.addWidget(btn, column, row)
                self.btns.append(btn)
                btn.myX = column
                btn.myY = row
                btn.setObjectName('btn_' + str(column) + '_' + str(row))
                btn.clickedSuccessfully.connect(self.checkIfGameIsWon)
                btn.clickedMine.connect(lambda: self.gameIsLost.emit())

        # apply the mines
        for myInt in self.getListOfInts((len(self.btns) - 1), mines):
            self.btns[myInt].isMine = True

        # add buttons to name-button dictionary
        for btn in self.btns:
            self.btnDict[str(btn.objectName())] = btn

        # add all neighbors of all buttons to the buttons
        for btn in self.btns:
            btnTopLeftStr = 'btn_' + str(btn.myX - 1) + '_' + str(btn.myY - 1)
            btnTopStr = 'btn_' + str(btn.myX) + '_' + str(btn.myY - 1)
            btnTopRightStr = 'btn_' + str(btn.myX + 1) + '_' + str(btn.myY - 1)
            btnLeftStr = 'btn_' + str(btn.myX - 1) + '_' + str(btn.myY)
            btnRightStr = 'btn_' + str(btn.myX + 1) + '_' + str(btn.myY)
            btnBottomLeftStr = 'btn_' + str(btn.myX - 1) + '_' + str(btn.myY + 1)
            btnBottomStr = 'btn_' + str(btn.myX) + '_' + str(btn.myY + 1)
            btnBottomRightStr = 'btn_' + str(btn.myX + 1) + '_' + str(btn.myY + 1)

            if btnTopLeftStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnTopLeftStr])
            if btnTopStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnTopStr])
            if btnTopRightStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnTopRightStr])
            if btnLeftStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnLeftStr])
            if btnRightStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnRightStr])
            if btnBottomLeftStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnBottomLeftStr])
            if btnBottomStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnBottomStr])
            if btnBottomRightStr in self.btnDict:
                btn.neighbors.append(self.btnDict[btnBottomRightStr])

            for neighbor in btn.neighbors:
                if neighbor.isMine:
                    btn.count = btn.count + 1


    def getListOfInts(self, numberRange, numberUniques):
        listOfInts = []
        while len(listOfInts) < numberUniques:
            newRand = (randint(0, numberRange))
            if newRand in listOfInts:
                pass
            else:
                listOfInts.append(newRand)
        return listOfInts

    def checkIfGameIsWon(self):
        for btn in self.btns:
            if not (btn.countIsVisible or btn.isMine):
                return
        self.gameIsWon.emit()

