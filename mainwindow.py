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

import os

from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication, Qt, QTimer
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from utilities import getResourcesPath
from newgamedialog import NewGameDialog
from game import Game


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        uic.loadUi(os.path.join(getResourcesPath(),'ui', 'mainwindow.ui'), self)
        
        self.actionNewGame.triggered.connect(self.showNewGameDialog)
        self.pushButtonNewGame.clicked.connect(self.showNewGameDialog)
        self.actionExit.triggered.connect(self.closeMe)
        self.setWindowTitle('pymine')
        
    def showNewGameDialog(self):
        dlg = NewGameDialog(self)
        if dlg.exec_():
            game = Game(dlg.spinBoxRows.value(), dlg.spinBoxColumns.value(), dlg.spinBoxMines.value(), parent=self)
            self.setCentralWidget(game)
            QTimer.singleShot(0, Qt.CoarseTimer, lambda: self.resize(0, 0))
        else:
            QCoreApplication.instance().quit()
            
    def closeMe(self, event):
        msgBox = QMessageBox(parent=self)
        msgBox.setWindowModality(Qt.WindowModal)
        msgBox.setWindowTitle('Confirm exit')
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText('Are you sure you want to quit?')
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        if msgBox.exec_() == QMessageBox.Yes:
            QCoreApplication.instance().quit()
