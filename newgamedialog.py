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

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
import os

from utilities import getResourcesPath

class NewGameDialog(QDialog):
    def __init__(self, parent=None):
        super(NewGameDialog, self).__init__(parent, Qt.Sheet)
        uic.loadUi(os.path.join(getResourcesPath(),'ui', 'newgamedialog.ui'), self)
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