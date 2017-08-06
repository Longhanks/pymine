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

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from utilities import getResourcesPath


class NewGameDialog(QDialog):
    def __init__(self, parent=None):
        super(NewGameDialog, self).__init__(parent, Qt.Sheet)
        uic.loadUi(path.join(getResourcesPath(), 'ui', 'newgamedialog.ui'), self)
        self.comboBoxDefaultModes.currentIndexChanged.connect(self.checkNewMode)

    def checkNewMode(self):
        if self.comboBoxDefaultModes.currentText() == 'Beginner':
            self.spinBoxRows.setEnabled(False)
            self.spinBoxRows.setValue(9)
            self.spinBoxColumns.setEnabled(False)
            self.spinBoxColumns.setValue(9)
            self.spinBoxMines.setEnabled(False)
            self.spinBoxMines.setValue(10)

        elif self.comboBoxDefaultModes.currentText() == 'Intermediate':
            self.spinBoxRows.setEnabled(False)
            self.spinBoxRows.setValue(16)
            self.spinBoxColumns.setEnabled(False)
            self.spinBoxColumns.setValue(16)
            self.spinBoxMines.setEnabled(False)
            self.spinBoxMines.setValue(40)

        elif self.comboBoxDefaultModes.currentText() == 'Expert':
            self.spinBoxRows.setEnabled(False)
            self.spinBoxRows.setValue(30)
            self.spinBoxColumns.setEnabled(False)
            self.spinBoxColumns.setValue(16)
            self.spinBoxMines.setEnabled(False)
            self.spinBoxMines.setValue(99)

        elif self.comboBoxDefaultModes.currentText() == 'Custom':
            self.spinBoxRows.setEnabled(True)
            self.spinBoxColumns.setEnabled(True)
            self.spinBoxMines.setEnabled(True)

