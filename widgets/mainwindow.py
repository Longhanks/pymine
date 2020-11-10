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

from os import path

from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication, Qt, QTimer, QPoint
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtGui import QCloseEvent

from widgets.newgamedialog import NewGameDialog
from widgets.gamewidget import GameWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        uic.loadUi(path.join(path.dirname(__file__), '..', 'ui', 'UI_MainWindow.ui'), self)

        self.actionNewGame.triggered.connect(self.showNewGameDialog)
        self.pushButtonNewGame.clicked.connect(self.showNewGameDialog)
        self.actionExit.triggered.connect(lambda: self.close())
        self.dialogIsVisible = False
        center = QApplication.desktop().availableGeometry(self).center()
        self.move(QPoint(center.x() - int(self.width() / 2), center.y() - int(self.height() / 2)))

    def showNewGameDialog(self) -> None:
        if self.dialogIsVisible:
            return
        self.dialogIsVisible = True

        dlg = NewGameDialog(self)
        if dlg.exec_():
            game = GameWidget(dlg.spinBoxRows.value(),
                              dlg.spinBoxColumns.value(),
                              dlg.spinBoxMines.value(),
                              parent=self)
            game.gameIsWon.connect(self.gameIsWon)
            game.gameIsLost.connect(self.gameIsLost)
            self.setCentralWidget(game)

            def cb():
                self.resize(0, 0)
                self.setFixedSize(self.size())

            QTimer.singleShot(0, Qt.CoarseTimer, cb)
            self.dialogIsVisible = False
        else:
            QCoreApplication.instance().quit()

    def gameIsWon(self) -> None:
        self.dialogIsVisible = True
        msgBox = QMessageBox(parent=self)
        msgBox.setWindowModality(Qt.WindowModal)
        msgBox.setWindowTitle('You won!')
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText('Congratulations! New game?')
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        if msgBox.exec_() == QMessageBox.No:
            QCoreApplication.instance().quit()
        else:
            self.dialogIsVisible = False
            self.showNewGameDialog()

    def gameIsLost(self) -> None:
        self.dialogIsVisible = True
        msgBox = QMessageBox(parent=self)
        msgBox.setWindowModality(Qt.WindowModal)
        msgBox.setWindowTitle('You lost!')
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText('Game over. New game?')
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        if msgBox.exec_() == QMessageBox.No:
            QCoreApplication.instance().quit()
        else:
            self.dialogIsVisible = False
            self.showNewGameDialog()

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.dialogIsVisible:
            event.ignore()
            return
        msgBox = QMessageBox(parent=self)
        msgBox.setWindowModality(Qt.WindowModal)
        msgBox.setWindowTitle('Confirm exit')
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText('Are you sure you want to quit?')
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        if msgBox.exec_() == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
