#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python Minesweeper (pymine)
# Copyright (C) 2014 Andreas Schulz
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

from PyQt4 import uic, QtCore
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QMainWindow, QMessageBox
from os.path import join
import sys

from utilities import resource_path
from NewGameDialog import NewGameDialog
from Game import Game

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        uic.loadUi(resource_path(join('ui', 'MainWindow.ui')), self)
        self.actionNewGame.triggered.connect(self.showNewGameDialog)
        self.pushButtonNewGame.clicked.connect(self.showNewGameDialog)
        self.actionExit.triggered.connect(self.closeMe)
        self.setWindowTitle("pymine")
        
    def showNewGameDialog(self):
        dlg = NewGameDialog()
        if dlg.exec_():
            game = Game(self)
            self.setCentralWidget(game)
            game.addTiles(dlg.spinBoxRows.value(), dlg.spinBoxColumns.value(), dlg.spinBoxMines.value())
        else:
            QCoreApplication.instance().quit()
            
    def closeMe(self, event):
        if QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No) == QMessageBox.Yes:
            QCoreApplication.instance().quit()