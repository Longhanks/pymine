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

from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QCoreApplication

class Tile(QPushButton):
    rightClicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super(Tile, self).__init__(parent)
        self.mine = False
        self.neighbors = []
        self.myX = 0
        self.myY = 0
        self.count = 0
        self.done = False
        
    def checkMine(self):
        if self.text() == "F":
            return
        
        if self.mine:
            self.setText("M")
            if QMessageBox.question(self, "You Lost!", "Game over. New game?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No) == QMessageBox.No:
                QCoreApplication.instance().quit()
            else:
                self.parent().parent().showNewGameDialog()
                
        else:
            self.setText(str(self.count))
            self.done = True
            if self.count == 0:
                for nb in self.neighbors:
                    if nb.done == False:
                        nb.checkMine()
            
        if self.parent().checkIfDone():
            if QMessageBox.question(self, "You won!", "Congratilations! New game?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No) == QMessageBox.No:
                QCoreApplication.instance().quit()
            else:
                self.parent().parent().showNewGameDialog()
                
    def setMine(self):
        if self.done:
            if self.mine:
                pass
            else:
                return
            
        if self.text() == "F":
            self.setStyleSheet('QPushButton {color: black;}')
            self.setText("")
        else:
            self.setStyleSheet('QPushButton {color: red;}')
            self.setText("F")
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(True)
        if event.button() == Qt.RightButton:
            self.rightClicked.emit()
                
        